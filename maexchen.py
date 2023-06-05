import pygame
import random
from dice import Dice
import const

pygame.init()
pygame.display.set_caption("Mäxchen")

class Maexchen():
    
    def __init__(self):
        self.init_game_screen()
        self.dice = Dice()

    def init_game_screen(self):
        self.background_image = pygame.image.load("assets/background.png")
        self.screen = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))
        self.screen.blit(self.background_image, (0, 0))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.screen.blit(self.background_image, (0, 0))
                    self.dice.roll2(self.screen)
        return True

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.blit_dice()
        pygame.display.update()

    def blit_dice(self):
        dice_image = self.dice.determine_dice()
        self.screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))

    def run(self):
        running = True
        while running:
            self.clock.tick(const.FPS)
            running = self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

maexchen = Maexchen()
maexchen.run()