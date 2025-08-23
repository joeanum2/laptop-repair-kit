# Laptop Repair Acceptance Criteria

This document defines the minimum conditions a repaired laptop must meet
before it is considered serviceable. Use it alongside the repair
checklist to verify every unit passes a consistent set of tests.

## Power and firmware

* The laptop powers on without abnormal delays, beeps or repeated
  restarts.
* BIOS/UEFI recognises the correct CPU, RAM capacity and storage
  devices.
* The BIOS/EC firmware version matches the approved release or has been
  updated to the latest stable version per manufacturer guidelines.

## Battery and charging

* Battery percentage and charging status are reported accurately.
* Full charge capacity is at least 80 % of design capacity or meets
  customer‑specified threshold.
* The system charges from an AC adapter without error messages.
* Charging current stays within the expected range for the battery type
  and does not intermittently drop out.

## Storage health

* SMART attributes show no reallocated sectors or pending sectors
  (ATA) and no critical errors (NVMe).
* Power‑on hours and wear level are within acceptable limits for the
  device’s age and usage.
* The drive is detected by the OS and file system integrity checks
  return no errors.

## Thermal performance

* Idle CPU temperature is within 40–50 °C and does not exceed
  90 °C under stress for mainstream mobile CPUs (adjust for high‑end
  or low‑power chips accordingly).
* All installed fans spin up under load and report RPM values via
  sensors.
* Heatsinks and cooling assemblies are securely attached and free from
  dust or obstructions.

## Input devices

* Every key on the internal keyboard registers correctly without
  sticking or double‑pressing.
* Touchpad responds smoothly to movement and gestures, with no
  dead zones.
* All physical buttons (power, volume, trackpad, etc.) operate and
  feel normal.

## Display

* There are no stuck or dead pixels visible during solid colour tests.
* Backlight brightness is uniform without significant bleeding at the
  edges.
* The panel exhibits normal colour balance and no flickering or
  banding.

## Audio

* Speakers produce clear sound across the frequency range without
  distortion or crackling.
* Microphone input is detected and records at a usable level without
  constant background noise.

## Connectivity and ports

* Wi‑Fi and Bluetooth interfaces detect networks/devices and maintain
  stable connections.
* All USB, HDMI, audio and SD card ports function and appear in the
  operating system when devices are inserted.
* Webcam and any sensors (fingerprint reader, IR camera) operate and
  are recognised by the OS.

## Documentation

* Service report is completed with all sections of the repair
  checklist filled out, including test results and any parts replaced.
* Serial numbers and model identifiers match the job ticket.

Only when all criteria above have been satisfied should the laptop be
signed off and returned to the customer or stock.
