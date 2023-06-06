import random 

import const

class Dice:
    def __init__(self):
        self.__dice = [0,0]

    def __str__(self):
        return "%d %d" % (self.__dice[0], self.__dice[1])

    def roll(self):
        for i in range(0,2):
            self.__dice[i] = random.randint(1, 6)

        self.__dice.sort(reverse=True)
        
    def get_value(self):
        if self.__is_maexchen(self.__dice):
            return const.VALUE_MAEXCHEN
        
        if self.__is_double(self.__dice):
            return const.VALUE_DOUBLE[self.__dice[0]-1]

        return self.__dice[0] * 10 + self.__dice[1]
    
    def __is_maexchen(self, dice):
        if dice[0] == 2 and dice[1] == 1:
            return True

    def __is_double(self, dice):
        return dice[0] == dice[1]

    def get_dice(self):
        return self.__dice
    
    def set_dice(self, dice):
        self.__dice = dice
