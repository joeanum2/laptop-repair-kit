"""
A simple keyboard tester using pynput.

Run this script from a terminal to capture keystrokes. It will print
each key pressed; press the Escape key to exit.
"""

from pynput import keyboard


def on_press(key: keyboard.Key | keyboard.KeyCode) -> bool | None:
    """Callback invoked when a key is pressed.

    Returns False to stop the listener when Escape is pressed.
    """
    try:
        # Printable keys
        print(f"KEY: {key.char}")
    except AttributeError:
        # Special keys (e.g. shift, ctrl)
        print(f"KEY: {key}")
    # Stop listening on Escape
    if key == keyboard.Key.esc:
        return False
    return None


def main() -> None:
    print("Press keys to test. Press ESC to exit.")
    # Create and start the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
