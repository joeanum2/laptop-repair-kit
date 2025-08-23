"""
Cross‑platform sensor diagnostic utility.

On Linux this script uses `lm‑sensors` via `sensors -j` to output
temperatures and fan speeds in JSON format. On Windows it queries
OpenHardwareMonitor via WMI to report temperature and fan sensors. On macOS
it uses `istats` to print temperature and fan information. For other
platforms it reports that the platform is unsupported.
"""

import platform
import subprocess
import json


def main() -> None:
    system = platform.system()

    if system == "Linux":
        try:
            # `sensors -j` outputs JSON data of sensors
            out = subprocess.check_output(["sensors", "-j"], text=True)
            # Print raw JSON string; user can parse as needed
            print(out.strip())
        except FileNotFoundError:
            print("Install lm-sensors and ensure `sensors` is in PATH.")
        except subprocess.CalledProcessError as e:
            print("Error running sensors:", e)

    elif system == "Windows":
        try:
            import wmi  # type: ignore

            w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
            results: list[dict[str, object]] = []
            for sensor in w.Sensor():
                # Only capture temperatures and fan speeds
                if sensor.SensorType in ("Temperature", "Fan"):
                    results.append({
                        "name": sensor.Name,
                        "type": sensor.SensorType,
                        "value": sensor.Value,
                    })
            print(json.dumps(results, indent=2))
        except ImportError:
            print("Install pywin32 and wmi Python modules.")
        except Exception:
            print("Ensure OpenHardwareMonitor is running and WMI namespace is accessible.")

    elif system == "Darwin":  # macOS
        try:
            # `istats` prints temperatures and other metrics
            out = subprocess.check_output(["istats"], text=True)
            print(out.strip())
        except FileNotFoundError:
            print("Install iStats via Homebrew (brew install istats).")
        except subprocess.CalledProcessError as e:
            print("Error running istats:", e)

    else:
        print(f"Unsupported platform: {system}")


if __name__ == "__main__":
    main()
