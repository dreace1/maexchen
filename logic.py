import random

import const

class Logic:
    __last_dice = [0, 0]
    __last_value = 0

    __current_dice = [0, 0]
    __current_value = 0

    def __init__(self):
        pass

    def roll_dice(self):
        self.__last_dice = self.__current_dice
        self.__last_value = self.__current_value

        for i in range(0,2):
            self.__current_dice[i] = random.randint(1, 6)

        self.__current_dice.sort(reverse=True)

        self.__current_value = self.get_dice_value(self.__current_dice)

    def print_dice(self):
        print("%d %d" % (self.__last_dice[0], self.__last_dice[1]))

    def print_dice_value(self):
        print("Value: %d" % (self.__current_value))


    def get_dice_value(self, dice):
        if self.__is_maexchen(dice):
            return const.VALUE_MAEXCHEN
        
        if self.__is_double(dice):
            return const.VALUE_DOUBLE[dice[0]-1]

        return dice[0] * 10 + dice[1]

    def __is_maexchen(self, dice):
        if dice[0] == 2 and dice[1] == 1:
            return True

    def __is_double(self, dice):
        return dice[0] == dice[1]
    
    
logic = Logic()
logic.roll_dice()
logic.print_dice()
logic.print_dice_value()
