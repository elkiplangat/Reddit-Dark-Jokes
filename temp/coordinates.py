import pyautogui

while True:
    x, y = pyautogui.position()
    print(f'x: {x}')
    print(f'y: {y}')