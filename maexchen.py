import pygame
import random
from dice import Dice
import const

pygame.init()
screen = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))
clock = pygame.time.Clock()

class Maexchen():
    
    def __init__(self):
        self.dice = Dice()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.dice.roll()
        return True

    def update(self):
        pass

    def draw(self):
        screen.fill(const.WHITE)
        self.dice.draw()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            clock.tick(const.FPS)

            running = self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

maexchen = Maexchen()
maexchen.run()