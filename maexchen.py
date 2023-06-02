import os

from logic import Logic

class Maexchen():

    def __init__(self):
        self.__logic = Logic()

    def play(self):
        while not self.__prompt_play():
            pass

        while True:
            self.__roll_dice()


            self.__clear_console()
            is_reveal = self.__prompt_believe()
            
            if is_reveal:
                pass
                #__prompt_reveal()
                #playagain?

    def __roll_dice(self):
        print("You rolled ", self.__logic.roll_dice())

    def __prompt_play(self):
        return input("Play Maexchen? [y/n]: ").__contains__('y')

    def __prompt_believe(self):
        return input("Believe and roll dice? [y/n]: ").__contains__('y')
        


    def __clear_console(self):
        lambda: os.system("cls")
        lambda: os.system("clear")

maexchen = Maexchen()
maexchen.play()