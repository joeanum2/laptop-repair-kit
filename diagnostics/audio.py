"""
Audio loopback diagnostic.

This script plays a 1 kHz tone via your default audio output device
for one second, then records three seconds of audio from your default
microphone. It computes and prints the RMS of the recorded signal to
give a rough indication of microphone sensitivity and speaker output.

Requires the `sounddevice` and `numpy` libraries. On some platforms you
may need additional backend packages (e.g. PortAudio on Linux).
"""

import numpy as np
import sounddevice as sd


def main() -> None:
    sample_rate = 44100  # Samples per second
    # Generate a 1 kHz sine wave tone for one second
    t = np.linspace(0, 1, sample_rate, False)
    tone = np.sin(2 * np.pi * 1000 * t) * 0.3  # Scaled to avoid clipping

    print("Playing 1 kHz test tone...")
    sd.play(tone, sample_rate)
    sd.wait()  # Wait for playback to finish

    # Record from microphone
    record_seconds = 3
    print(f"Recording from microphone for {record_seconds} seconds...")
    rec = sd.rec(int(record_seconds * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Calculate RMS level of the recording
    rms = float(np.sqrt(np.mean(np.square(rec))))
    print(f"Recorded RMS: {rms:.3f}")


if __name__ == "__main__":
    main()
