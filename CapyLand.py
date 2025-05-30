# CapyLand.py
import win32gui
import win32con
import win32api
from tkinter import *
import time
import keyboard
import os

# Глобальные переменные
root = Tk()
transparency = 1.0
user = os.getlogin()
current_num_of_windows = 0  # Инициализируем счетчик окон

##############
### CONFIG ###
##############
cmd = "ctrl + g"
def cmd_():
    os.startfile("C:/Users/" + user + "/Desktop/Capynux.py") 
    time.sleep(2)
    reload()
##############

def start():
    root.geometry("425x60")
    root.overrideredirect(True)
    root.attributes('-alpha', transparency)
    root['bg'] = 'black'

    t = Label(text="Welcome to CapyLand", font="Arial 30", bg='black', fg='white')
    t.pack()

    def fade_out():
        global transparency
        if transparency > 0:
            transparency -= 0.01
            root.attributes('-alpha', transparency)
            print(f"Прозрачность: {transparency:.2f}")
            root.after(20, fade_out)
        else:
            root.destroy()

    root.after(500, fade_out)
    root.mainloop()

def is_real_app_window(hwnd):
    """Проверяет, является ли окно обычным приложением"""
    if not win32gui.IsWindowVisible(hwnd):
        return False
    
    # Исключаем окна без заголовка
    title = win32gui.GetWindowText(hwnd)
    if not title:
        return False
    
    # Исключаем служебные окна Windows
    className = win32gui.GetClassName(hwnd)
    if className in ["Shell_TrayWnd", "Progman", "WorkerW", "Windows.UI.Core.CoreWindow"]:
        return False
    
    # Исключаем окна без рамки (типа всплывающих подсказок)
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    if not (style & win32con.WS_OVERLAPPEDWINDOW):
        return False
    
    # Исключаем свернутые окна
    if win32gui.IsIconic(hwnd):
        return False
    
    false_titles = ["Параметры", "Медиаплеер", "Калькулятор", "Microsoft Text Input Application", "Проводник", "TextInputHost", "Calculator", "Application Frame Host", "Microsoft"] # Проверка на системные приложения(у вас названия могут отличатся)
    if title in false_titles:
        return False

    return True

def get_app_windows():
    """Получает список окон только обычных приложений"""
    windows = []
    
    def callback(hwnd, hwnds):
        if is_real_app_window(hwnd):
            hwnds.append((hwnd, win32gui.GetWindowText(hwnd)))
        return True
    
    win32gui.EnumWindows(callback, windows)
    
    # Сортируем по Z-порядку (последние использованные - первые)
    windows.sort(key=lambda x: win32gui.GetWindowRect(x[0])[0], reverse=True)
    return [hwnd for hwnd, title in windows]
def split_windows(windows):
    """Распределяет окна по экрану с поддержкой до 10 окон"""
    if not windows:
        print("Нет окон для управления")
        return
    
    count = len(windows)
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    
    print(f"Управление {count} окнами:")
    for i, hwnd in enumerate(windows):
        title = win32gui.GetWindowText(hwnd)[:50]  # Обрезаем длинные названия
        print(f"{i+1}. {title}{'...' if len(title) >= 50 else ''}")
        
        try:
            # 1 окно - полный экран
            if count == 1:
                x, y, w, h = 0, 0, screen_width, screen_height
            
            # 2 окна - горизонтально пополам
            elif count == 2:
                w = screen_width // 2
                h = screen_height
                x = w * i
                y = 0
            
            # 3 окна - одно слева (50%), два справа (вертикально)
            elif count == 3:
                if i == 0:  # Левое окно
                    x, y = 0, 0
                    w = screen_width // 2
                    h = screen_height
                else:  # Правые окна
                    x = screen_width // 2
                    w = screen_width // 2
                    h = screen_height // 2
                    y = h * (i - 1)
            
            # 4 окна - сетка 2x2
            elif count == 4:
                w = screen_width // 2
                h = screen_height // 2
                x = w * (i % 2)
                y = h * (i // 2)
            
            # 5 окон - верхний ряд (3), нижний (2)
            elif count == 5:
                if i < 3:  # Верхний ряд
                    w = screen_width // 3
                    h = screen_height // 2
                    x = w * i
                    y = 0
                else:  # Нижний ряд
                    w = screen_width // 2
                    h = screen_height // 2
                    x = w * (i - 3)
                    y = screen_height // 2
            
            # 6 окон - 2 ряда по 3
            elif count == 6:
                w = screen_width // 3
                h = screen_height // 2
                x = w * (i % 3)
                y = h * (i // 3)
            
            # 7 окон - верх (4), низ (3)
            elif count == 7:
                if i < 4:  # Верхний ряд
                    w = screen_width // 4
                    h = screen_height // 2
                    x = w * i
                    y = 0
                else:  # Нижний ряд
                    w = screen_width // 3
                    h = screen_height // 2
                    x = w * (i - 4)
                    y = screen_height // 2
            
            # 8 окон - 2 ряда по 4
            elif count == 8:
                w = screen_width // 4
                h = screen_height // 2
                x = w * (i % 4)
                y = h * (i // 4)
            
            # 9 окон - 3 ряда по 3
            elif count == 9:
                w = screen_width // 3
                h = screen_height // 3
                x = w * (i % 3)
                y = h * (i // 3)
            
            # 10 окон - верх (4), середина (3), низ (3)
            elif count == 10:
                if i < 4:  # Верхний ряд
                    w = screen_width // 4
                    h = screen_height // 3
                    x = w * i
                    y = 0
                elif i < 7:  # Средний ряд
                    w = screen_width // 3
                    h = screen_height // 3
                    x = w * (i - 4)
                    y = screen_height // 3
                else:  # Нижний ряд
                    w = screen_width // 3
                    h = screen_height // 3
                    x = w * (i - 7)
                    y = 2 * (screen_height // 3)
            
            # Применяем размеры
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetWindowPos(
                hwnd, win32con.HWND_TOP, 
                x, y, w, h,
                win32con.SWP_SHOWWINDOW | win32con.SWP_NOZORDER
            )
            
        except Exception as e:
            print(f"Ошибка с окном '{title}': {str(e)[:100]}")

def reload():
    global current_num_of_windows  # Добавляем global
    print("Поиск окон приложений...")
    app_windows = get_app_windows()
    if not app_windows:
        print("Не найдено подходящих окон приложений")
    else:
        current_num_of_windows = len(app_windows)  # Обновляем счетчик
        print(f"Найдено окон: {current_num_of_windows}")
        for i, hwnd in enumerate(app_windows):
            print(f"{i+1}. {win32gui.GetWindowText(hwnd)}")
        
        split_windows(app_windows[:10])

def check_new_windows():
    global current_num_of_windows  # Добавляем global
    app_windows = get_app_windows()
    new_count = len(app_windows)
    
    if new_count != current_num_of_windows:
        print(f"Обнаружено изменение: было {current_num_of_windows}, стало {new_count}")
        current_num_of_windows = new_count  # Обновляем счетчик
        reload()
    else:
        print(f"Изменений нет (окон: {current_num_of_windows})")
    
    return current_num_of_windows

if __name__ == "__main__":
    start()
    reload()  # Инициализируем счетчик при старте
    try:
        keyboard.add_hotkey(cmd, cmd_)
    except Exception as e:
        print(f"Ошибка регистрации горячей клавиши: {e}")
    
    while True:
        check_new_windows()
        time.sleep(1)  # Проверяем каждую секунду
