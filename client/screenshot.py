import pyautogui
import time
import os
from config import GAME_REGION

def capture_screenshot():
    screenshot = pyautogui.screenshot(region=GAME_REGION)
    save_path = "screenshots/screen.png"
    
    os.makedirs("screenshots", exist_ok=True)  # Pastikan folder ada
    screenshot.save(save_path)
    
    return save_path

if __name__ == "__main__":
    time.sleep(2)  # Tunggu 2 detik sebelum screenshot
    print("Menyimpan screenshot:", capture_screenshot())
