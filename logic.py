from dice import Dice

class Logic:
    __last_dice = Dice()
    __current_dice = Dice()
    __statement_dice = Dice()

    def __init__(self):
        pass

    def roll_dice(self):
        self.__last_dice.set_dice(self.__current_dice.get_dice) 

        self.__current_dice.roll()
        print(self.__current_dice)
        
    def reveal(self):
        print("Statement was: %d %d" % (self.__statement_dice[0], self.__statement_dice[1]))
        print(" but dice are:" % (self.__current_dice[0], self.__current_dice[1]))

    def get_last_dice(self):
        return self.__last_dice

    def get_current_dice(self):
        return self.__current_dice

    def get_statement_dice(self):
        return self.__statement_dice
