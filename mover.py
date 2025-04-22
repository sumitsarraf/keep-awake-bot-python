import pyautogui
import random
import time

pyautogui.FAILSAFE = True  # Keep fail-safe on for emergency stop

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Define a margin to avoid edges
MARGIN = 10
FIVE_SECONDS = 5

while True:
    try:
        # Generate random safe coordinates
        x = random.randint(MARGIN, screen_width - MARGIN)
        y = random.randint(MARGIN, screen_height - MARGIN)

        # Move the mouse
        pyautogui.moveTo(x, y)
        print(f"Cursor moved to: ({x}, {y})")

        # Simulate a shift press
        pyautogui.press('shift')
        print("Shift key pressed.")

    except pyautogui.FailSafeException:
        print("⚠️ Fail-safe triggered! Mouse likely moved to the corner.")
        # Wait a moment before trying again
        time.sleep(2)

    # Wait before repeating
    time.sleep(FIVE_SECONDS)
