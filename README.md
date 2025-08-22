# Laptop Repair Kit

This repository contains a cross‑platform toolkit for diagnosing and
repairing laptops. It includes Python scripts to gather hardware
information, firmware flashing helpers, and documentation outlining
repair procedures and acceptance criteria. Use it with **Visual Studio
Code** to streamline your workflow and maintain a consistent repair
process across Windows, Linux and macOS.

## Features

* **Battery diagnostics** – report charge percentage, plug status and
  capacity across different platforms.
* **Storage health** – fetch SMART information (requires
  smartmontools).
* **Sensor monitoring** – read temperatures and fan speeds via
  lm‑sensors, OpenHardwareMonitor or iStats depending on OS.
* **Keyboard tester** – capture key presses to verify all keys work.
* **Display test** – cycle through solid colours to spot dead pixels and
  backlight bleed.
* **Audio loopback** – play a test tone and record microphone input to
  measure RMS level.
* **Firmware flashing wrapper** – simplify BIOS/EC flashing with
  `flashrom` using a CH341A programmer.
* **Comprehensive documentation** – repair checklist and acceptance
  criteria for quality assurance.

## Setup

1. Install Python 3.11 or later on your system.
2. Install [smartmontools](https://www.smartmontools.org/) to enable
   storage diagnostics.
3. Clone this repository:
   ```bash
   git clone https://github.com/<your_username>/laptop-repair-kit.git
   cd laptop-repair-kit
   ```
4. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. (Windows only) Install `wmi` and `pywin32` for sensor and battery
   support:
   ```bash
   pip install wmi pywin32
   ```
6. (Linux only) Install `lm‑sensors` and run `sudo sensors-detect`.
7. (macOS only) Install [`iStats`](https://github.com/Chris911/iStats)
   via Homebrew (`brew install istats`).

## Using the diagnostics

You can run individual scripts from the command line:

```bash
python diagnostics/battery.py
python diagnostics/storage.py
python diagnostics/sensors.py
python diagnostics/keyboard.py
python diagnostics/display.py
python diagnostics/audio.py
```

Alternatively, open the folder in **VS Code** and use the built‑in
tasks (Terminal → Run Task) to launch each diagnostic without typing
commands manually. The task definitions reside in `.vscode/tasks.json`.

## Firmware flashing

The `firmware-tools/flashrom_wrapper.py` script wraps the `flashrom`
utility for convenience. It assumes you are using a CH341A SPI
programmer. To read a BIOS chip:

```bash
python firmware-tools/flashrom_wrapper.py -r backup.bin
```

To write a new image:

```bash
python firmware-tools/flashrom_wrapper.py -w new_image.bin
```

Make sure to back up the existing firmware before writing and check
manufacturer guidelines for safe flashing procedures.

## Documentation

The `docs` folder contains:

* **repair_checklist.md** – a step‑by‑step guide covering pre‑repair
  preparation, diagnostics and final checks.
* **acceptance_criteria.md** – a comprehensive list of minimum
  conditions the repaired laptop must meet before being returned.

Review these documents regularly to ensure your repair practices are
consistent and thorough.