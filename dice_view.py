import random
import time
import pygame
import const


class Dice:
    def __init__(self) -> None:
        self.init_dice_images()
        self.init_dice_roll_images()
        self.first_value = 1
        self.second_value = 1

    def init_dice_images(self):
        self.dice_images = [ 
                pygame.image.load('assets/dice1.png'),
                pygame.image.load('assets/dice2.png'),
                pygame.image.load('assets/dice3.png'),
                pygame.image.load('assets/dice4.png'),
                pygame.image.load('assets/dice5.png'),
                pygame.image.load('assets/dice6.png')]
        
    def init_dice_roll_images(self):
        self.dice_roll_images = [
                pygame.image.load('assets/roll1.png'),
                pygame.image.load('assets/roll2.png'),
                pygame.image.load('assets/roll3.png'),
                pygame.image.load('assets/roll4.png'),
                pygame.image.load('assets/roll5.png'),
                pygame.image.load('assets/roll6.png'),
                pygame.image.load('assets/roll7.png'),
                pygame.image.load('assets/roll8.png')]

    def roll(self, screen):
        for dice_index in range(1, 8):
            time.sleep(0.1)
            rolling_dice = self.dice_roll_images[dice_index]       
            self.blit_dice_animation(screen, rolling_dice)
        
        self.first_value = random.randint(1, 6)
        self.second_value = random.randint(1, 6)
        first_dice_image = self.dice_images[self.first_value-1]
        second_dice_image = self.dice_images[self.second_value-1]
        self.blit_dices(screen, first_dice_image, second_dice_image)

    def blit_dices(self, screen, first_dice_image, second_dice_image):
        screen.blit(first_dice_image, 
            (200 - first_dice_image.get_height() / 2, 
            const.GAME_HEIGHT / 2 - first_dice_image.get_height() / 2))
        
        screen.blit(
            second_dice_image, 
            (400 - second_dice_image.get_height() / 2, 
            const.GAME_HEIGHT / 2 - second_dice_image.get_height() / 2))

    def blit_dice_animation(self, screen, rolling_dice):
        screen.blit(
                rolling_dice,  
                (200 - rolling_dice.get_height() / 2, 
                const.GAME_HEIGHT / 2 - rolling_dice.get_height() / 2))
            
        screen.blit(rolling_dice, 
                (400 - rolling_dice.get_height() / 2, 
                const.GAME_HEIGHT / 2 - rolling_dice.get_height() / 2))
        
        pygame.display.update()



    def get_dice_image(self, value):
        return self.dice_images[value - 1]
 
