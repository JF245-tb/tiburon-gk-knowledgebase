# OpenGK File Repository — Index

**Source:** <https://opengk.org/files/>
**Maintainer:** Chase206 (`chase (at) opengk.org`) — mirror of the OpenGK GitHub repository
**License:** MIT. Contributions solicited via the Facebook groups or email.

> **Their disclaimer, verbatim:** "ALL DATA WITHIN REPOSITORY IS PROVIDED 'AS IS', WITHOUT
> WARRANTY OR GUARANTEE. USE AT YOUR OWN RISK!"

This is the file host behind OpenGK — factory ECU dumps, datasheets, and tooling. It is a
plain directory lister, browsable via `?dir=<path>`. Files are fetched directly:

```
https://opengk.org/files/EEPROMS/Siemens/GK-27/<filename>.bin
```

---

## Tree

```
files/
├── Documentation/
│   └── HMC_V6 MS42/         HMC_V6 MS42.pdf
├── EEPROMS/
│   ├── Bosch/               (empty)
│   ├── Kefico/              LC-16, RD-18, RD-20, X3-15
│   └── Siemens/             12 chassis-engine directories  ← factory dumps live here
├── Tools/
│   ├── Hex Editors/         HxD 2.5.0, wxHexEditor 0.24 (Win32/Win64)
│   ├── TunerProFree/        SetupTunerProFree_v500_10018.exe
│   └── Willem GQ-4x4/       USBPrgSetup7.29.exe + USB drivers (chip-off programmer)
└── Users/
    ├── chase206/            GKFlasher MSI installers, OpenGK logo icon
    └── dante383/            datasheets + three large bin collections
```

---

## EEPROMS/Siemens — the factory dump library

Directories are named `<chassis>-<engine>`; see `chassis-identifiers.md` for the chassis
codes. **These are full raw EEPROM images** and are the only files in the repository
suitable for byte-diffing against a dump of your own ECU.

| Directory | Vehicle | Engine | Files |
|-----------|---------|--------|-------|
| **GK-27** | **Tiburon** | **2.7L V6** | **40** ← our cars |
| **GK-20** | **Tiburon** | **2.0L L4** | **18** |
| EF-27 | Sonata (1998–2004) | 2.7L V6 | 19 |
| EF-25 | Sonata (1998–2004) | 2.5L V6 | 1 |
| SM-27 | Santa Fe (2000–2006) | 2.7L V6 | 8 |
| JM-20 / JM-27 | Tucson | 2.0L / 2.7L | 8 / 3 |
| KM-20 / KM-27 | KIA Sportage | 2.0L / 2.7L | 3 / 5 |
| XD-20 | Elantra (2000–2005) | 2.0L | 3 |
| BK-20 | Genesis Coupe | 2.0L | 1 |
| LD-20 | KIA Spectra / Cerato | 2.0L | 1 |

`EEPROMS/Kefico` holds one dump each for LC-16 (Accent), RD-18 (Scoupe) and X3-15
(Accent 1995–2000). `EEPROMS/Bosch` exists but is empty.

**Filename convention** (decoded in `ecu-factory-verification.md`):

```
ca652051_G3N7TS0H_6577715116_5WY1502B_G8_0524661407-HMC021147190609316577657601H.bin
└─description─┘ └calibration┘ └part no.┘ └hardware┘                └── ECU ID ──┘
```

Every field is a real byte sequence in the dump, so a dump of your own ECU names the
reference file you need. Match on the first two fields.

---

## Users/dante383 — datasheets and bulk bin collections

### Datasheets (directly useful)

| File | Why it matters |
|------|----------------|
| `OBDII Specifications - KWP2000 DaimlerChrysler 2002.pdf` | **The KWP2000 reference `k-line.md` recommends.** This is where to get it. |
| `PCF7991AT_datasheet.pdf` | Transponder base-station IC used by SMARTRA — see `smartra.md` |
| `gk_cluster_faces_front_and_back.pdf` | GK instrument cluster faces — relevant to `builds/white-tiburon/cluster-integration.md` |

### `GDS_bins_US/` — 840 files

US-market calibrations pulled from Hyundai GDS. Named by calibration ID (`6549TS0P.BIN`,
`342GAK2Q.BIN`).

> **These are NOT raw EEPROM dumps.** Verified: `6549TS0P.BIN` is **256,880 bytes**, not the
> 262,144 of a real 2mbit image, and it carries none of the `5WY…` / `HMC…` strings a raw
> dump has. They are GDS reflash payloads with a metadata trailer — the trailer for that file
> reads `S3N7TS0P` / `ca654012` / `ca654012.DAT`.
>
> **Do not feed these to `scripts/verify-ecu-stock.py` as a reference** — the diff is
> meaningless. Use them as a *catalog* of which calibrations shipped on US cars, and take
> diff references from `EEPROMS/Siemens/` instead.

### `J2534_bins/` — 1,517 bins + 1,517 `_metadata.txt`

Hyundai/Kia J2534 reflash files spanning the whole KDM range, each paired with a decoded
metadata sidecar. The metadata format is documented by dante383 and parses as:

| Field | Example |
|-------|---------|
| Manufacturer / Platform / Model year | `HME` / `RB12` / `2014` |
| Engine | `G 1.6 MPI` |
| Affected unit | `ENGINE` |
| ROM ID / Filename | `020113` / `HGU40002.BIN` |
| File size | `393840` (384 KB) |
| Checksum (per Hyundai) | `0x03C5` — *"doesn't appear anywhere in the file"* |
| Release reference | `HFE14-92-E050-RB` |
| Connector | `OBD-II 16PIN CONNECTOR` |
| Program zone size / offset | `0x060270` / `0x005008` |
| Calibration zone size / offset | (often blank) |

Useful for cross-referencing zone offsets on unfamiliar ECUs.

### `scrapped_bins/` — forum-sourced, unvetted

Two subdirectories (`forum_1`, `forum_2`) of bins scraped from tuning forums.

> **Their warning, verbatim:** "These files have been not vetted. They might damage your ECU,
> engine or cause unpredictable behavior. Use strictly for research!"

The value here is the **`README.md` summary**, not the bins. It tabulates, per hardware
revision, which calibrations were observed, the socket labels, and production date ranges —
a real-world distribution of what shipped on what. Sample:

```
5WY1252:
    Calibrations: ca652051 (1 - 100.00%)
    Production dates: min 10.2000 max 10.2000
```

It covers 2.7L revisions including 5WY1503/1514/1572, 5WY1709/1733/1736/1747, the 5WY18xx
series and 5WY1F11/1F20/1F45/1F66. Useful as a sanity check when an ECU label and its
calibration ID seem mismatched.

---

## Users/chase206 — GKFlasher installers

| File | Note |
|------|------|
| `GKFlasher_v1.0.4.msi` | Older MSI, kept here |
| `archive/GKFlasher_v1.0.0–1.0.3.msi` | Superseded |
| `Siemens_T_Logo.ico` | OpenGK/GKFlasher icon, for the desktop shortcut |

**Current MSI packages come from GitHub releases, not here** —
<https://github.com/Dante383/GKFlasher/releases> (latest is far newer than v1.0.4; see
`gkflasher.md`).

---

## Tools

| Directory | Contents | Use |
|-----------|----------|-----|
| `Hex Editors/` | HxD 2.5.0 (installer + portable), wxHexEditor 0.24 Win32/Win64 | Inspecting dumps by hand |
| `TunerProFree/` | TunerPro Free v5.00.10018 | Map editing with XDF definitions — see `map-definitions.md` |
| `Willem GQ-4x4/` | USBPrgSetup 7.29 + 32/64-bit USB drivers | Chip-off EEPROM programmer, for reviving an ECU that will not talk over K-Line |

`Documentation/HMC_V6 MS42/HMC_V6 MS42.pdf` covers the MS42 ECU on HMC V6 applications.

---

## Related

- Verifying a dump against these references — `ecu-factory-verification.md`
- Reading and writing with GKFlasher — `gkflasher.md`
- Decoding ECU labels — `ecm-identification.md`
- Chassis code lookup — `chassis-identifiers.md`
