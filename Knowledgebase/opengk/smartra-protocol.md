# SMARTRA Protocol — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=SMARTRA_Protocol
**Note:** This page is a stub. Full SMARTRA3 protocol spec (backwards compatible): FCC ID LXP-VIMA01
**Physical layer:** See `w-line.md`

---

## Overview

- SMARTRA never initiates communication — it only responds to ECU commands
- Each ECU command requires exactly one SMARTRA response
- Only one command at a time (wait for reply before sending next)

---

## Packet Structure

### ECU → SMARTRA (command)
```
[Address=0x49] [Length] [Command/Action] [Data...] [Checksum]
```

### SMARTRA → ECU (response)
```
[Address=0x69] [Length] [Data...] [Checksum]
```

- **Address:** Always `0x49` for ECU commands, `0x69` for SMARTRA responses
- **Length:** Number of bytes after the Length field, including checksum
- **Checksum:** One-byte addition of all bytes excluding Address byte

### Checksum Example
Message: `0x49 0x05 0x55 0x02 0x03 0x04 ??`
Checksum = `0x05 + 0x55 + 0x02 + 0x03 + 0x04 = 0x63`

---

## Commands

### 0x06 — Acknowledge
Used to test if SMARTRA is ready to receive commands. Must respond before other commands will work.

```
ECU:    0x49 0x02 0x06 0x08
SMARTRA: 0x69 0x02 0x06 0x08
```

---

## Reference

Full SMARTRA3 protocol spec (FCC submission by Bosch):
`Smartra3_lxp-vima01_protocol-spec_march-2007.pdf` (available on OpenGK wiki)

Note: Manual covers SMARTRA3; GK uses SMARTRA2 — protocol is backwards compatible.
