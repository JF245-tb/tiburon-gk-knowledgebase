// ============================================================
// NewTiburon Forum Thread Extractor (XenForo)
// ============================================================
// Usage: Paste this entire script into the browser console or
// execute via Claude in Chrome's javascript_tool while on a
// NewTiburon thread page. Returns a JSON object with metadata
// and posts arrays ready for direct file write.
//
// For multi-page threads: run once per page, then merge the
// posts arrays. Metadata only needs to come from page 1.
//
// IMPORTANT: NewTiburon has aggressive ad-redirect scripts.
// Call window.stop() immediately after navigation before
// running this extractor.
//
// Selector compatibility: NewTiburon uses two DOM layouts
// depending on thread age/theme. This script tries both:
//   Layout A (standard XenForo): article.message--post
//   Layout B (NewTiburon custom): .js-post / .MessageCard
// ============================================================

(function extractThread() {
  // --- Expand all "See more" blocks first ---
  document.querySelectorAll('.js-expandLink').forEach(el => el.click());

  // --- Detect which DOM layout we're on ---
  const layoutA = document.querySelectorAll('article.message--post');
  const layoutB = document.querySelectorAll('.js-post, .MessageCard');
  const useLayoutB = layoutA.length === 0 && layoutB.length > 0;
  const articles = useLayoutB ? layoutB : layoutA;

  // --- Metadata (from page 1 only) ---
  const titleEl = document.querySelector('h1.p-title-value')
    || document.querySelector('.p-title-value')
    || document.querySelector('[class*="ThreadHeader"] h1');
  const title = titleEl ? titleEl.textContent.trim() : document.title;

  // Thread ID from URL
  const urlMatch = window.location.href.match(/\.(\d+)\/?/);
  const threadId = urlMatch ? urlMatch[1] : null;

  // Author and date from first post header
  const firstPost = articles[0] || null;
  let author = null;
  let dateCreated = null;

  if (firstPost) {
    // Layout A: [data-author] attribute
    const authorAttrEl = firstPost.querySelector('[data-author]');
    if (authorAttrEl) {
      author = authorAttrEl.getAttribute('data-author');
    } else {
      // Layout B: .MessageCard__user-info__name or similar
      const authorNameEl = firstPost.querySelector(
        '.MessageCard__user-info__name, [class*="user-info"] a, .message-userDetails a'
      );
      if (authorNameEl) author = authorNameEl.textContent.trim();
    }

    const dateEl = firstPost.querySelector('time.u-dt, time[datetime]');
    dateCreated = dateEl ? dateEl.getAttribute('datetime')?.split('T')[0] : null;
  }

  // Page info
  const pageNav = document.querySelector('.pageNav-main');
  const pageLinks = pageNav ? pageNav.querySelectorAll('a') : [];
  const totalPages = pageLinks.length > 0
    ? Math.max(...[...pageLinks].map(a => parseInt(a.textContent)).filter(n => !isNaN(n)))
    : 1;
  const currentPageEl = document.querySelector('.pageNav-page--current');
  const currentPage = currentPageEl ? parseInt(currentPageEl.textContent) : 1;

  // Reply count and view count from thread header
  let replyCount = null, viewCount = null;
  document.querySelectorAll('.p-description .pairs, .pairs--inline').forEach(pair => {
    const dt = pair.querySelector('dt');
    const dd = pair.querySelector('dd');
    if (dt && dd) {
      const label = dt.textContent.trim().toLowerCase();
      if (label.includes('repl')) replyCount = parseInt(dd.textContent.trim().replace(/,/g, '')) || null;
      if (label.includes('view')) {
        const raw = dd.textContent.trim();
        if (raw.includes('K')) viewCount = Math.round(parseFloat(raw) * 1000);
        else if (raw.includes('M')) viewCount = Math.round(parseFloat(raw) * 1000000);
        else viewCount = parseInt(raw.replace(/,/g, '')) || null;
      }
    }
  });

  // Stickied check
  const isStickied = !!document.querySelector('.p-title .label--sticky, .label[title="Sticky"]');

  // Section from breadcrumb
  const breadcrumbs = document.querySelectorAll('.p-breadcrumbs li');
  const section = breadcrumbs.length > 1
    ? breadcrumbs[breadcrumbs.length - 1].textContent.trim()
    : null;

  // --- Posts ---
  const posts = [];

  articles.forEach((article, idx) => {
    // --- Author ---
    let postAuthor = 'unknown';
    const authorAttrEl = article.querySelector('[data-author]');
    if (authorAttrEl) {
      postAuthor = authorAttrEl.getAttribute('data-author');
    } else {
      const authorNameEl = article.querySelector(
        '.MessageCard__user-info__name, [class*="user-info"] a, .message-userDetails a'
      );
      if (authorNameEl) postAuthor = authorNameEl.textContent.trim();
    }

    // --- Date ---
    const postDateEl = article.querySelector('time.u-dt, time[datetime]');
    const postDate = postDateEl ? postDateEl.getAttribute('datetime')?.split('T')[0] : null;

    // --- Post number ---
    const postNumEl = article.querySelector('.message-attribution-opposite a, [class*="post-number"] a');
    let postNumber = idx + 1;
    if (postNumEl) {
      const numMatch = postNumEl.textContent.trim().match(/#?(\d+)/);
      if (numMatch) postNumber = parseInt(numMatch[1]);
    }

    // --- Content ---
    // Try multiple content selectors
    const contentEl = article.querySelector(
      '.message-body .bbWrapper, .message-content.js-messageContent .bbWrapper, .message-content .bbWrapper, .bbWrapper'
    );
    let content = '';
    let hasImages = false;
    const imageDescriptions = [];

    if (contentEl) {
      // Clone to process without mutating DOM
      const clone = contentEl.cloneNode(true);

      // Replace img elements with [IMAGE: alt] placeholders
      clone.querySelectorAll('img').forEach(img => {
        hasImages = true;
        const alt = img.getAttribute('alt') || img.getAttribute('title') || 'photo';
        const placeholder = document.createTextNode(`[IMAGE: ${alt}]`);
        img.parentNode.replaceChild(placeholder, img);
        imageDescriptions.push(alt);
      });

      // Replace blockquotes with [QUOTE by author] markers
      clone.querySelectorAll('.bbCodeBlock--quote').forEach(q => {
        const quoteAuthor = q.querySelector('.bbCodeBlock-title')?.textContent?.trim() || '';
        const quoteBody = q.querySelector('.bbCodeBlock-expandContent, .bbCodeBlock-content')
          ?.textContent?.trim() || '';
        const short = quoteBody.length > 120 ? quoteBody.substring(0, 120) + '...' : quoteBody;
        const placeholder = document.createTextNode(`[QUOTE ${quoteAuthor}: ${short}]`);
        q.parentNode.replaceChild(placeholder, q);
      });

      content = clone.textContent.trim()
        .replace(/\n{3,}/g, '\n\n')  // collapse triple+ newlines
        .replace(/\t/g, ' ');         // tabs to spaces
    }

    const post = {
      post_number: postNumber,
      author: postAuthor,
      date: postDate,
      content: content,
      is_op: idx === 0 && currentPage === 1,
      has_images: hasImages
    };

    if (hasImages && imageDescriptions.length > 0) {
      post.image_descriptions = imageDescriptions;
    }

    posts.push(post);
  });

  // --- Unique participants across visible posts ---
  const participants = [...new Set(posts.map(p => p.author))];

  // --- Last post info ---
  const lastPost = posts[posts.length - 1];

  // --- Build result ---
  const result = {
    _layout: useLayoutB ? 'B (MessageCard)' : 'A (standard XenForo)',
    _post_count: posts.length,
    metadata: {
      thread_id: threadId,
      title: title,
      url: window.location.href.split('page-')[0].replace(/\/$/, ''),
      forum: 'newtiburon',
      section: section,
      author: author,
      date_created: dateCreated,
      reply_count: replyCount,
      view_count: viewCount,
      participants: null,  // filled after all pages merged
      page_count: totalPages,
      current_page: currentPage,
      is_stickied: isStickied,
      last_post_date: lastPost ? lastPost.date : null,
      last_post_by: lastPost ? lastPost.author : null,
      extracted: new Date().toISOString().split('T')[0],
      extracted_by: 'JF245-tb'
    },
    posts: posts,
    _page_participants: participants
  };

  // --- Output ---
  // Copy to clipboard for easy paste
  if (navigator.clipboard) {
    navigator.clipboard.writeText(JSON.stringify(result, null, 2))
      .then(() => console.log('Thread data copied to clipboard!'))
      .catch(() => {});
  }

  return JSON.stringify(result);
})();
