import random
import pygame
import const

screen = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))

class Dice:
    def __init__(self) -> None:
        self.init_dice_images()
        self.init_dice_roll_images()
        self.value = 1
        self.is_rolling = False

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
        
    def roll(self, dice_roll_counter):
        self.is_rolling = True
        rolling_images_counter = 0

        if self.is_rolling:
            # showing rolling animation images
            screen.blit(self.dice_roll_images[rolling_images_counter], (250, 150))
            
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                self.is_rolling = False
                self.value=rolling_images_counter
                rolling_images_counter = 0

        else:
            self.value = random.randint(1, 6)


    def draw(self):
        if(self.is_rolling):
            dice_image = self.dice_roll_images[self.value - 1]
            screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))
        else:    
            dice_image = self.dice_images[self.value - 1]
            screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))