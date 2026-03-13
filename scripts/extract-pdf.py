#!/usr/bin/env python3
"""
extract-pdf.py — Extract PDF pages as PNG images for Claude vision processing.

Usage:
    python scripts/extract-pdf.py extract <pdf_path> [--pages START-END] [--output DIR] [--dpi DPI]
    python scripts/extract-pdf.py manifest <pdf_path>
    python scripts/extract-pdf.py batch <pdf_path> --sections "EMA-2:2-7,EMA-28:28-41" --output DIR

Examples:
    python scripts/extract-pdf.py extract "Tiburon-Shop-Manual/EMA.pdf" --pages 2-7 --output .work/ema-specs/
    python scripts/extract-pdf.py manifest "Tiburon-Shop-Manual/EMA.pdf"
    python scripts/extract-pdf.py batch "Tiburon-Shop-Manual/EMA.pdf" --sections "specs:2-7,engine-block:8-27" --output .work/ema/
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import fitz  # pymupdf
except ImportError:
    print("ERROR: pymupdf not installed. Run: pip install pymupdf")
    sys.exit(1)


def extract_pages(pdf_path: str, start: int, end: int, output_dir: str, dpi: int = 200):
    """Extract a range of PDF pages as PNG images."""
    doc = fitz.open(pdf_path)
    total = len(doc)

    # Convert to 0-indexed
    start_idx = max(0, start - 1)
    end_idx = min(total, end)

    os.makedirs(output_dir, exist_ok=True)

    extracted = []
    for i in range(start_idx, end_idx):
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi)
        filename = f"page-{i + 1:03d}.png"
        filepath = os.path.join(output_dir, filename)
        pix.save(filepath)
        extracted.append({
            "page": i + 1,
            "file": filename,
            "path": filepath,
            "width": pix.width,
            "height": pix.height,
        })
        print(f"  Extracted page {i + 1}/{total} -> {filename} ({pix.width}x{pix.height})")

    # Write manifest
    manifest = {
        "source_pdf": os.path.basename(pdf_path),
        "source_path": pdf_path,
        "total_pages": total,
        "extracted_range": f"{start}-{end}",
        "dpi": dpi,
        "pages": extracted,
    }
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"  Manifest -> {manifest_path}")

    doc.close()
    return extracted


def show_manifest(pdf_path: str):
    """Show PDF info and page count."""
    doc = fitz.open(pdf_path)
    print(f"PDF: {os.path.basename(pdf_path)}")
    print(f"Pages: {len(doc)}")
    print(f"Path: {pdf_path}")

    # Try to detect text on first few pages (indicates OCR version)
    has_text = False
    for i in range(min(3, len(doc))):
        text = doc[i].get_text().strip()
        if len(text) > 10:
            has_text = True
            break

    print(f"Has text layer: {has_text}")
    if has_text:
        print("  (OCR version -- use scanned version for vision extraction)")
    else:
        print("  (Scanned version -- ideal for Claude vision extraction)")

    # Show page dimensions
    page = doc[0]
    rect = page.rect
    print(f"Page size: {rect.width:.0f} x {rect.height:.0f} points ({rect.width/72:.1f}\" x {rect.height/72:.1f}\")")

    doc.close()


def batch_extract(pdf_path: str, sections: str, output_dir: str, dpi: int = 200):
    """Extract multiple section ranges into separate subdirectories.

    sections format: "name:start-end,name:start-end,..."
    Example: "specs:2-7,engine-block:8-27,main-moving:28-41"
    """
    os.makedirs(output_dir, exist_ok=True)

    for section_spec in sections.split(","):
        section_spec = section_spec.strip()
        if ":" not in section_spec:
            print(f"  SKIP: Invalid format '{section_spec}' — expected 'name:start-end'")
            continue

        name, page_range = section_spec.split(":", 1)
        if "-" not in page_range:
            print(f"  SKIP: Invalid page range '{page_range}' — expected 'start-end'")
            continue

        start, end = page_range.split("-", 1)
        section_dir = os.path.join(output_dir, name.strip())

        print(f"\n[{name.strip()}] pages {start}-{end}")
        extract_pages(pdf_path, int(start), int(end), section_dir, dpi)

    print(f"\nDone. Output in: {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Extract PDF pages as PNG for Claude vision")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # extract command
    p_extract = subparsers.add_parser("extract", help="Extract page range as PNG images")
    p_extract.add_argument("pdf_path", help="Path to PDF file")
    p_extract.add_argument("--pages", default=None, help="Page range (e.g., 2-7). Default: all pages")
    p_extract.add_argument("--output", default="scripts/.work/extract", help="Output directory")
    p_extract.add_argument("--dpi", type=int, default=200, help="Resolution (default: 200)")

    # manifest command
    p_manifest = subparsers.add_parser("manifest", help="Show PDF info")
    p_manifest.add_argument("pdf_path", help="Path to PDF file")

    # batch command
    p_batch = subparsers.add_parser("batch", help="Extract multiple sections")
    p_batch.add_argument("pdf_path", help="Path to PDF file")
    p_batch.add_argument("--sections", required=True, help='Section specs: "name:start-end,name:start-end"')
    p_batch.add_argument("--output", default="scripts/.work/batch", help="Output directory")
    p_batch.add_argument("--dpi", type=int, default=200, help="Resolution (default: 200)")

    args = parser.parse_args()

    if args.command == "manifest":
        show_manifest(args.pdf_path)

    elif args.command == "extract":
        if args.pages:
            parts = args.pages.split("-")
            start, end = int(parts[0]), int(parts[1])
        else:
            doc = fitz.open(args.pdf_path)
            start, end = 1, len(doc)
            doc.close()
        print(f"Extracting pages {start}-{end} from {os.path.basename(args.pdf_path)}")
        extract_pages(args.pdf_path, start, end, args.output, args.dpi)

    elif args.command == "batch":
        print(f"Batch extracting from {os.path.basename(args.pdf_path)}")
        batch_extract(args.pdf_path, args.sections, args.output, args.dpi)


if __name__ == "__main__":
    main()
