# Body Control Module (BCM) — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=Body_Control_Module
**Vehicle:** 2003 Hyundai Tiburon GK

---

## FCC Reports

- GK Keyfob FCC report: https://fcc.report/FCC-ID/LXP-RKE225
- FL2 Keyfob FCC report: https://fcc.report/FCC-ID/LXP-RK225

## PCB Layouts

See: https://opengk.org/index.php?title=BCM_PCB_Layouts

## Microcontroller

8-bit Motorola CPU: **MC68HC908AZ60** running at 8 MHz
64 KiB FLASH EEPROM (Motorola MC68HC908A microcontroller)
Part file: `311-21300-0-MC908AZ32ACFU.pdf`

## Part Numbers Referenced

- **95410-2C160** — BCM variant (EU, 2.0L engine, demonstrated in PCB layout)
- BCM FCC report: https://fccid.io/LXP-VIM233

---

## BCM Connector Pinouts

The BCM has multiple connectors labeled BCM-AI, BCM-CE, BCM-DE, BCM-EF, BCM-FF, BCM-GF, BCM-HM, BCM-IM, BCM-JM, BCM-KM, BCM-LM, BCM-MR.

### BCM-AI — AMP 929504-4
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | — | — | |
| 2 | — | — | |
| 3 | — | — | |
| 4 | | ESPS (IG1) | |
| 5 | | RH seat belt buckle | |
| 6 | | LH seat belt buckle | |
| 7 | Input | Crash signal | |
| 8 | — | — | |
| 9 | Input | Airbag diagnosis (from ESPS) | |
| 10 | Output | Airbag warning light | |

### BCM-CE
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Output | Head lamp low relay (S2) | |
| 2 | | DRL unit NO 12 | |
| 3 | Output | Front wiper relay control | |
| 4 | Output | Front fog lamp relay (S1) | |
| 5 | | Turn signal lamp (FR) | |
| 6 | | Tail auto cut to DRL | |
| 7 | | DRL unit (11) | |
| 8 | Output | Front wiper relay (IG2) | |
| 9 | Output | Turn signal lamp (FL) | |
| 10 | Output | Position lamp (RH) | |
| 11 | Output | Position lamp (LH) | |
| 12 | Output | ABS module (IG1) | |
| 13 | Output | Alternator charge line / dash indicator | |
| 14 | Output | Fuse & relay box (IG2) (Ignition fuse) | |
| 15 | Output | Wiper park output | |
| 16 | Output | Washer motor | |
| 17 | — | — | |
| 18 | — | — | |

### BCM-DE
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Input | Battery | |

### BCM-EF — TE 175965-2
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Input | Assist door key switch | |
| 2 | Input | Tail gate lock switch | |
| 3 | Input | Assist door lock switch | |
| 4 | Input | Assist door switch | |
| 5 | Input | Folding switch | |
| 6 | Input | Tail gate open switch | |
| 7 | Input | Driver door key unlock switch | |
| 8 | Input | Driver door lock switch | |
| 9 | Input | Driver door switch | |
| 10 | Input | Seat belt switch | |
| 11 | — | — | |
| 12 | — | — | |

### BCM-FF
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Output | Rear fog lamp relay | |
| 2 | Output | Back up lamp | |
| 3 | — | — | |
| 4 | Output | Outside mirror | |
| 5 | Output | Tail lamp (RH) | |
| 6 | Output | Door lock relay | |
| 7 | — | — | |
| 8 | Output | Door unlock relay | |
| 9 | — | — | |
| 10 | Output | Tail lamp (LH) fuse | |
| 11 | Input | Door switch | |
| 12 | Output | Mirror unfolding/door unlock relay | |
| 13 | | Turn signal (RL) | |
| 14 | — | — | |
| 15 | Output | Luggage lamp | |
| 16 | — | — | |
| 17 | | Turn signal (RR) | |
| 18 | Output | Amplifier | |
| 19 | Output | Outside mirror heater | |
| 20 | | Mirror folding | |
| 21 | Output | Rear wiper motor (IG2) | |
| 22 | Input | Tail gate open switch | |

### BCM-GF
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Output | Rear window defogger | |
| 2 | Output | Power window relay | |

### BCM-HM
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | IO | Immobilizer antenna 1 | |
| 2 | Output | 2 stage unlock ground | |
| 3 | Input | Turn signal switch (RH) | |
| 4 | Input | Door warning switch | |
| 5 | Input | Tail lamp switch | |
| 6 | Input | Rear fog lamp switch | |
| 7 | Input | Code saver | |
| 8 | — | — | |
| 9 | Input | Hood switch | |
| 10 | — | — | |
| 11 | IO | Immobilizer antenna 2 | |
| 12 | Output | Export ground | |
| 13 | Input | Turn signal lamp switch | |
| 14 | Input | Auto light switch input | |
| 15 | — | — | |
| 16 | Input | Head lamp switch | |
| 17 | Input | Front fog lamp switch | |
| 18 | Input | Hazard lamp switch | |
| 19 | Input | Rear defogger switch | |
| 20 | Output | Rear fog lamp indicator | |

### BCM-IM
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Input | Air conditioner switch | |
| 2 | Output | Cluster battery charge | |
| 3 | — | — | |
| 4 | | ESP switch (IG1) | |
| 5 | Output | Cluster (IG1) | |
| 6 | Output | Cluster (IG2) | |
| 7 | Output | Cluster (turn signal LH out) | |
| 8 | | ECU (IG1) | |
| 9 | Output | Cluster (turn signal RH out) | |
| 10 | | RR HTD switch | |
| 11 | Output | Cluster (airbag indicator) | |
| 12 | | Diagnostic tool (B+) | |
| 13 | Output | Digital clock (ACC) | |
| 14 | Output | Immobilizer indicator | |
| 15 | | External tail lamp (RH) | |
| 16 | | Diagnostic tool (Airbag) | |
| 17 | | Air conditioner (IG2) | |
| 18 | | Auto light ground | |
| 19 | | Diagnosis & code saving | |
| 20 | | Immobilizer | |

### BCM-JM ← IMPORTANT for Race Car
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | | Multifunction switch - intermittent wiper ground | |
| 2 | | Siren control | |
| 3 | Output | Key hole illumination | |
| **4** | **Input** | **Speed sensor** | **VSS signal comes here — BCM uses for over-speed warning, wiper speed sensitivity, auto-lock** |
| 5 | Output | Interior illumination | |
| 6 | Output | Cluster (Airbag warning indicator) | |
| 7 | | DCT | |
| 8 | Output | Door open indicator | |
| 9 | | Multifunction INT | |
| 10 | | Multifunction INT (T) | |
| 11 | | Auto light signal | |
| 12 | Output | Seat belt indicator | |
| 13 | Output | Over speed ground | |
| 14 | — | — | |
| 15 | | Auto light supply | |
| 16 | Output | Tail gate open indicator | |

### BCM-KM
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Output | Cigar lighter | |
| 2 | | Wiper low | |
| 3 | | Wiper high | |
| 4 | | Back up switch (reverse gear) | |
| 5 | | ACC | |
| 6 | Input | Washer switch | |
| 7 | Input | Back up lamp switch | |
| 8 | | Start inhibit relay | |
| 9 | Input | Seat heater switch (IG2) | |
| 10 | | Joint main 3 (B+) | |
| 11 | Input | Stop switch (B+) | |
| 12 | | Ignition coil | |
| 13 | — | — | |
| 14 | | Wiper parking | |

### BCM-LM
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | Ground | Ground 1 | |
| 2 | — | — | |
| 3 | Output | Blower motor | |
| 4 | | Ignition switch (IG1) | |
| 5 | Ground | Ground 2 | |
| 6 | | Wiper switch power | |
| 7 | | Ignition switch (ACC) | |
| 8 | | Ignition switch (IG2) | |

### BCM-MR — TE 929504-5
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | | Sunroof (IG2) | |
| 2 | | Roof lamp (B+) | |
| 3 | | Roof lamp decay control | |
| 4 | | ECU | |
| 5 | — | — | |
| 6 | | Sunroof & room lamp ground | |
| 7 | | ECM mirror | |
| 8 | | Sunroof (B+) | |

---

## Race Car Notes

**BCM-JM pin 4 = Speed Sensor input** — The VSS signal from the transaxle (C109) routes to the BCM for:
- Over-speed warning
- Intermittent wiper speed sensitivity
- Auto-lock at speed

In the white car (Haltech/PDM), VSS signal must still reach BCM-JM pin 4 if over-speed warning or wiper functions are retained. If BCM is removed/bypassed, this becomes irrelevant.

**V6 Immobilizer:** BCM-based (BCM asks ECM for start permission). BCM-HM pins 1 and 11 are the immobilizer antenna connections. Blue car uses a start button — may need BCM bypass for immobilizer.
