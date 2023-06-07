import pygame
from dice_view import Dice
import const



class Maexchen():
    
    def __init__(self):
        self.init_game_screen()
        self.dice = Dice()

    def init_game_screen(self):
        pygame.init()
        pygame.display.set_caption("Mäxchen")
        self.background_image = pygame.image.load("assets/background.png")
        self.screen = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))
        self.screen.blit(self.background_image, (0, 0))
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.roll_message = font.render("Press SPACEBAR to start rolling.", True, (0, 0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.screen.blit(self.background_image, (0, 0))
                    self.dice.roll(self.screen)
        return True

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.roll_message, (140, 250))
        self.dice.blit_dices(self.screen, 
                             self.dice.get_dice_image(self.dice.first_value), 
                             self.dice.get_dice_image(self.dice.second_value))
        pygame.display.update()

    def run(self):
        running = True
        while running:
            self.clock.tick(const.FPS)
            running = self.handle_events()
            self.draw()

        pygame.quit()

maexchen = Maexchen()
maexchen.run()