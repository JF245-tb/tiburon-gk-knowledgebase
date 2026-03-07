# Immobiliser Systems
**Source:** https://opengk.org/index.php?title=Immobiliser

---

## By Engine / Market

### 2.7L V6 (Both Tiburons)
**Architecture:** Contained entirely within the BCM. ECU doesn't store any immobiliser data — it only asks the BCM for permission to start.

- Uses passive mutual authentication
- Components: key transponder → standalone antenna → BCM → ECM
- BCM performs the immobilisation function
- ECM simply requests start permission from BCM

**Relevance to Blue Tiburon:** With the start button conversion and no ignition switch, the immobiliser bypass/programming needs to be handled. Since it's BCM-based, the ECU itself doesn't care — the BCM must be convinced to grant start permission.

### 2.0L L4 (Reference only)
**Architecture:** Contained entirely within the ECU. BCM acts as intermediate but doesn't store data.

- Uses SMARTRA (Smart Transponder Antenna) — Bosch system
- SMARTRA2 version on this platform
- Transponders pair only to the ECU

### US Market
US market vehicles reportedly have no immobiliser by default.

---

## OpenGK Wiki Pages for Further Reading
- https://opengk.org/index.php?title=SMARTRA
- https://opengk.org/index.php?title=SMARTRA_Protocol
- https://opengk.org/index.php?title=Keyfob
