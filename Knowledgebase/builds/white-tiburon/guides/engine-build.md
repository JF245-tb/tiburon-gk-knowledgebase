# Race Engine Build — September Target
## G6BA 2.7L V6 Short Block → Complete Engine

**Target:** Complete and ready to mate to the transmission (Quaife ATB LSD already installed) before the September race.

**Current state (July 2026):** Pistons installed in the block. Everything below is remaining.

> This is a separate engine build, not the one currently running in the car (see `weekend-tasks.md` for the current car's status). Once complete, this engine replaces the current one and all Haltech AVI/CAN wiring needs to be re-verified against its actual sensor locations before first start.

---

## Build Sequence

1. [ ] Oil pump + crank sprocket
2. [ ] Harmonic balancer (crank pulley)
3. [ ] Oil pans (upper + lower)
4. [ ] Cylinder heads (gasket + torque-angle bolts)
5. [ ] Camshafts (per head, into the head)
6. [ ] Valve covers
7. [ ] Timing belt + water pump
8. [ ] Mate to transmission (Quaife LSD already installed) + CV axles, tie rod ends, wheel hubs and bearings

Steps 1–3 and 7 all live in the front-of-engine area (oil pump case, timing covers, water pump all mount to/near the same timing case) — worth dry-fitting the crank sprocket and checking timing-belt routing clearance before final-torquing the oil pump case, since it's much easier to address now than after the timing belt is on.

---

## Gasket & Torque Quick Reference

Sourced from `common/shop-manual/engine-mechanical/` (factory manual, Tier 1). ⚠️ = torque-to-yield/angle method, not a straight torque value — do not reuse these fasteners if the manual says so.

| Step | Component | Gasket / Seal | Torque | Source |
|------|-----------|---------------|--------|--------|
| 1 | Oil pump case | New gasket | 12–15 Nm (9–11 lb·ft) | `lubrication-system.md` |
| 1 | Oil pump cover | — | 8–12 Nm (6–9 lb·ft) | `lubrication-system.md` |
| 1 | Oil pump case front seal | Oil seal (special tool 09214-33000) | Seated, not torqued | `lubrication-system.md` |
| 1 | Oil relief valve plug | — | 40–50 Nm (29–36 lb·ft) | `lubrication-system.md` |
| 1 | Oil screen | **New** gasket | 15–22 Nm (11–15 lb·ft) | `lubrication-system.md` |
| 1 | Crank sprocket (timing belt drive, not the pulley) | — | 20–27 Nm (14–20 lb·ft) | `cooling-system.md` |
| 2 | Crank pulley (harmonic balancer) | — | 180–190 Nm (130–138 lb·ft) | `timing-system.md` |
| 3 | Oil pan flange | **Sealant, not a gasket** — apply to flange groove, install pan within 15 min of application | Upper pan bolts vary by marked bolt type: * 19–28 Nm, ** 5–7 Nm, *** 30–42 Nm (see bolt-position diagram) | `lubrication-system.md` |
| 3 | Lower oil pan bolts | — | 10–12 Nm (7–9 lb·ft) | `lubrication-system.md` |
| 3 | Oil pressure switch | Sealant on threads: Three Bond 1141E or 3M ATD 8660 | 15–22 Nm (11–16 lb·ft) — do not overtorque | `lubrication-system.md` |
| 4 | Cylinder head gasket | **New**, orientation matters — ID mark faces the cylinder head, no sealant on these surfaces | — | `cylinder-head-assembly.md` |
| 4 | Cylinder head bolts | — | ⚠️ 25 Nm + 58–62° + 43–47° (torque-angle method, tightened in sequence) | `cylinder-head-assembly.md` |
| 5 | Camshaft bearing caps | — | M10: 14–16 Nm (10–12 lb·ft); M7: 10–12 Nm (7–9 lb·ft) — tighten in 2–3 increments | `main-moving-system.md` |
| 5 | Camshaft oil seal | Special tool 09221-21000, oil on outer surface | Seated, not torqued | `main-moving-system.md` |
| 5 | Camshaft sprocket | — | 90–110 Nm (65–80 lb·ft) | `main-moving-system.md` / `cooling-system.md` |
| 6 | Valve cover (cylinder head cover) | Gasket (reused unless damaged — manual doesn't mandate new, unlike the head gasket) | 5–6 Nm (3.6–4.4 lb·ft) — tighten to half spec first in sequence 1–8, then full spec | `main-moving-system.md` |
| 7 | Timing belt upper cover | — | 15–22 Nm (11–15 lb·ft) | `timing-system.md` |
| 7 | Timing belt lower cover | — | 10–12 Nm (7–9 lb·ft) | `timing-system.md` |
| 7 | Water pump | **New** gasket | 15–22 Nm | `cooling-system.md` |

---

## Sequencing Notes That Matter

**Cylinder heads (step 4):**
- Clean both gasket surfaces (head + block) before installing the new gasket — **no sealant** on the head gasket surfaces.
- Verify the identification mark on the gasket and install with the marked surface facing the cylinder head.
- Head bolts use the torque-angle method: 25 Nm, then +58–62°, then +43–47° more, in the specified bolt sequence (see `cylinder-head-assembly.md` for the sequence diagram).

**Camshafts (step 5):**
- Each head has an internal chain linking the intake and exhaust camshaft sprockets — align the timing marks on this chain during install, separate from the main crank-to-cam timing belt in step 7.
- Bearing caps are marked I (intake) / E (exhaust) — don't mix them up.
- Camshaft sprocket bolts get final-torqued as part of the timing belt install (step 7), not necessarily right after the camshaft goes in — see the timing belt installation order below.

**Valve covers (step 6):**
- Tighten bolts to half spec first, in sequence, then to full spec — not straight to final torque in one pass.

**Timing belt + water pump (step 7):**
- Install order per the manual: idler pulley → tensioner arm/pulley → camshaft sprockets (align timing marks) → auto tensioner (with set pin compressed) → route belt **crank sprocket → idler pulley → camshaft sprocket (LH) → water pump pulley → camshaft sprocket (RH) → tensioner pulley** → pull tensioner set pin.
- No.1 cylinder must be at TDC compression stroke before belt install, with camshaft sprocket timing marks aligned to the cylinder head cover marks. **Do not rotate a camshaft sprocket more than 3 teeth off-mark** without first rotating the crank counter-clockwise slightly — valve/piston contact risk otherwise.
- After install: rotate crank 2 full turns clockwise, let sit 5 minutes at TDC #1 compression, then verify auto tensioner projected length is 6–8 mm. Re-verify all sprocket timing marks are still aligned.
- Water pump gasket surfaces (pump body + block) must be clean before installing the new gasket.

**Mating to transmission (step 8):**
- Quaife ATB LSD is already installed in the transmission — no work needed there.
- Do CV axles, tie rod ends, wheel hubs and bearings while the engine/trans is out — this is also the window for the front sway bar swap (see `weekend-tasks.md` → Suspension — Open Items). Bundle all engine-out-only suspension/driveline work together.

---

## Related Files

| File | Contents |
|------|----------|
| `common/shop-manual/engine-mechanical/lubrication-system.md` | Oil pump, oil screen, oil pan — full disassembly/reassembly procedure |
| `common/shop-manual/engine-mechanical/timing-system.md` | Timing belt removal/install, tension adjustment |
| `common/shop-manual/engine-mechanical/cylinder-head-assembly.md` | Valve/spring/seal assembly, head gasket, head bolt torque sequence |
| `common/shop-manual/engine-mechanical/main-moving-system.md` | Camshaft install, bearing caps, valve cover |
| `common/shop-manual/engine-mechanical/cooling-system.md` | Water pump removal/install |
| `common/shop-manual/engine-mechanical/specifications.md` | Full spec/torque tables for this chapter |
| `common/shop-manual/engine-mechanical/engine-block.md` | Block, pistons, main bearings (already done for this build) |
| `weekend-tasks.md` | Current car status + suspension backlog, including the engine-out suspension/driveline items that pair with this build |
