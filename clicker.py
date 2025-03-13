import pyautogui
import keyboard
import time

is_clicking = False
interval = 0.1  

def toggle_clicker():
    global is_clicking
    is_clicking = not is_clicking
    print("Автокликер:", "включен" if is_clicking else "выключен")

def increase_interval():
    global interval
    interval += 0.1
    print("Интервал:", interval)

def decrease_interval():
    global interval
    if interval > 0.1:
        interval -= 0.1
        print("Интервал:", interval)

keyboard.add_hotkey('ctrl + c', toggle_clicker)
keyboard.add_hotkey('ctrl + up', increase_interval)
keyboard.add_hotkey('ctrl + down', decrease_interval)

print("Автокликер запущен. Управление:")
print("- Ctrl + C: старт/стоп")
print("- Ctrl + ↑/↓: изменить интервал")
while True:
    if is_clicking:
        pyautogui.click()
        time.sleep(interval)
    time.sleep(0.01)