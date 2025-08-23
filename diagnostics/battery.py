import platform
import subprocess
import psutil
import os
import json


def battery_generic() -> dict:
    """Return generic battery information via psutil."""
    b = psutil.sensors_battery()
    if b:
        return {
            "percent": b.percent,
            "plugged": b.power_plugged,
            "secs_left": b.secsleft,
        }
    return {}


def battery_windows() -> dict:
    """Retrieve Windows‑specific battery details using WMI."""
    try:
        import wmi  # type: ignore

        w = wmi.WMI(namespace="root\\wmi")
        details: dict[str, int] = {}
        for x in w.BatteryFullChargedCapacity():
            # Report the full charge capacity in milli‑watt‑hours
            details["full_capacity_mWh"] = x.FullChargedCapacity
        return details
    except Exception:
        # Either wmi module is unavailable or query failed
        return {}


def battery_linux() -> dict:
    """Retrieve Linux battery percentage from sysfs if available."""
    base = "/sys/class/power_supply/BAT0/"
    capacity_path = os.path.join(base, "capacity")
    if os.path.exists(capacity_path):
        try:
            with open(capacity_path) as f:
                return {"percent_linux": int(f.read().strip())}
        except Exception:
            pass
    return {}


def battery_macos() -> dict:
    """Retrieve macOS battery information via pmset."""
    try:
        # pmset returns battery status; capture as plain text
        out = subprocess.check_output(["pmset", "-g", "batt"], text=True)
        return {"pmset": out.strip()}
    except Exception:
        return {}


if __name__ == "__main__":
    system_name = platform.system()
    info: dict[str, object] = {"os": system_name}
    if system_name == "Windows":
        info.update(battery_windows())
    elif system_name == "Linux":
        info.update(battery_linux())
    elif system_name == "Darwin":
        info.update(battery_macos())
    # Always include generic info as a base layer
    info.update(battery_generic())
    print(json.dumps(info, indent=2))
