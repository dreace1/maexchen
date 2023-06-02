import os

from logic import Logic

def clear_console():
    lambda: os.system("cls")
    lambda: os.system("clear")

logic = Logic()
logic.roll_dice()
clear_console