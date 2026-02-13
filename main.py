import pyautogui

def auto_left_click(amount=None):
    if amount:
        for i in range(amount):
            pyautogui.leftClick()
    else:
        pyautogui.leftClick()