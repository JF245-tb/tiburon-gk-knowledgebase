# 2003 Hyundai Tiburon GK — Platform Specifications
**Applies to:** Both blue and white race cars (2003 GK chassis, 2.7L V6 / G6BA)

**Confidence:** ⚠️ Dimensions, weights, and engine specs sourced from published Hyundai specs and community knowledge — cross-verify against factory manual for torque specs before use in build decisions. Gear ratios need verification against actual Aisin documentation.

---

## Chassis Dimensions

| Spec | Value |
|------|-------|
| Wheelbase | 2,570 mm (101.2 in) |
| Overall Length | 4,345 mm (171.1 in) |
| Overall Width | 1,795 mm (70.7 in) |
| Overall Height | 1,325 mm (52.2 in) |
| Front Track Width | 1,530 mm (60.2 in) |
| Rear Track Width | 1,530 mm (60.2 in) |
| Curb Weight (V6 6-speed) | ~1,370 kg (~3,020 lb) approx |
| Weight Distribution | ~62/38 front/rear (FWD) |
| Fuel Tank Capacity | 60 L (15.9 US gal) |
| Turning Radius | ~5.2 m (17.1 ft) curb-to-curb |

---

## Suspension

| Spec | Value |
|------|-------|
| Front | MacPherson strut |
| Rear | Multi-link |
| Front Brake | 280 mm vented rotor |
| Rear Brake | 262 mm solid rotor |
| Steering | Rack and pinion, hydraulic assist |

---

## Wheels & Tires

| Spec | Value |
|------|-------|
| Lug Pattern | **4×114.3** (4×4.5") |
| Hub Bore | **67.1 mm** |
| OEM Wheel (V6 GT trim) | 17×7" |
| OEM Tire | 215/45R17 |
| Lug Torque | 65–80 ft-lb (88–108 Nm) |

**Race car notes:**
- Blue car: 3 sets OEM 17×7 wheels, 215/45/17, 25mm spacers (testing bearing wear)
- White car: Enkei RPF01 17×7, no spacers

---

## G6BA Engine (2.7L V6 Delta, DOHC)

| Spec | Value |
|------|-------|
| Displacement | 2,656 cc |
| Configuration | 60° V6, DOHC, 24-valve |
| Bore × Stroke | 86.7 mm × 75.0 mm |
| Compression Ratio | 10.0:1 |
| Rated Power | 181 hp @ 6,000 rpm |
| Rated Torque | 177 lb-ft @ 4,000 rpm |
| Valvetrain | Hydraulic lifters, no VVT (base G6BA) |
| Timing | **Timing belt** (interference engine — failure = bent valves) |
| Timing Belt Service | 60,000 mi / every race rebuild — belt + idler + tensioner + water pump |
| Ignition | Wasted spark — 3 coils, each fires 2 cylinders (stock) |
| Fuel system | Sequential MPFI |
| Oil capacity | 4.5 L w/o filter / 5.0 L with filter (5W-30 full synthetic) |
| Knock sensor | Yes, single sensor on block |
| O2 sensors | 4× (pre/post cat, both banks) |
| Spark plugs | NGK BKR6E or equivalent, gap 1.0–1.1 mm |

**⚠️ IGNITION NOTE:** Stock G6BA uses **wasted spark** (3 coils for 6 cylinders). Coil-on-plug (COP) is an **upgrade** being considered for the white car — NOT stock. The white car currently has wasted spark.

### Critical Racing Notes — G6BA

- **Interference engine** — timing belt failure bends valves. Inspect belt every oil change in race use; replace belt, idler, tensioner, and water pump as a set.
- **Oil consumption** — known tendency under sustained high RPM/load. Check oil level before every session.
- **Cooling** — no factory oil cooler. Remote oil cooler highly recommended for endurance racing.
- **ECM type** — SIMK43 (MAF-based on most GK variants, MAP-based on some). Blue car uses SIMK43, tunable via GKFlasher. White car uses Haltech Elite 2500 standalone.

---

## Aisin 6-Speed Manual Transaxle

**Both cars** have the 6-speed Aisin manual transmission (stock).
**Model:** Aisin AY6 (also referenced as M6CF1 in some Hyundai documentation)

| Spec | Value |
|------|-------|
| Type | 6-speed manual transaxle (FWD) |
| Manufacturer | Aisin AI (Japan) |
| 1st gear ratio | 3.538 ⚠️ |
| 2nd gear ratio | 2.045 ⚠️ |
| 3rd gear ratio | 1.393 ⚠️ |
| 4th gear ratio | 1.027 ⚠️ |
| 5th gear ratio | 0.825 ⚠️ |
| 6th gear ratio | 0.666 ⚠️ |
| Reverse | 3.583 ⚠️ |
| Final drive ratio | 4.050:1 ⚠️ |
| Fluid type | API GL-4, 75W-85 or 75W-90 |
| Fluid capacity | ~2.2 L (2.3 qt) |
| Clutch disc OD | ~240 mm |

**⚠️ Gear ratios are from community/training data — verify against factory service manual before using for speedometer calibration or gear indicator programming.**

### Transaxle Racing Notes
- Stock synchros generally durable for Lemons-type racing
- 3rd gear synchro is common failure under aggressive shifting; double-clutch downshifts help
- Fluid upgrade recommended: Redline MT-90 or Amsoil Synchromesh
- No factory LSD in most V6 GK trim levels
- CV joints (especially inner) are a wear point under racing loads — inspect boots regularly

**Modifications:**
- Blue car: Phantom Grip block-style LSD installed
- White car: Currently stock, eventually getting Quaife LSD (see engine-builds.md)

---

## Suspension Alignment Reference

| Spec | Stock (approx) | Racing Target |
|------|---------------|---------------|
| Front camber | 0° | −2.0° to −3.0° |
| Front toe | 0 / slight toe-in | 0 to +1/16" total (toe-in) |
| Front caster | ~3.5° | Maximize (camber plates) |
| Rear camber | ~−0.5° | −1.5° to −2.0° |
| Rear toe | slight toe-in | ~1/8" total toe-in |

OEM front strut spring rate approximately 18–22 N/mm.

---

## Fastener Reference

| Application | Spec | Part # | Notes |
|-------------|------|--------|-------|
| Strut-to-knuckle bolts (blue car) | M14×1.5×70mm, Class 10.9 | Belmetric BFD14X1.5X70YLW | DIN 6921 hex flange, yellow zinc |
| Strut-to-knuckle washers (blue car) | M14, 23mm OD | Belmetric WNORD14 | Nord-Lock wedge dual-lock, zinc flake |
| Wheel lugs | — | — | 65–80 ft-lb / 88–108 Nm |

---

## OEM Part Numbers — Key Sensors

| Component | OEM Part | Aftermarket Equivalent | Notes |
|-----------|----------|----------------------|-------|
| CKP sensor | Hyundai 39180-37150 | NTK EH0220 | Hall effect |
| CMP sensor | Hyundai 39350-37100 | NTK EC0145 | Hall effect |
| Stock fuel injectors (blue) | Kefico 9260930004 | — | 194cc @ 45 psi, 14.2Ω |

---

## Instrument Cluster (OEM — both cars)

| Gauge | Type | Input | Resistance / Signal |
|-------|------|-------|---------------------|
| Tachometer | Cross-coil | Frequency from ECM | 3 pulses/rev |
| Speedometer | Cross-coil (Hall IC drive) | VSS (C109) | 4 pulses/rev, 637 rpm = 60 km/h |
| Fuel level | Cross-coil | Fuel sender M55 (6–97 Ω) | 6Ω = full, 97Ω = empty |
| Coolant temp | Cross-coil | CTS sender C111 (NTC) | 143.4Ω@60°C → 17.5Ω@125°C |

---

## Key Connectors (OEM)

| Connector ID | Component | Location |
|-------------|-----------|----------|
| C109 | VSS (Vehicle Speed Sensor) | Transaxle |
| C111 | CTS (Coolant Temp Sensor/Sender) | Engine coolant manifold |
| C133-3 | ECM connector 3 | ECM |
| C133-4 | ECM connector 4 | ECM — pin 17 = tach signal, pin 39 = VSS in |
| M10-1/2/3 | Instrument cluster | Instrument cluster |
| M42 | Multi-gauge unit | Instrument cluster |
| M55 | Fuel sender | Fuel tank |

---

## Related Files

| File | Contents |
|------|----------|
| `cars/blue-tiburon.md` | Blue car build profile |
| `cars/white-tiburon.md` | White car build profile |
| `cars/oem-cluster-integration.md` | OEM cluster wiring plan for Haltech |
| `opengk/ecm-pinouts.md` | Siemens SIMK43 ECU connector pinouts |
| `opengk/sensor-information.md` | Recommended sensor part numbers |
| `shop-manual/engine-mechanical.md` | G6BA engine specs (extracted factory text) |
| `signal-routing.md` | End-to-end signal routing for white car |
