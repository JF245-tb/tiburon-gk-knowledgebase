#!/usr/bin/env python3
"""
CAN wake / probe script for BlinkMarine / AiM CAN Keypad.
Use this if can-sniff.py found no frames — sends probe messages
to see if the keypad needs a wake-up or config frame.

Strategies:
  1. Send heartbeat-style frames on common AiM IDs
  2. Send remote frames requesting data
  3. Broadcast 0x000 wake
  4. Listen after each probe for responses

Usage:
    python can-wake.py                    # try all probes at 250k
    python can-wake.py --bitrate 500000   # try at 500k
    python can-wake.py --term-check       # measure bus resistance hint
"""

import os
import sys
import can
import time
import argparse

# Fix pyusb backend on Windows - point to the libusb DLL shipped with pip libusb
_LIBUSB_DLL = os.path.join(
    os.path.dirname(sys.executable), "Lib", "site-packages",
    "libusb", "_platform", "windows", "x86_64", "libusb-1.0.dll"
)
if os.path.exists(_LIBUSB_DLL):
    import usb.backend.libusb1
    usb.backend.libusb1.get_backend(find_library=lambda x: _LIBUSB_DLL)

# AiM ecosystem common IDs
AIM_PROBE_IDS = [
    0x00,   # broadcast wake
    0x19,   # AiM keypad ID range
    0x1A,
    0x1B,
    0x1C,
    0x100,  # common PDM heartbeat range
    0x200,
    0x7DF,  # OBD2 broadcast (unlikely but cheap to try)
]

# Generic wake payloads
WAKE_PAYLOADS = [
    bytes([0x00] * 8),          # all zeros
    bytes([0xFF] * 8),          # all ones
    bytes([0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),  # minimal
    bytes([0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),  # NMT start
]


def probe_and_listen(bus, arb_id, payload, listen_time=2.0):
    """Send a frame, then listen for any response."""
    msg = can.Message(
        arbitration_id=arb_id,
        data=payload,
        is_extended_id=False,
    )
    try:
        bus.send(msg)
        print(f"  TX -> ID=0x{arb_id:03X}  Data={payload.hex(' ')}")
    except can.CanError as e:
        print(f"  TX FAILED -> ID=0x{arb_id:03X}: {e}")
        return []

    # Listen for response
    responses = []
    start = time.time()
    while (time.time() - start) < listen_time:
        rx = bus.recv(timeout=0.5)
        if rx is not None:
            responses.append(rx)
            print(f"  RX ← ID=0x{rx.arbitration_id:03X}  "
                  f"DLC={rx.dlc}  "
                  f"Data={rx.data.hex(' ')}  "
                  f"** RESPONSE **")
    return responses


def run_probes(bitrate, listen_time=2.0):
    """Send all probe combinations and report results."""
    print(f"CAN Wake Probe — {bitrate} bps")
    print(f"Sending probe frames on {len(AIM_PROBE_IDS)} IDs "
          f"x {len(WAKE_PAYLOADS)} payloads")
    print(f"Listening {listen_time}s after each TX\n")

    try:
        bus = can.Bus(interface="gs_usb", channel=0, bitrate=bitrate)
    except Exception as e:
        print(f"ERROR opening bus: {e}")
        return

    all_responses = []
    total = len(AIM_PROBE_IDS) * len(WAKE_PAYLOADS)
    count = 0

    try:
        for arb_id in AIM_PROBE_IDS:
            for payload in WAKE_PAYLOADS:
                count += 1
                print(f"\n[{count}/{total}] Probing 0x{arb_id:03X}...")
                responses = probe_and_listen(bus, arb_id, payload, listen_time)
                all_responses.extend(responses)

                if responses:
                    print(f"\n  *** GOT {len(responses)} RESPONSE(S)! ***")
                    print(f"  Keypad responded to ID=0x{arb_id:03X} "
                          f"payload={payload.hex(' ')}")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        bus.shutdown()

    print(f"\n{'='*60}")
    if all_responses:
        print(f"  Total responses: {len(all_responses)}")
        unique_ids = set(r.arbitration_id for r in all_responses)
        print(f"  Response IDs: {', '.join(f'0x{i:03X}' for i in sorted(unique_ids))}")
        print(f"\n  Next: run can-sniff.py --bitrate {bitrate} to capture full traffic")
    else:
        print(f"  No responses to any probe.")
        print(f"  Troubleshooting:")
        print(f"    1. Add 120 ohm resistor between CAN-H and CAN-L")
        print(f"    2. Try other bitrate: python can-wake.py -b <rate>")
        print(f"    3. Check if Red wire needs +12V for full activation")
        print(f"    4. Swap CAN-H / CAN-L wires")
        print(f"    5. Verify keypad draws >0.036A when CAN is active")
    print(f"{'='*60}")


def bus_resistance_hint():
    """Remind user to check termination."""
    print("CAN Bus Termination Check")
    print("="*40)
    print("With keypad POWERED OFF and CAN wires disconnected:")
    print("  1. Measure resistance between CAN-H and CAN-L on the keypad connector")
    print("  2. Expected: 120 ohm if keypad has internal termination")
    print("  3. If open/high: keypad has NO internal termination")
    print()
    print("For a 2-node bus (adapter + keypad):")
    print("  - If keypad has 120 ohm: add 120 ohm at the adapter end -> 60 ohm total")
    print("  - If keypad has none: add 120 ohm at BOTH ends -> 60 ohm total")
    print("  - Quick bench hack: single 120 ohm across adapter H/L often works")
    print()
    print("Your RH-02/CANable likely has NO built-in termination.")
    print("A 100 ohm–130 ohm resistor across H/L on the adapter is fine for bench.")


def main():
    parser = argparse.ArgumentParser(
        description="CAN wake/probe for BlinkMarine/AiM keypad")
    parser.add_argument("--bitrate", "-b", type=int, default=250000,
                        help="CAN bitrate (default: 250000)")
    parser.add_argument("--listen", "-t", type=float, default=2.0,
                        help="Seconds to listen after each probe (default: 2)")
    parser.add_argument("--term-check", action="store_true",
                        help="Print termination resistance check instructions")
    args = parser.parse_args()

    if args.term_check:
        bus_resistance_hint()
        return

    run_probes(args.bitrate, listen_time=args.listen)


if __name__ == "__main__":
    main()
