import pyautogui
import time
from pathlib import Path

# Read the code to be typed
code = Path("code.txt").read_text(encoding="utf-8")

print("Starting in 5 seconds.")
print("Switch to your permitted code editor.")

time.sleep(5)

# Type the code
pyautogui.write(code, interval=0.03)

print("Typing complete.")