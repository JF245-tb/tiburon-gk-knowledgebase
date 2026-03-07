# Fasteners Database
**Purpose:** Reference library for all fasteners used in the 2003 Hyundai Tiburon GK (G6BA V6). Bolts are photographed, measured, and indexed to support bin organization, torque reference, and eventual OEM part number matching.

---

## Quick Start

- **Primary query file:** `bolt-index.json` — search by bolt_id, location, system, or tags
- **Add a new bolt:** Copy `_templates/record-template.json` → `bolts/{bolt_id}/record.json`, fill in fields, add 4 photos
- **Bin reference:** `bin-labels.md` — printable table for physical bin labels

---

## bolt_id Naming Format

```
M{diameter}x{pitch}-{uhl}-{head_type}-{location-slug}
```

| Field | Example | Notes |
|-------|---------|-------|
| diameter | `M8` | Metric thread diameter in mm |
| pitch | `x1.25` | Thread pitch in mm |
| uhl | `25` | Under-head length in mm |
| head_type | `hex` | See controlled vocabulary below |
| location-slug | `cam-cap` | Short kebab-case location descriptor |

**Full example:** `M8x1.25-25-hex-cam-cap`

For bolts shared across many locations, use a generic slug: `M10x1.25-30-hex-generic`

---

## Controlled Vocabularies

### `system`
```
engine, transmission, suspension, brakes, steering, electrical,
body, interior, exhaust, fuel, cooling, hardware-generic
```

### `head_type`
```
hex, socket-cap, button-cap, torx, phillips, jis, flange-hex,
flange-socket, carriage, stud, nut-hex, nut-flange, washer
```

### `drive`
```
hex-external, hex-internal (allen), torx, phillips, jis,
pozi, slotted, none (studs/nuts without drive feature)
```

### `material`
```
steel, stainless, aluminum, titanium, nylon
```

### `grade`
```
4.8, 8.8, 10.9, 12.9, A2-70, A4-70, A4-80, OEM-unknown
```

### `finish`
```
zinc, black-oxide, cadmium, plain, stainless-natural,
anodized, oem-phosphate
```

### `cars` (which cars this bolt appears in)
```
white, blue, both
```

### `torque.method`
```
torque-wrench, torque-angle, hand-tight, thread-lock-only, oem-spec
```

---

## Photo Standards

Each bolt folder should contain exactly 4 photos:

| Filename | Subject | Notes |
|----------|---------|-------|
| `spec.jpg` | Bolt next to ruler/calipers | Measure diameter, UHL, head height clearly visible |
| `head.jpg` | Top-down view of head | Show drive type and any markings/grade stamps |
| `side.jpg` | Side profile | Full bolt visible, threaded portion clear |
| `location.jpg` | Bolt in car | Show where it came from; include surrounding context |

- Shoot on a white or gray background for spec/head/side
- Good lighting; avoid shadows across threads
- 1–3 MP minimum; phone camera is fine
- Name exactly as shown — no spaces, lowercase

---

## Workflow

1. Remove bolt from car → measure with calipers (diameter, pitch, UHL)
2. Identify head type and drive
3. Look up or derive `bolt_id`
4. Check `bolt-index.json` — does this bolt_id already exist?
   - **Yes:** Verify fields match; update `qty_per_car` or `location` if different application
   - **No:** Create `bolts/{bolt_id}/` directory, copy template, fill in fields
5. Take 4 photos, save to `bolts/{bolt_id}/`
6. Add entry to `bolt-index.json` (copy the JSON object structure from template)
7. Print updated `bin-labels.md` and label the physical bin

---

## Related Files

| File | Contents |
|------|----------|
| `bolt-index.json` | Primary query file — all bolt records in one JSON object |
| `_templates/record-template.json` | Blank template for new bolt records |
| `bin-labels.md` | Printable bin label reference |
| `bolts/{bolt_id}/record.json` | Full record for individual bolt |
| `bolts/{bolt_id}/*.jpg` | Photos (spec, head, side, location) |
