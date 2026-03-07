# CAN Bus Message Definitions
**Source:** https://opengk.org/index.php?title=CAN_Bus_messages

---

## DME1 (0x316) — 10ms refresh

| Byte | Signal | Formula | Description |
|------|--------|---------|-------------|
| 0 | Bitfield | — | Terminal status, error flags, TCS ack, fuel cut, torque intervention, AC relay |
| 1 | TQI_TQR_CAN | hex × 0.39 | Indexed engine torque (% of C_TQ_STND) |
| 2-3 | N_ENG | (MSB×256 + LSB) × 0.15625 | **Engine speed (RPM)** |
| 4 | TQI_CAN | hex × 0.39 | Indicated engine torque (%) |
| 5 | TQ_LOSS_CAN | hex × 0.39 | Engine torque loss (%) |
| 6 | VS | direct | **Vehicle speed (km/h)** |
| 7 | TQI_MAF_CAN | hex × 0.39 | Theoretical engine torque (%) |

## DME2 (0x329) — 10ms refresh

| Byte | Signal | Formula | Description |
|------|--------|---------|-------------|
| 0 | Bitfield | — | CAN version, TCU config, OBD freeze frame, torque scaling |
| 1 | TCO | hex × 0.75 − 48 | **Coolant temperature (°C)** |
| 2 | AMP_CAN | hex × 2 + 598 | **Ambient pressure (hPa)** |
| 3 | VB_OFF_ACT_CAN | 0x10 = connected | Battery disconnection detection |
| 4 | ACK_ES_CAN | — | Engine stopped acknowledgment |
| 5 | TPS_CAN | hex × 0.390625 | **Accelerator pedal position (%)** |
| 6 | ENG_CHR_CAN | 0xFF = gasoline | Engine characteristic/fuel type |

## DME4 (0x545) — 10ms refresh

| Byte | Signal | Formula | Description |
|------|--------|---------|-------------|
| 0 | Bitfield | — | Immobilizer auth, MIL lamp, immobilizer status |
| 1-2 | FCO_SUM_DIF | hex × 0.128 | **Fuel consumption (μl)** |
| 3 | VB | hex × 0.1 | **Battery voltage (V)** |

## DME5 (0x2A0) — 10ms refresh

| Byte | Signal | Formula | Description |
|------|--------|---------|-------------|
| 0 | Bitfield | — | Driver override, ACC failures, brake switch |
| 1 | TIA_CAN | hex × 0.75 | **Intake air temp (°C)** |
| 2 | Bitfield | — | Rate-based monitoring status |
| 3-4 | CTR_IG_CYC_OBD | LSB/MSB | Ignition cycle counter |
| 5-6 | CTR_CDN_OBD | LSB/MSB | General denominator |

**Note:** DME5 values are not fully verified on actual Tiburon CAN dumps.

---

## Messages SIMK43 READS (from other modules)

### ASC1 (0x153) — Traction Control Module → ECU — 10ms refresh

| Byte | Signal | Description |
|------|--------|-------------|
| 0 | Bitfield | Bit0: TCS_REQ_CAN (request TCS); Bit1: MSR_C_REQ_CAN (MSR functions); Bit2: TCS_PAS (TCS disabled by user); Bit3: TCS_GSC (gear shift char); Bit6: ABS_DIAG (diagnostic mode); Bit7: ABS_DEF (ABS defective) |
| 1 | Bitfield | Bit0: TCS_DEF; Bit1: TCS_CTL; Bit2: ABS_ACT; Bit3: EBD_DEF; Bit4: ESP_PAS; Bit5: ESP_DEF; Bit6: ESP_CTL; Bit7: TCS_MFRN |
| 2 | — | Unused |
| 3 | MD_IND_ASC | Torque intervention: `hex × 0.390625` → 0x00=0% (max reduction), 0xFF=99.6% (no reduction) |
| 4 | TQI_MSR_CAN | Reserved for MSR |
| 5 | TQI_SLW_TCS_CAN | Slow torque intervention for TCS (referred to indicated engine torque) |
| 6–7 | — | Unused |

**Example:** `00 80 48 FF 00 FF 00 00`

### ASC2 (0x1F0) — Traction Control Module → ECU — 20ms refresh

Individual wheel speeds from ABS/TCS module.

| Byte | Signal | Formula | Description |
|------|--------|---------|-------------|
| 0 | Wheel 1 speed | `hex × 0.95439` | Wheel speed (km/h) |
| 1 | Wheel 2 speed | `hex × 0.95439` | Wheel speed (km/h) |
| 2 | Wheel 3 speed | `hex × 0.95439` | Wheel speed (km/h) |
| 3 | Wheel 4 speed | `hex × 0.95439` | Wheel speed (km/h) |
| 4–7 | — | — | Unused |

**Example:** `0C 0F 0B 0E 00 00 00 00` → ~11.2 / 14.2 / 10.4 / 13.3 km/h

**Note:** ASC1/ASC2 bits labeled "not used for EMS" on Tiburon (no TCS on GK base model). ECU reads them but most flags are for TCS-equipped variants.

### EGS1 (0x43F) — Transmission Control Module → ECU

Referenced in factory documentation but not fully documented on OpenGK wiki. Used on automatic transmission variants only (not applicable to 6-speed Aisin manual cars).
