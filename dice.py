import random
import pygame
import const

screen = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))

class Dice:
    def __init__(self) -> None:
        self.init_dice_images()
        self.value = 1

    def init_dice_images(self):
        self.dice_images = [ 
                pygame.image.load('assets/dice1.png'),
                pygame.image.load('assets/dice2.png'),
                pygame.image.load('assets/dice3.png'),
                pygame.image.load('assets/dice4.png'),
                pygame.image.load('assets/dice5.png'),
                pygame.image.load('assets/dice6.png')]
        
    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self):
        dice_image = self.dice_images[self.value - 1]
        screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))