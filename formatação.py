import time, os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')

def zzz():
    time.sleep(0.5)

def typing(x):
    for i in x:
        print(i, end = "")
        time.sleep(0.03)
    print()

def fas_typing(x):
    for i in x:
        print(i, end = "")
        time.sleep(0.01)
    print()