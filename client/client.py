import requests
import pyautogui
import time
import numpy as np
from PIL import ImageGrab
import io

# URL server di Render
SERVER_URL = "https://match3-bot.onrender.com/process"

def capture_screen():
    """Ambil screenshot layar emulator dan kirim ke server"""
    screenshot = ImageGrab.grab()
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

def send_screenshot():
    """Kirim screenshot ke server untuk dianalisis"""
    image_data = capture_screen()
    response = requests.post(SERVER_URL, files={"image": image_data})
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Gagal mendapatkan data dari server.")
        return None

def execute_moves(moves):
    """Jalankan klik otomatis berdasarkan instruksi server"""
    for move in moves:
        x1, y1 = move["from"]
        x2, y2 = move["to"]
        
        pyautogui.moveTo(x1, y1, duration=0.2)
        pyautogui.mouseDown()
        pyautogui.moveTo(x2, y2, duration=0.2)
        pyautogui.mouseUp()

if __name__ == "__main__":
    print("Menjalankan bot...")
    
    while True:
        moves = send_screenshot()
        
        if moves:
            execute_moves(moves)
        else:
            print("Tidak ada langkah tersedia.")

        time.sleep(1)  # Tunggu 1 detik sebelum mengambil screenshot lagi
