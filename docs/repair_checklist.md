# Laptop Repair Checklist

Use this checklist to document and guide your laptop repair process. Each
step helps ensure you diagnose faults correctly, perform repairs safely
and verify that the laptop meets acceptance criteria before returning it
to a customer or putting it back into service.

## Pre‑repair

1. **ESD Precautions:** Put on your ESD wrist strap and ensure the
   workstation is grounded. Lay the laptop on an ESD mat.
2. **Visual Inspection:** Check the chassis, hinges, keyboard and ports
   for obvious damage, debris or liquid ingress. Photograph
   pre‑repair condition for reference.
3. **Power Tests:** Using a bench PSU with current limiting, apply
   appropriate voltage to the DC‑in jack or battery pins. Observe
   current draw; high immediate current suggests a shorted rail.
4. **Battery Removal:** Disconnect and, if possible, remove the battery
   to prevent accidental charging during board work.
5. **Disassembly:** Carefully disassemble the laptop following the
   manufacturer’s guide. Label screws and note cable locations.
6. **Board Inspection:** Look for burnt components, liquid damage,
   cracked traces or bulging capacitors. Clean corrosion with
   isopropyl alcohol if present.

## Repair activities

1. **Diagnosis:** Use a multimeter to check power rails, continuity and
   diodes. If the BIOS is suspected, connect your CH341A programmer
   using the SOIC8 clip and back up the SPI flash (`flashrom_wrapper.py -r backup.bin`).
2. **Component Replacement/Repair:** Replace faulty components such as
   MOSFETs, capacitors or the DC‑in jack. Use flux, solder wick and
   hot air where appropriate.
3. **Firmware Update:** Flash a known‑good BIOS/EC image using
   `flashrom_wrapper.py -w new.bin` if firmware corruption was the cause.
4. **Reassemble:** Refit the board, reconnect cables and install the
   battery. Ensure thermal paste and pads are replaced on CPU/GPU.

## Post‑repair diagnostics

1. **Power On:** Power the laptop via its charger or PSU. Check that
   all power rails come up and the CPU fan spins.
2. **BIOS Access:** Enter BIOS/UEFI. Verify that the system recognises
   memory, storage and battery correctly.
3. **Run Diagnostic Scripts:** With the laptop booted into an OS:
   - **Battery:** `python diagnostics/battery.py` – record
     percentage, charge status and capacity.
   - **Storage:** `python diagnostics/storage.py` – note model,
     serial, power‑on hours and error metrics.
   - **Sensors:** `python diagnostics/sensors.py` – verify CPU/GPU
     temperatures and fan speeds.
   - **Keyboard:** `python diagnostics/keyboard.py` – test all
     keys, ensuring none are stuck or unresponsive.
   - **Display:** `python diagnostics/display.py` – cycle colours to
     check for dead pixels, colour uniformity and backlight bleed.
   - **Audio:** `python diagnostics/audio.py` – play and record to
     confirm speaker/microphone functionality.
4. **Functional Checks:** Test Wi‑Fi, Bluetooth, USB ports, webcam and
   card reader. Insert known‑good peripherals to confirm detection.
5. **Charging Test:** Connect the charger and measure the charging
   current with a USB power meter. Ensure the battery percentage
   increases over time.
6. **Final Assembly:** Once all tests pass, replace the bottom cover
   and screws. Clean the laptop exterior.

## Documentation

Log the following in your service report:

| Item                       | Details                                 |
|---------------------------|------------------------------------------|
| Laptop model / serial     |                                          |
| Fault description         |                                          |
| Pre‑repair notes          |                                          |
| Components replaced       |                                          |
| Firmware versions         |                                          |
| Test results (battery)    |                                          |
| Test results (storage)    |                                          |
| Test results (sensors)    |                                          |
| Test results (keyboard)   |                                          |
| Test results (display)    |                                          |
| Test results (audio)      |                                          |
| Additional observations   |                                          |

Use this log to support quality assurance and to track recurring
hardware issues across multiple repairs.
