from dice_logic import Dice

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
        print("Statement was: ", self.__statement_dice)
        print(" Dice roll is: ", self.__current_dice)

        if self.__statement_dice.get_value() == self.__current_dice.get_value():
            print("You lose!")
        else:
            print("You win!")

    def get_last_dice(self):
        return self.__last_dice

    def get_current_dice(self):
        return self.__current_dice

    def get_statement_dice(self):
        return self.__statement_dice
