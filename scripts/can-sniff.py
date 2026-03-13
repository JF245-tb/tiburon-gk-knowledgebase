#!/usr/bin/env python3
"""
CAN bus sniffer for BlinkMarine / AiM CAN Keypad bench testing.
Uses gs_usb (candlelight) firmware on CANable / RH-02 adapter.

Usage:
    python can-sniff.py 250000           # listen at 250k (default 30s)
    python can-sniff.py 125000 -d 10     # listen at 125k for 10s
    python can-sniff.py 250000 --log     # listen + save to CSV
    python can-sniff.py scan             # auto-scan common bitrates (5s each)

NOTE: On Windows with gs_usb, only ONE bitrate per script run is reliable.
      The 'scan' mode restarts the process for each bitrate automatically.

Expected AiM 12-button keypad CAN IDs: 0x19, 0x1A, 0x1B, 0x1C
"""

import os
import sys
import time
import argparse
import csv
import subprocess
from datetime import datetime
from collections import defaultdict

# Fix pyusb backend on Windows
_LIBUSB_DLL = os.path.join(
    os.path.dirname(sys.executable), "Lib", "site-packages",
    "libusb", "_platform", "windows", "x86_64", "libusb-1.0.dll"
)
if os.path.exists(_LIBUSB_DLL):
    import usb.backend.libusb1
    usb.backend.libusb1.get_backend(find_library=lambda x: _LIBUSB_DLL)

import can

BITRATES = [250000, 500000, 125000, 1000000, 100000]

# AiM keypad known IDs (from Blink/AiM FAQ for 12-button)
AIM_KEYPAD_IDS = {0x19, 0x1A, 0x1B, 0x1C}


def listen(bitrate, duration=30.0, log_file=None):
    """Listen at a single bitrate. This is the core function."""
    print(f"{'='*60}")
    print(f"  Bitrate: {bitrate} bps")
    print(f"  Duration: {duration}s (Ctrl+C to stop early)")
    print(f"  Adapter: gs_usb (CANable / RH-02)")
    print(f"{'='*60}")
    print(f"  Press keypad buttons now...")
    print()

    bus = None
    frames = []
    try:
        bus = can.Bus(interface="gs_usb", channel=0, bitrate=bitrate)
        start = time.time()
        while (time.time() - start) < duration:
            msg = bus.recv(timeout=0.5)
            if msg is not None:
                frames.append(msg)
                ts = time.time() - start
                tag = " << AiM KEYPAD" if msg.arbitration_id in AIM_KEYPAD_IDS else ""
                print(f"  [{ts:6.2f}s] ID=0x{msg.arbitration_id:03X}  "
                      f"DLC={msg.dlc}  "
                      f"Data={msg.data.hex(' ')}  "
                      f"{'EXT' if msg.is_extended_id else 'STD'}"
                      f"{tag}")
    except KeyboardInterrupt:
        print("\n  Stopped by user.")
    except Exception as e:
        print(f"  ERROR: {e}")
    finally:
        if bus is not None:
            bus.shutdown()

    # Summary
    print()
    if frames:
        print(f"  >> {len(frames)} frames captured at {bitrate} bps")
        summarize_frames(frames)
        if log_file:
            save_log(frames, log_file)
    else:
        print(f"  No frames at {bitrate} bps.")
        print(f"  Check: termination, wiring, power, bitrate.")

    return len(frames)


def summarize_frames(frames):
    """Print summary of unique IDs and data patterns."""
    by_id = defaultdict(list)
    for msg in frames:
        by_id[msg.arbitration_id].append(msg)

    print(f"\n  Unique CAN IDs: {len(by_id)}")
    for arb_id in sorted(by_id.keys()):
        msgs = by_id[arb_id]
        unique_data = set(m.data.hex() for m in msgs)
        print(f"    0x{arb_id:03X}: {len(msgs)} frames, "
              f"{len(unique_data)} unique payloads")
        for i, d in enumerate(sorted(unique_data)):
            if i >= 5:
                print(f"           ... and {len(unique_data) - 5} more")
                break
            print(f"           {d}")


def save_log(frames, filename):
    """Save captured frames to CSV."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "id_hex", "id_dec", "dlc",
                         "data_hex", "is_extended", "channel"])
        for msg in frames:
            writer.writerow([
                msg.timestamp,
                f"0x{msg.arbitration_id:03X}",
                msg.arbitration_id,
                msg.dlc,
                msg.data.hex(" "),
                msg.is_extended_id,
                msg.channel,
            ])
    print(f"\n  Log saved: {filepath} ({len(frames)} frames)")


def auto_scan():
    """Scan all bitrates by spawning a subprocess for each one.
    This avoids the Windows gs_usb device release bug."""
    print("BlinkMarine / AiM CAN Keypad - Bitrate Auto-Scan")
    print(f"Testing: {', '.join(str(b) for b in BITRATES)} bps (5s each)")
    print(f"Press keypad buttons during each window.\n")

    script = os.path.abspath(__file__)
    for bitrate in BITRATES:
        print(f"\n--- Scanning {bitrate} bps ---")
        result = subprocess.run(
            [sys.executable, script, str(bitrate), "-d", "5", "--_internal_scan"],
            capture_output=False,
            timeout=15,
        )
        if result.returncode == 42:  # special exit code = frames found
            print(f"\n{'*'*60}")
            print(f"  FOUND TRAFFIC at {bitrate} bps!")
            print(f"  Run: python can-sniff.py {bitrate}")
            print(f"{'*'*60}")
            return
        time.sleep(0.5)  # let USB release

    print(f"\n{'!'*60}")
    print(f"  No frames at any bitrate.")
    print(f"  Next steps:")
    print(f"    1. Enable R120 on RH-02 (120 ohm termination)")
    print(f"    2. Run: python can-wake.py")
    print(f"    3. Try Red wire to +12V")
    print(f"    4. Swap CAN-H / CAN-L")
    print(f"{'!'*60}")


def main():
    parser = argparse.ArgumentParser(
        description="CAN sniffer for BlinkMarine/AiM keypad bench test")
    parser.add_argument("bitrate", nargs="?", default=None,
                        help="Bitrate in bps (e.g. 250000) or 'scan' for auto-scan")
    parser.add_argument("-d", "--duration", type=float, default=30.0,
                        help="Listen duration in seconds (default: 30)")
    parser.add_argument("-l", "--log", action="store_true",
                        help="Save frames to CSV")
    parser.add_argument("--logfile", type=str, default=None,
                        help="CSV filename (default: auto-timestamped)")
    parser.add_argument("--_internal_scan", action="store_true",
                        help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.bitrate is None or args.bitrate.lower() == "scan":
        auto_scan()
        return

    bitrate = int(args.bitrate)
    log_file = args.logfile
    if args.log and not log_file:
        log_file = f"can-log-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"

    count = listen(bitrate, duration=args.duration, log_file=log_file)

    # Special exit code for scan mode
    if args._internal_scan and count > 0:
        sys.exit(42)


if __name__ == "__main__":
    main()
