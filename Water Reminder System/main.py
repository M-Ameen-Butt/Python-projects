import os
import time
import ctypes
import winsound

REPEAT_INTERVAL = 3  # Repeat frequency in seconds (1 hour)

while True:
    # Play a sound to get attention (optional, but adds a sound reminder)
    winsound.Beep(1000, 1000)  # Frequency, Duration in milliseconds

    # Display a reminder pop-up
    ctypes.windll.user32.MessageBoxW(0, "Hey Ameen Butt, drink water!", "Reminder", 0x40 | 0x1)

    # Wait for the specified interval (1 hour in this case)
    time.sleep(REPEAT_INTERVAL)

