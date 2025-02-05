import requests
import pyautogui
import time
import cv2
import numpy as np

SERVER_URL = "https://match3-bot.onrender.com/get_move"

def get_board_state():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    x_start, y_start, width, height = 100, 200, 600, 600
    game_area = screenshot[y_start:y_start + height, x_start:x_start + width]
    gray = cv2.cvtColor(game_area, cv2.COLOR_BGR2GRAY)
    tile_size = width // 6
    board_state = [[int(np.mean(gray[y:y + tile_size, x:x + tile_size])) for x in range(0, width, tile_size)] for y in range(0, height, tile_size)]
    return board_state

def execute_move(move):
    x1, y1, x2, y2 = move["x1"], move["y1"], move["x2"], move["y2"]
    screen_x1, screen_y1 = 100 + x1 * 50, 200 + y1 * 50
    screen_x2, screen_y2 = 100 + x2 * 50, 200 + y2 * 50
    pyautogui.moveTo(screen_x1, screen_y1)
    pyautogui.dragTo(screen_x2, screen_y2, duration=0.2)

while True:
    board_state = get_board_state()
    response = requests.get(SERVER_URL, params={"board_state": str(board_state)})
    move = response.json()
    execute_move(move)
    time.sleep(1)
