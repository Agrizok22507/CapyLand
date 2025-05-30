# Capynux.py
import os
from datetime import *
import time
import shutil

time = datetime.now()
current_dir = "C:/Users/"
capybara = """.--^*^--.
( o v o )
(           )
  vv     vv
"""
user = os.getlogin()
dekstop = "C:/Users/" + user + "/Desktop/comands.txt"
help_ = """
ls - показать содержимое папки
cd - перейти в дирикторию
pwd - показать дирикторию, в который вы находитесь
mkdir - создать дирикторию
touch - создать файл
cp - копировать файл/папку
mv - переместить файл/папку
rm - удалить файл/папку
find - найти файл/папку
cat - прочитать файл
uname - название пользователя
date - дата в данный момент
history - история команд
chmod - изменение прав файла
exp - открыть проводник
calc - открыть калькулятор
pwrshl - команда в powershell
cmd - команда в cmd
hi - приветственная надпись
capy - капибара
help - показать список команд
"""

def do(cmd):
    global current_dir
    if cmd == "help":
        print(help_)
    elif cmd == "hi": 
        print(f"Привет {user}, я Капинукс - терминал линукса, но на windows")
        print("Здесь не все команды, возможно я добавлю их, но всё равно я старался :3")
    elif cmd == "capy":
        print(capybara)
    elif cmd == "pwd":
        print(f"Вы находитесь в : {current_dir}")
    elif cmd == "cd":
        new_dir = input("Введите путь: ").strip()
        if os.path.isdir(new_dir):
            current_dir = new_dir
        else:
            print(f"Ошибка: Директория '{new_dir}' не существует!")
    elif cmd == "ls":
        items = os.listdir(current_dir)
        print(f"Содержимое {current_dir}:")
        for item in items:
            print(f"  - {item}")
    elif cmd == "cmd":
        c = input("    > ")
        os.system(c)
    elif cmd == "pwrshl":
        p = input("    > ")
        os.system(f"powershell {p}")
    elif cmd == "history":
        try:
            with open(dekstop, "r") as f:
                rr = f.read()
                history = f"""History:
                {rr}"""
                print(history)
        except Exception as e:
            print(f"Ошибка : {e}")
    elif cmd == "exp":
        os.system("explorer.exe")
    elif cmd == "calc":
        os.system("calc.exe")
    elif cmd == "mkdir":
        dir_ = input("    > ")
        if "/" not in dir_:
            diir = f"{current_dir}/{dir_}"
            os.mkdir(diir)
        else:
            os.mkdir(dir_)
    elif cmd == "touch":
        t = input("    > ")
        if t == "":
            t = current_dir
        with open(t, "w") as tt:
            tt.write("")
        current_dir = t
    elif cmd == "uname":
        print(user)
    elif cmd == "cat":
        cc = input("    > ")
        if cc == "":
            cc = current_dir
        with open(cc, "r") as ccc:
            cccc = ccc.read()
            print(cccc)
    elif cmd == "date":
        print(time)
    elif cmd == "cp":
        cp = input("    > ")
        if cp == "":
            cp = current_dir
        cpp = input("     to> ")
        if os.path.isdir(cp):
            try:
                shutil.copytree(cp, cpp)
            except Exception as e:
                print(f"Error : {e}")
        else:
            try:
                shutil.copy2(cp, cpp)
            except Exception as e:
                print(f"Error : {e}")
    elif cmd == "mv":
        mv = input("    > ")
        if mv == "":
            mv = current_dir
        mvv = input("     to> ")
        try:
            shutil.move(mv, mvv)
        except Exception as e:
            print(f"Error : {e}")
    elif cmd == "rm":
        rm = input("    > ")
        if rm == "":
            rm = current_dir
        yn = input(f"Are you sure delete {rm}(y/n)?: ")
        if yn == "y":
            print(f"{rm} be deleted after 5 seconds...")
            time.sleep(5)
            try:
                os.remove(rm)
            except Exception as e:
                print(f"Error : {e}")
        elif yn == "n":
            print("Ok...")
        else:
            print("Incorrect comand...") 
    elif cmd == "find":
        find = input("    > ")
        print("Возможно вы устонавили устаревшую версию, посмотрите на сайте откуда вы скачали на наличее обновления(возможно я до сих пор не добавил эту функцию -\_(^.^)_/-)")
    elif cmd == "chmod":
        ch = input("    > ")
        if ch == "":
            ch = current_dir
        mod = input("    mod> ")
        try:
            os.chmod(ch, mod)
        except Exception as e:
            print(f"Error : {e}")
    else:
        print("Неизвестная команда...")

while True:
    user_input = input(f"{user}/{current_dir}> ").strip()
    do(user_input)
    try:
        with open(dekstop, "a")as f:
            f.write(f"{user_input}\n")
    except Exception as e:
        print(f"Ошибка : {e}")
