import random

class Logic:
    __last_dice = [0, 0]

    def __init__(self):
        pass

    def roll_dice(self):
        for i in range(0,2):
            self.__last_dice[i] = random.randint(1, 6)

    def print_dice(self):
        print("%d %d" % (self.__last_dice[0], self.__last_dice[1]))

logic = Logic()
logic.roll_dice()
logic.print_dice()