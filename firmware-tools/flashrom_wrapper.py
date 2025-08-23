"""
Wrapper for the `flashrom` utility to simplify BIOS and EC flashing.

This script checks for the presence of `flashrom` on your PATH and
then forwards all additional command‑line arguments to it using the
CH341A programmer by default. For example, to read a SPI chip into
`dump.bin` use:

    python flashrom_wrapper.py -r dump.bin

To write an image called `new.bin`:

    python flashrom_wrapper.py -w new.bin

Please ensure you have backed up the existing firmware before writing.
"""

import subprocess
import sys
import shutil



def main() -> None:
    # Verify flashrom is available
    if not shutil.which("flashrom"):
        print("flashrom not found. Install and ensure it is in your PATH.")
        sys.exit(1)

    # Compose command using CH341A programmer by default
    cmd = ["flashrom", "-p", "ch341a_spi"] + sys.argv[1:]
    print("Running:", " ".join(cmd))

    # Execute flashrom command; propagate exit code
    exit_code = subprocess.call(cmd)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
