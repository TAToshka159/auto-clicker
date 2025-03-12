import pyautogui
import keyboard
import time

is_clicking = False

def toggle_clicker():
    global is_clicking
    is_clicking = not is_clicking
    print("Автокликер:", "включен" if is_clicking else "выключен")

keyboard.add_hotkey('ctrl + c', toggle_clicker)

print("Автокликер запущен. Нажмите Ctrl + C для старта/остановки.")
while True:
    if is_clicking:
        pyautogui.click() 
        time.sleep(0.1)    
    time.sleep(0.01)