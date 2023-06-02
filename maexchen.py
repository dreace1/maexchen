import os

from logic import Logic

class Maexchen():

    def __init__(self):
        self.__logic = Logic()

    def play(self):
        self.__logic.roll_dice()
        
        self.__clear_console()

    def __clear_console(self):
        lambda: os.system("cls")
        lambda: os.system("clear")

maexchen = Maexchen()
maexchen.play()