import os
import datetime

def clear_console():
    os.system("clear" if os.name == "posix" else "cls")

def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")