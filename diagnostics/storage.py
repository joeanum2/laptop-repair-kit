"""
Retrieve SMART information from storage devices on Windows, Linux or macOS.

This script relies on the `smartctl` command from the smartmontools suite. It
outputs a JSON summary including model, serial, power or hours, and other key
metrics such as reallocated sector count or NVMe wear.

Usage:
    python storage.py [device]

If no device is provided, it defaults to the first physical drive on Windows
(`physicaldrive0`) and `/dev/sda` on other systems.
"""

import json
import shutil
import subprocess
import sys
import platform


def main() -> None:
    # Accept a device path/name as the first argument; otherwise use a default
    drive: str | None = sys.argv[1] if len(sys.argv) > 1 else None

    # Ensure smartctl is available
    if not shutil.which("smartctl"):
        print("smartctl not found. Install smartmontools and add to PATH.")
        sys.exit(1)

    system = platform.system()
    if system == "Windows":
        # Default to first physical drive on Windows
        drive = drive or "physicaldrive0"
        cmd = ["smartctl", "-a", f"//./{drive}", "-j"]
    else:
        # On Linux and macOS assume /dev/sda if not specified
        drive = drive or "/dev/sda"
        cmd = ["smartctl", "-a", drive, "-j"]

    try:
        # Execute smartctl and capture its JSON output
        output = subprocess.check_output(cmd, text=True, errors="ignore")
        data = json.loads(output)
    except subprocess.CalledProcessError as e:
        print("SMART command failed:", e)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print("Failed to parse smartctl output as JSON:", e)
        sys.exit(1)

    # Build summary from the parsed data
    summary: dict[str, object] = {
        "model": data.get("model_name"),
        "serial": data.get("serial_number"),
        "power_on_hours": data.get("power_on_time", {}).get("hours"),
    }

    # ATA drives: extract reallocated sector count if present
    ata_table = data.get("ata_smart_attributes", {}).get("table")
    if isinstance(ata_table, list):
        for attr in ata_table:
            if attr.get("name") == "Reallocated_Sector_Ct":
                raw = attr.get("raw")
                if raw and isinstance(raw, dict):
                    summary["reallocated"] = raw.get("value")
                break

    # NVMe drives: extract percent used if available
    nvme_log = data.get("nvme_smart_health_information_log", {})
    if isinstance(nvme_log, dict) and "percent_used" in nvme_log:
        summary["percent_used"] = nvme_log.get("percent_used")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
