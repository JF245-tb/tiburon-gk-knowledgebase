# MCP Setup Guide — Step by Step
**From the example config to a working AI session with your build context loaded**

This walks you through converting `claude_desktop_config.example.json` into a working configuration, and then shows how to use it effectively for PDM and build questions.

---

## Step 1 — Install Node.js (if not already installed)

1. Go to [nodejs.org](https://nodejs.org/) and download the LTS version
2. Run the installer with defaults
3. Verify: open a new terminal and run `node --version` — should show v18 or later

---

## Step 2 — Find your Claude Desktop config file

On Windows, the config file lives at:
```
%APPDATA%\Claude\claude_desktop_config.json
```

To open it:
- Press `Win + R`, type `%APPDATA%\Claude\` and hit Enter
- Open `claude_desktop_config.json` in any text editor (Notepad, VS Code, etc.)
- If the file doesn't exist yet, create it

---

## Step 3 — Add the knowledgebase server

Open `claude_desktop_config.json` and add (or merge) the `mcpServers` block below.

**Replace `Julian` with your actual Windows username if different.**

```json
{
  "mcpServers": {
    "tiburon-kb": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\Julian\\Desktop\\Tiburon Project\\Knowledgebase"
      ]
    }
  }
}
```

If your config already has other MCP servers, add `tiburon-kb` inside the existing `mcpServers` block — don't create a second one.

**Verify the path** — open File Explorer and confirm that folder exists:
```
C:\Users\Julian\Desktop\Tiburon Project\Knowledgebase
```

---

## Step 4 — Restart Claude Desktop

Close Claude Desktop completely (check the system tray — right-click and Quit if it's running in the background).

Reopen it. The MCP server launches automatically when Claude starts. You'll see a hammer icon (🔨) near the message box if MCP tools are loaded.

---

## Step 5 — Start a session with build context

At the start of any build or wiring session, paste this as your first message:

```
You have access to the Tiburon knowledgebase via the tiburon-kb MCP server.

Before answering any questions:
1. Read builds/white-tiburon/build-profile.json — use it to answer AVI, PDM,
   and wiring questions without asking me to re-specify my setup each time.
2. For factory specs, prefer common/shop-manual/ and common/electrical-manual/
   (Tier 1 — highest authority).
3. For ECU/PDM community knowledge, use common/opengk/.
4. Always cite file and page_ref when giving specs or procedures.
```

That's it. Claude now knows your AVI assignments, PDM map, ignition config, and sensor details for the rest of the session.

---

## PDM — Example Queries

Once the session is loaded, try these to confirm it's working:

---

**"Which PDM output powers the fuel pump, and what's the trigger logic?"**

Expected answer (from `build-profile.json` + `hardware/aim-pdm/pdm-configuration-guide.md`):
> HP3 (pins A24+A25), 15A overcurrent protection. Trigger: `FP_PRIME_AND_RUN` — 3-second prime on IGN on, then tracks RPM > 50 via CAN from Haltech. Key 06 (Fuel Override) on keypad bypasses the RPM condition and runs the pump regardless.

---

**"What CAN speed is the Haltech running to the PDM, and what pins?"**

Expected answer (from `build-profile.json`):
> CAN0, 1 Mbps. Haltech 26-pin pin 23 (CAN H, white wire) → PDM A22. 26-pin pin 24 (CAN L, blue wire) → PDM A11.

---

**"Walk me through Phase 1.4 — fan PWM logic — and tell me if anything's unclear."**

Expected answer (from `builds/white-tiburon/weekend-tasks.md`):
> The guide lists simulating ECT via CAN in Race Studio to test the 4 duty cycle bands (25% / 50% / 75% / 98%), manual override with Key 05, and the loss-of-CAN failsafe (HP2 goes to 98% after 5s with no CAN signal). [Then Claude can flag anything ambiguous or missing in the procedure.]

---

**"What's the wiring for a Lowdoller oil pressure sensor — all 5 wires?"**

Expected answer (from `build-profile.json` + `hardware/sensors/lowdoller-sensors.md`):
> AVI3 assignment. Red → +5V (34-pin pin 9, orange, 100mA supply). Black → signal GND. Yellow (pressure signal) → 34-pin pin 17 (O/R wire) → AVI3. White → signal GND. Green (temp signal) → 34-pin pin 2 (O/Y wire) → AVI4. Calibration: PSI = (V − 0.5) × 37.5 for 0–150 PSI range.

---

## For the Blue Car (OEM ECU)

Create `builds/blue-tiburon/build-profile.json` from `builds/template/build-profile-template.json` and set:

```json
{
  "build_id": "blue-tiburon",
  "ecu": {
    "make": "Siemens",
    "model": "SIMK43",
    "oem_ecu": true
  }
}
```

Then change the session prompt to load `builds/blue-tiburon/build-profile.json` instead. The rest of the workflow is the same.

---

## For Community Members

1. Clone the repo (link in README)
2. Follow Steps 1–4 above, changing the path to wherever you cloned it:
   ```
   "C:\\Users\\YourName\\Desktop\\tiburon-gk-knowledgebase\\Knowledgebase"
   ```
3. Create your own `builds/{your-car}/build-profile.json` from the template
4. Change the session prompt to load your car's profile

No accounts, no API keys beyond your existing Claude subscription.
