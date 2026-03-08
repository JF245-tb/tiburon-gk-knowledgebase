# Haltech REM Upgrade Harness
**Source:** `Haltech/REM Harness Diagram.pdf` — HT-142001, Rev A, 14 June 2016
**Device:** Race Expansion Module (REM) — adds 8 injector channels, 10 AVI, 6 DPI, 8 DPO

> **White Tiburon note:** The REM is not installed on the white Tiburon. This file is reference only.
> The Elite 2500 base harness handles all 6 injectors directly. Only consult this if adding REM capability later.

---

## Integration Connections (Main ECU → REM)

These wires connect from the Elite 2500 base harness to the REM harness:

| Wire Color | Connection Name | Function | ECU Location |
|-----------|----------------|----------|--------------|
| RED/BLU | Injection Power ECU Flyback | ECU flyback | ECU 34-pin A26 |
| GRY/BLU | REM DPI 5 | ECU Stage 2 RX | ECU 34-pin A1 |
| GRY/GRN | REM DPI 6 | ECU Stage 3 RX | ECU 34-pin A23 |
| YEL/BLK | Watchdog | Watchdog | ECU 34-pin A3 (B7 in table) |
| VIO/ORG | E2500 INJ Enable (DPO 4) | INJ enable | ECU 26-pin B19 |

## REM Connector Groups

| Connector | Label | Contents |
|-----------|-------|----------|
| J7 | Main ECU Connection | Integration wires to Elite 2500 (see table above) |
| J8 | REM AVI | 10 analog voltage inputs (REM AVI 1–10) |
| J9 | REM DPI | 6 digital pulsed inputs (REM DPI 1–6) |
| J10 | REM DPO | 8 digital pulsed outputs (REM DPO 1–8) |
| J11 | REM Injectors | 8 injector outputs (REM INJ 1–8) |
| J12 | ECU Injectors 12V Supply | Injection power from main ECU harness |
| J13 | Battery + | +13.8V battery input |
| J14 | Battery − | Battery ground |
| J5 | Solid State Relay | Integrated SSR PCB (HT-030202) |
| J6 | SSR Control | Conditioned enable from ECU DPO 4 |
| J3/J4 | CAN (M/F) | CAN daisy-chain: +12V, GND, CAN H, CAN L |

## REM AVI Wire Colors

| Signal | Wire Color |
|--------|-----------|
| REM AVI 1 | GRY/YEL (shd) |
| REM AVI 2 | ORG/BLK |
| REM AVI 3 | ORG/RED |
| REM AVI 4 | ORG/YEL |
| REM AVI 5 | ORG/GRN |
| REM AVI 6 | GRY/ORG (shd) |
| REM AVI 7 | GRY |
| REM AVI 8 | VIO |
| REM AVI 9 | YEL |
| REM AVI 10 | WHT |
| +5V supply | ORG (×5) |
| Signal ground | BLK/WHT (×6) |

## REM DPO Wire Colors

| Signal | Wire Color |
|--------|-----------|
| REM DPO 1 | VIO/BLK |
| REM DPO 2 | VIO/BRN |
| REM DPO 3 | VIO/RED |
| REM DPO 4 | VIO/ORG |
| REM DPO 5 | GRN |
| REM DPO 6 | GRN/BLK |
| REM DPO 7 | GRN/BRN |
| REM DPO 8 | GRN/RED |

## Source PDF
For the full schematic diagram showing all connector-to-connector wire routing, see:
`Haltech/REM Harness Diagram.pdf`
