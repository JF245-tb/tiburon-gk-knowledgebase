# Siemens 5WY ECM Identification Guide
**Source:** https://opengk.org/index.php?title=5WY_ECM_Identification

---

## Label Reading

ECM labels contain 10 identification elements:
- **Hardware revision** (e.g., "5WY1611B") → indicates ECM family
- **Region code:** N = North America, D = Korea, E/F/T/G = European variants
- **Engine designation:** 7 = Delta 2.7L V6, C = Beta 2.0L CVVT
- **Date code:** DAY.MONTH.YEAR format → flash programming date

## 2.7L V6 Delta — 5WY 5 Connector

| Family | Years | EEPROM | Engine | Notes |
|--------|-------|--------|--------|-------|
| 5WY12 | 1999-2001 | 2MBit (256KB) | G6BV/G6BW | Older V6 |
| 5WY15 | 2002-2003 | 2MBit (256KB) | G6BA | **Blue Tiburon likely candidate** |
| 5WY17-5WY1F | 2003-2009 | 4MBit (512KB) | G6BA | Later production |

Label format: N (region) + 7 (2.7L) + year digit + G (GK chassis)

**Note:** Pre/post January 31, 2003 ECUs have different O2 sensor requirements (5-volt vs 1-volt upstream sensors). Check ECU label date to determine which sensors to use.

## 2.0L L4 Beta — 5WY 2 Connector

| Family | Years | EEPROM | Notes |
|--------|-------|--------|-------|
| 5WY14 | 2002-2003 | 2MBit | No CVVT |
| 5WY16/5WY41 | 2004-2006 | 4MBit | With CVVT |
| 5WY19/5WY1A/5WY44 | 2007-2009 | 4MBit | Later variants |

Label format: N (North America) + C (CVVT) + year digit + G (chassis)
