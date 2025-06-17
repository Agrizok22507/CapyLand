# DISPLAY-BAKLYSHA.py
import pygetwindow as gw
from tkinter import messagebox
import keyboard
import time
import math

##############
## KEYBINDS ##
##############
right_ = "ctrl + right"  # ctrl + стрелка вправо
left_ = "ctrl + left"    # ctrl + стрелка влево
down_ = "ctrl + down"    # ctrl + стрелка вниз
up_ = "ctrl + up"        # ctrl + стрелка вверх
pxpx = 3000
pxpxm = -3000
animation_duration = 0.5  # Длительность анимации в секундах
##############

def get_active_window():
    try:
        return gw.getActiveWindow()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить активное окно: {e}")
        return None

def smooth_move(window, start_x, start_y, end_x, end_y):
    """Плавное перемещение окна с анимацией"""
    steps = 30  # Количество шагов анимации
    for i in range(steps + 1):
        # Квадратичная easing-функция для плавности
        progress = i / steps
        eased_progress = progress * progress  # Ease-in эффект
        
        current_x = start_x + (end_x - start_x) * eased_progress
        current_y = start_y + (end_y - start_y) * eased_progress
        
        try:
            window.moveTo(int(current_x), int(current_y))
        except:
            break
        time.sleep(animation_duration / steps)

def move_window(window, dx=0, dy=0):
    if window is None:
        return
        
    try:
        start_x, start_y = window.left, window.top
        end_x, end_y = start_x + dx, start_y + dy
        
        smooth_move(window, start_x, start_y, end_x, end_y)
        print(f"Окно '{window.title}' перемещено на ({dx}, {dy})")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось переместить окно: {e}")

def right():
    window = get_active_window()
    move_window(window, dx=pxpx)

def left():
    window = get_active_window()
    move_window(window, dx=pxpxm)

def down():
    window = get_active_window()
    move_window(window, dy=pxpx)

def up():
    window = get_active_window()
    move_window(window, dy=pxpxm)

# Регистрация горячих клавиш
keyboard.add_hotkey(right_, right)
keyboard.add_hotkey(left_, left)
keyboard.add_hotkey(down_, down)
keyboard.add_hotkey(up_, up)

print("Display-Baklysha работает... Нажмите Ctrl+C для выхода")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Завершение работы...")
