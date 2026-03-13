# Tiburon GK Knowledgebase — MCP Setup
**Connect any AI model to the knowledgebase using the Model Context Protocol (MCP)**

This uses `@modelcontextprotocol/server-filesystem` — the simplest possible MCP server.
It gives the AI read access to the knowledgebase directory with no cloud hosting, no ongoing cost, and no API keys required.

---

## What You Get

- AI can read any file in the knowledgebase (build profiles, pinouts, sensor specs, shop manual, bolt database)
- AI can list directories and explore the structure
- Works with Claude, OpenAI-compatible models, Gemini, and any other model with an MCP client
- Completely local — no data leaves your machine (unless you explicitly configure a remote AI endpoint)

---

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or later (check: `node --version`)
- An AI client that supports MCP (see "Connecting" section below)

---

## Installation (One-Time)

```bash
# Install the filesystem MCP server globally
npm install -g @modelcontextprotocol/server-filesystem
```

That's it. No configuration files, no environment variables, no accounts.

---

## Running the MCP Server

```bash
# Point it at the Knowledgebase directory
npx @modelcontextprotocol/server-filesystem "C:\Users\YourName\Desktop\Tiburon Project\Knowledgebase"
```

The server starts and listens for MCP client connections. Keep this terminal open while using the AI.

---

## Connecting Your AI Client

### Claude Desktop

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tiburon-kb": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\YourName\\Desktop\\Tiburon Project\\Knowledgebase"
      ]
    }
  }
}
```

Restart Claude Desktop. The server launches automatically when Claude starts.

### Claude Code (CLI)

```bash
claude mcp add tiburon-kb npx @modelcontextprotocol/server-filesystem "C:\Users\YourName\Desktop\Tiburon Project\Knowledgebase"
```

### OpenAI-Compatible Clients (Continue, Cursor, etc.)

Most MCP-compatible editors support the same `mcpServers` config format as Claude Desktop. Check your editor's settings for "MCP Servers" and add:

```json
{
  "name": "tiburon-kb",
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-filesystem",
    "/path/to/Knowledgebase"
  ]
}
```

### LibreChat / Open-WebUI / Self-Hosted

If you're running a self-hosted OpenAI-compatible front-end:
1. Start the MCP server manually in a terminal (see "Running" above)
2. Configure your front-end to connect to the MCP endpoint (port is printed on startup)
3. Works with any model backend (Ollama, OpenAI API, Anthropic API, etc.)

---

## Sharing With the Community

When you push this repo to GitHub, other builders can:

1. Clone or download the repo
2. `npm install -g @modelcontextprotocol/server-filesystem`
3. Point the server at their local clone
4. Connect their AI of choice

**No accounts, no API keys, no subscriptions required** beyond whatever AI service they already use.

To share the config in your repo, update the path in `claude_desktop_config.json` to use a relative path or placeholder:

```json
"args": ["@modelcontextprotocol/server-filesystem", "./Knowledgebase"]
```

---

## What the AI Can Do

With MCP filesystem access, the AI can:
- `read_file` — read any `.md`, `.json`, `.pdf` file
- `list_directory` — explore the folder structure
- `search_files` — search for content across files

### Suggested Prompts

```
Read builds/white-tiburon/build-profile.md and summarize the current ECU wiring status.
```

```
Find all files that mention the Lowdoller fuel pressure sensor and list the AVI pin assignment.
```

```
Read hardware/aim-pdm/pdm-configuration-guide.md and help me configure the starter logic.
```

```
Search the fasteners/bolt-index.json for any M8x1.25 bolts.
```

---

## File Structure Reference

See `Knowledgebase/README.md` for the full directory layout.

Key entry points:
| Path | Contents |
|------|----------|
| `builds/{car}/build-profile.md` | Per-car equipment, wiring, known issues |
| `builds/{car}/signal-routing.md` | End-to-end signal routing |
| `hardware/aim-pdm/pdm-configuration-guide.md` | PDM output map and input configuration |
| `hardware/haltech/main-connector-26-pin-elite2500.md` | Haltech 26-pin pinout |
| `hardware/sensors/lowdoller-sensors.md` | Sensor specs and calibration |
| `common/opengk/ecm-pinouts.md` | Stock ECM connector pinouts |
| `fasteners/bolt-index.json` | Bolt database |

---

## Forum Data (Planned)

The `forum/` directory (planned) will contain selected threads from newtiburon.com, prioritizing posts from key contributors. See `forum/README.md` for scraping methodology and contributor priority list.

---

## Cost

**Zero.** The MCP server is free and open source. You pay only for whatever AI API calls your client makes — which you would be making anyway.
