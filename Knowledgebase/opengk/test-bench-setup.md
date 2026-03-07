# Creating a Test Bench Setup — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=Creating_a_test_bench_setup
**Note:** Draft page — some info unverified

---

## Purpose

Build an ECU test bench that simulates the full car environment — for parts swapping, immobilizer testing, and research. Covers connector part numbers and pinouts for bench use.

---

## Ignition Switch

### Harness-Side Connector
- **Connector:** KUM PH772-06015 (female/harness side)
- **Terminals:** Faston 6.3mm

### Pinout (female side, looking from front)
```
#3. Ignition output       #2. +12V input      #1. Starter output
#6. Ignition output       #5. +12V input      #4. Accessory output
```

**Notes:**
- Pins 3 and 6 power different BCM fuses but are functionally the same (swapping does no harm)
- Pin 1 → Starter
- Pin 2 → Immobilizer antenna (coupled with ignition illumination)
- Pin 3 → Ignition switch

---

## Key Sensor / Immobilizer Antenna / Key Illumination

### Harness-Side Connector
- **Connector:** KET MG651044 / Yazaki 7283-1060 (female/harness side)
- **Terminals:** Unknown

### Pinout (female side, looking from front)
```
#2. Immobilizer antenna → BCM-HM pin 1
#1. Immobilizer antenna → BCM-HM pin 11
#6. Ground
#5. Key sensor           → BCM-HM pin 4
#4. Key sensor           → BCM-JM pin 3
#3. +12V illumination    → BCM-KM pin 10
```

---

## Notes for Blue Tiburon Bench Work

- BCM-HM pins 1 and 11 are the immobilizer antenna connections (confirmed in body-control-module.md)
- To bench test immobilizer: connect ignition switch, key sensor connector, and BCM power/grounds
- GKFlasher can communicate with ECU via K-Line without full car harness (just power, ground, K-Line)
- For SMARTRA bypass: use GKFlasher routine 0x26 (neutralize SMARTRA) after providing DPN via 0x1A
