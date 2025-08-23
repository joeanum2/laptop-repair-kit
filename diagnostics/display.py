"""
Display diagnostic test using pygame.

When executed, this script opens a fullscreen window and cycles through
several solid colours (black, white, red, green, blue). Each colour is
shown for two seconds to help identify dead pixels, uniformity issues
or colour casting problems on laptop displays. Close the window or
interrupt the script to exit.
"""

import pygame
import time


def main() -> None:
    # Initialise pygame and create a fullscreen window
    pygame.init()
    try:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        colours = [
            (0, 0, 0),        # Black
            (255, 255, 255),  # White
            (255, 0, 0),      # Red
            (0, 255, 0),      # Green
            (0, 0, 255),      # Blue
        ]
        # Cycle through colours
        for colour in colours:
            screen.fill(colour)
            pygame.display.flip()
            print(f"Displaying colour: {colour}")
            time.sleep(2)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
