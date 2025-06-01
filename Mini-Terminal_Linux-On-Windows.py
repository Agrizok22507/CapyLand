import os
from rich import print
from rich.panel import Panel
import platform
import datetime

time = datetime.datetime.now()
system = platform.system()
user = os.getlogin()
current_dir = "C:/"
help_ = """
Комманды :

ls       - показать содержимое папки,
cd       - перейти в дирикторию,
pwd      - показать дирикторию, в который вы находитесь,
mkdir    - создать дирикторию,
touch    - создать файл,
cat      - прочитать файл,
clear    - очищает поле,
neofetch - Сообщение neofetch,
uname    - название пользователя,
date     - дата в данный момент,
hi       - приветственное сообщение,
help     - показать список команд
"""
fetch = f"""                                lll         Username: {user}
                    llll,,:;+ccllll         System: {system}
      lll,,+:;  cllllllllllllllllll
,cclllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
                               
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
`'ccllllllllll  lllllllllllllllllll
       `lll*::  :ccllllllllllllllll
                       ````''*::cll
                                 ``"""

def cc():
    global current_dir
    c = input(f"{current_dir}> ")
    split = c.split()
    if not split:
        return
    command = split[0]

    if command == "neofetch":
        print(Panel(f"[blue]{fetch}[/blue]", title="✨ NeoFetch", border_style="green"))
    elif command == "cd":
        add_dir = f"{current_dir}{split[1]}"
        add_dir2 = f"{current_dir}/{split[1]}"
        if os.path.isdir(split[1]):
            current_dir = split[1]
        else:
            if os.path.isdir(add_dir):
                current_dir = add_dir
            else:
                if os.path.isdir(add_dir2):
                    current_dir = add_dir2
                else:
                    print("[bold red]Not found directory[/bold red]")
    elif command == "pwd":
        print(f"[bold orange]{current_dir}[/bold orange]")
    elif command == "clear":
        os.system('cls')
    elif command == "help":
        print(f"[bold violet]{help_}[/bold violet]")
    elif command == "ls":
        items = os.listdir(current_dir)
        print(f"[bold violet]Содержимое {current_dir}:[/bold violet]")
        for item in items:
            print(f"[bold violet]    {item}[/bold violet]")
    elif command == "cat":
        try:
            with open(split[1], 'r') as read:
                rd = read.read()
                print(rd)
        except Exception as e:
            print(f"[bold red]Ошибка: {e}[/bold red]")
    elif command == "touch":
        try:
            with open(split[1], 'w') as file:
                read.write("")
                current_dir = split[1]
        except Exception as e:
            print(f"[bold red]Ошибка: {e}[/bold red]")

    elif command == "go":
        try:
            os.startfile(split[1])
        except Exception as e:
            print(f"[bold red]Ошибка: {e}[/bold red]")
    elif command == "mkdir":
        try:
            os.mkdir(split[1])
        except Exception as e:
            print(f"[bold red]Ошибка: {e}[/bold red]")
    elif command == "uname":
        print(f"[bold violet]Username: {user}[/bold violet]")
    elif command == "date":
        print(f"[bold violet]Time: {time}[/bold violet]")
    elif command == "hi":
        print(f"[bold violet]Привет {user}, Это терминал Linux, но на Windows, ввод не любит пробелов :>[/bold violet]")
    else:
        os.system(c)

while True:
    cc()
