#!/usr/bin/env python3
"""
Verify whether a Siemens SIMK41/SIMK43 EEPROM dump is in factory configuration.

Intended workflow: dump the installed ECU with GKFlasher (`--read`), then run this
script against the dump to decide whether it is stock or carries a tune. Nothing
here touches the car -- it only reads .bin files on disk.

Three independent checks, weakest to strongest:

  1. FINGERPRINT  Reads the ECU's own identity strings out of the dump
                  (description, calibration, hardware revision, part number).
                  These are what OpenGK's factory bin filenames are built from, so
                  a fingerprint tells you WHICH reference bin to compare against.
                  A GKFlasher tune normally leaves these untouched, so a match
                  here is necessary but NOT sufficient.

  2. CHECKSUM     Recomputes the CRC16 for every region using the same algorithm
                  as GKFlasher's --correct-checksum and compares to the stored
                  values. A MISMATCH proves the file was edited. A match does not
                  prove stock -- GKFlasher fixes checksums automatically.

  3. DIFF         Byte-compares against a known-good factory reference bin from
                  https://opengk.org/files/?dir=EEPROMS/Siemens and clusters the
                  differing bytes into contiguous runs. This is the decisive test.
                  Scattered single bytes are adaptives/learned values; long
                  contiguous runs inside the calibration zone are a tune.

Usage:
    # Identify a dump and audit its checksums
    python verify-ecu-stock.py dump.bin

    # Full comparison against the matching factory reference
    python verify-ecu-stock.py dump.bin --reference ca652051_G3N7TS0H_....bin

    # Compare two of your own ECUs against each other
    python verify-ecu-stock.py ecu-a.bin --reference ecu-b.bin

Reference bins for the 2.7L V6 Tiburon live under EEPROMS/Siemens/GK-27.
Match on the first two filename fields (description_calibration).

See Knowledgebase/common/opengk/ecu-factory-verification.md for the full procedure.
"""

import sys
import argparse

# ---------------------------------------------------------------------------
# ECU layout tables, mirrored from GKFlasher ecu_definitions.py / checksum.py.
# `ident_offset` and region addresses are EEPROM addresses; `bin_offset` converts
# an EEPROM address to a file offset.
# ---------------------------------------------------------------------------

ECU_TYPES = [
    {
        "name": "SIMK41 / V6 2mbit",
        "size": 262144,
        "bin_offset": -0x40000,
        "ident_offset": 0x48040,
        "prefixes": [b"ca660", b"ca652", b"ca650"],
        "calibration": (0x48000, 0x8000),
        "program": (0x50000, 0x30000),
        "cks": "2mbit",
    },
    {
        "name": "SIMK43 V6 4mbit (5WY17)",
        "size": 524288,
        "bin_offset": -0x80000,
        "ident_offset": 0x88040,
        "prefixes": [b"ca65401"],
        "calibration": (0x88000, 0x5F40),
        "program": (0x90000, 0x70000),
        "cks": "v6 (5WY17)",
    },
    {
        "name": "SIMK43 V6 4mbit (5WY18+)",
        "size": 524288,
        "bin_offset": -0x80000,
        "ident_offset": 0x88040,
        "prefixes": [b"ca654", b"ca655"],
        "calibration": (0x88000, 0x6EFF),
        "program": (0x90000, 0x70000),
        "cks": "v6 (5WY18+)",
    },
]

# Checksum region tables, copied from GKFlasher flasher/checksum.py.
# Addresses here are already file offsets (that is how GKFlasher uses them).
CKS_TYPES = {
    "2mbit": {
        "flag": 0xFEFE,
        "regions": [
            ("Boot", 0x3FE4, 0x3EF4, 0),
            ("Calibration", 0x00800C, 0x0FEE0, -0x40000),
            ("Program", 0x010052, 0x010010, -0x40000),
        ],
    },
    "v6 (5WY17)": {
        "flag": 0xDEFE,
        "regions": [
            ("Boot", 0x3FE4, 0x3EF4, 0),
            ("Calibration", 0x0800C, 0xDEE0, -0x80000),
            ("Program", 0x010052, 0x010010, -0x80000),
        ],
    },
    "v6 (5WY18+)": {
        "flag": 0xEEFE,
        "regions": [
            ("Boot", 0x3FE4, 0x3EF4, 0),
            ("Calibration", 0x0800C, 0xEEE0, -0x80000),
            ("Program", 0x010052, 0x010010, -0x80000),
        ],
    },
}


def crc16(data, init):
    """Reflected CRC16, poly 0x8005 -- equivalent to crcmod.mkCrcFun(0x18005, initCrc=init).

    Reimplemented in pure Python so this script has no dependencies. Verified to
    reproduce GKFlasher's stored checksums exactly on known-good factory bins.
    """
    crc = init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return crc & 0xFFFF


def _read_reversed(payload, start, length):
    return list(payload[start:start + length])[::-1]


def _concat3(b):
    return ((b[0] << 8 | b[1]) << 8 | b[2])


def identify(payload):
    """Return the ECU_TYPES entry matching this dump, or None."""
    for ecu in ECU_TYPES:
        if len(payload) != ecu["size"]:
            continue
        pos = ecu["ident_offset"] + ecu["bin_offset"]
        if pos + 8 > len(payload):
            continue
        desc = payload[pos:pos + 8]
        if any(desc.startswith(p) for p in ecu["prefixes"]):
            return ecu
    return None


def _ascii(raw):
    return "".join(chr(c) if 32 <= c < 127 else "." for c in raw)


def fingerprint(payload, ecu):
    """Pull the ECU identity strings out of a dump.

    description  = 8 bytes at the identification offset (calibration start + 0x40)
    calibration  = 8 bytes at the calibration zone start
    These are the first two fields of every OpenGK factory bin filename.
    """
    cal_addr = ecu["calibration"][0]
    off = ecu["bin_offset"]
    desc = _ascii(payload[cal_addr + 0x40 + off: cal_addr + 0x40 + off + 8])
    cal = _ascii(payload[cal_addr + off: cal_addr + off + 8])

    # Hardware revision (5WYxxxx) and Hyundai part number live outside the
    # calibration zone at model-specific offsets, so locate them by pattern.
    hw = "not found"
    idx = payload.find(b"5WY")
    if idx >= 0:
        hw = _ascii(payload[idx:idx + 8])

    ecu_id = "not found"
    idx_hmc = payload.find(b"HMC")
    if idx_hmc >= 0:
        ecu_id = _ascii(payload[idx_hmc:idx_hmc + 28])

    return {
        "description": desc,
        "calibration": cal,
        "hardware": hw,
        "ecu_id": ecu_id,
    }


def audit_checksums(payload, ecu):
    """Recompute every region checksum and compare to what is stored in the dump.

    Returns a list of (region_name, stored, computed, ok) tuples.
    """
    spec = CKS_TYPES.get(ecu["cks"])
    if spec is None:
        return None
    if payload[spec["flag"]:spec["flag"] + 2] != b"OK":
        return None

    results = []
    for name, init_address, cks_address, bin_offset in spec["regions"]:
        zones = payload[cks_address + 2]
        if zones in (0, 0xFF):
            results.append((name, None, None, None))
            continue

        checks = []
        zone_addr = cks_address
        for i in range(zones):
            start = _concat3(_read_reversed(payload, zone_addr + 0x04, 3)) + bin_offset
            stop = _concat3(_read_reversed(payload, zone_addr + 0x08, 3)) + bin_offset + 1
            if i == 0:
                iv_bytes = _read_reversed(payload, init_address, 2)
                init = (iv_bytes[0] << 8) | iv_bytes[1]
            else:
                init = checks[i - 1]
            checks.append(crc16(payload[start:stop], init))
            zone_addr += 0x08

        last = checks[-1]
        computed = ((last & 0xFF) << 8) | ((last >> 8) & 0xFF)
        stored = int.from_bytes(payload[cks_address:cks_address + 2], "big")
        results.append((name, stored, computed, stored == computed))

    return results


def cluster_diff(a, b, gap=16):
    """Byte-compare two dumps and group differing bytes into contiguous runs.

    Runs separated by fewer than `gap` matching bytes are merged, so an edited
    map shows up as one run rather than hundreds of single-byte hits.
    """
    diffs = [i for i in range(min(len(a), len(b))) if a[i] != b[i]]
    if not diffs:
        return []

    runs = []
    start = prev = diffs[0]
    count = 1
    for i in diffs[1:]:
        if i - prev <= gap:
            prev = i
            count += 1
        else:
            runs.append((start, prev, count))
            start = prev = i
            count = 1
    runs.append((start, prev, count))
    return runs


def region_of(file_offset, ecu):
    """Name the ECU region a given file offset falls into."""
    off = ecu["bin_offset"]
    cal_start, cal_size = ecu["calibration"]
    prog_start, prog_size = ecu["program"]
    addr = file_offset - off
    if cal_start <= addr < cal_start + cal_size:
        return "CALIBRATION"
    if prog_start <= addr < prog_start + prog_size:
        return "program"
    return "boot/other"


def main():
    parser = argparse.ArgumentParser(
        description="Check whether a SIMK41/SIMK43 EEPROM dump is in factory configuration.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("dump", help="EEPROM dump from GKFlasher --read")
    parser.add_argument("-r", "--reference",
                        help="Known-good factory bin to compare against (OpenGK EEPROMS/Siemens)")
    parser.add_argument("--gap", type=int, default=16,
                        help="Merge diff runs separated by fewer than N matching bytes (default 16)")
    args = parser.parse_args()

    try:
        with open(args.dump, "rb") as fh:
            payload = fh.read()
    except OSError as e:
        print("[!] Could not read {}: {}".format(args.dump, e))
        return 1

    print("=" * 68)
    print("  ECU FACTORY CONFIGURATION CHECK")
    print("=" * 68)
    print("[*] File: {}  ({:,} bytes)".format(args.dump, len(payload)))

    ecu = identify(payload)
    if ecu is None:
        print("[!] Unrecognised dump. Expected 262,144 or 524,288 bytes with a")
        print("    'ca6xx' identification string. A partial read will look like this.")
        return 1
    print("[*] ECU type: {}".format(ecu["name"]))

    # --- 1. Fingerprint ----------------------------------------------------
    fp = fingerprint(payload, ecu)
    print()
    print("-- 1. FINGERPRINT " + "-" * 50)
    print("    Description  : {}".format(fp["description"]))
    print("    Calibration  : {}".format(fp["calibration"]))
    print("    Hardware rev : {}".format(fp["hardware"]))
    print("    ECU ID       : {}".format(fp["ecu_id"]))
    print()
    print("    Look for a reference bin named {}_{}_*.bin".format(
        fp["description"], fp["calibration"]))
    print("    at https://opengk.org/files/?dir=EEPROMS/Siemens/GK-27")

    # --- 2. Checksums ------------------------------------------------------
    print()
    print("-- 2. CHECKSUM AUDIT " + "-" * 47)
    results = audit_checksums(payload, ecu)
    if results is None:
        print("    [!] Could not locate checksum tables -- dump may be incomplete.")
        checksum_bad = False
    else:
        checksum_bad = False
        for name, stored, computed, ok in results:
            if stored is None:
                print("    {:<12} skipped (no zones defined)".format(name))
                continue
            status = "OK" if ok else "MISMATCH <-- EDITED"
            print("    {:<12} stored={:#06x}  computed={:#06x}  {}".format(
                name, stored, computed, status))
            if not ok:
                checksum_bad = True
        if checksum_bad:
            print()
            print("    A mismatch proves this file was modified after it left the")
            print("    factory. A clean result does not prove stock -- GKFlasher")
            print("    recomputes checksums whenever it flashes.")

    # --- 3. Diff -----------------------------------------------------------
    print()
    print("-- 3. REFERENCE DIFF " + "-" * 47)
    if not args.reference:
        print("    Skipped. Re-run with --reference <factory.bin> for the decisive test.")
        print()
        print("=" * 68)
        return 0

    try:
        with open(args.reference, "rb") as fh:
            ref = fh.read()
    except OSError as e:
        print("    [!] Could not read {}: {}".format(args.reference, e))
        return 1

    if len(ref) != len(payload):
        print("    [!] Size mismatch: dump is {:,} bytes, reference is {:,}.".format(
            len(payload), len(ref)))
        print("        These are different ECU families -- comparison is meaningless.")
        return 1

    ref_fp = fingerprint(ref, ecu)
    print("    Reference: {}".format(args.reference))
    print("    Reference calibration: {} / {}".format(
        ref_fp["description"], ref_fp["calibration"]))
    cal_match = ((ref_fp["description"], ref_fp["calibration"])
                 == (fp["description"], fp["calibration"]))
    if not cal_match:
        print()
        print("    [!] Calibration IDs differ between dump and reference. Differences")
        print("        below will reflect that, not tuning. Find a matching reference.")
    print()

    runs = cluster_diff(payload, ref, gap=args.gap)
    if not runs:
        print("    IDENTICAL -- byte-for-byte match with the reference.")
        print()
        print("=" * 68)
        print("  VERDICT: STOCK")
        print("=" * 68)
        return 0

    total = sum(r[2] for r in runs)
    print("    {:,} differing bytes in {} run(s):".format(total, len(runs)))
    print()
    print("    {:<12} {:<12} {:>8}  {:<10}".format("FILE START", "FILE END", "BYTES", "REGION"))
    cal_bytes = 0
    for start, end, count in runs[:40]:
        region = region_of(start, ecu)
        if region == "CALIBRATION":
            cal_bytes += count
        print("    {:<12} {:<12} {:>8}  {:<10}".format(
            hex(start), hex(end), count, region))
    if len(runs) > 40:
        remaining = runs[40:]
        for start, _, count in remaining:
            if region_of(start, ecu) == "CALIBRATION":
                cal_bytes += count
        print("    ... and {} more run(s)".format(len(remaining)))

    print()
    print("=" * 68)
    if not cal_match:
        print("  VERDICT: NOT COMPARABLE.")
        print("  These are two different calibrations ({} vs {}), so the".format(
            fp["calibration"], ref_fp["calibration"]))
        print("  differences above say nothing about whether either one is tuned.")
        print("  Get a reference bin whose first two filename fields match:")
        print("      {}_{}_*.bin".format(fp["description"], fp["calibration"]))
    elif cal_bytes == 0:
        print("  VERDICT: calibration zone is CLEAN.")
        print("  Differences fall outside the tuning area -- most likely adaptives")
        print("  or per-car data rather than a tune.")
    elif len(runs) <= 4 and cal_bytes < 32:
        print("  VERDICT: LIKELY STOCK, {} calibration byte(s) differ.".format(cal_bytes))
        print("  A handful of scattered bytes is consistent with learned values.")
        print("  Inspect them before trusting this result.")
    else:
        print("  VERDICT: MODIFIED -- {} bytes differ inside the calibration zone".format(cal_bytes))
        print("  across contiguous runs. That is the signature of a flashed tune.")
        print("  This is very likely your tuned ECU.")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    sys.exit(main())
