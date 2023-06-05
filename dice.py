import random
import time
import pygame
import const


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
        
    def roll(self, screen):
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

    def roll2(self, screen):
        # self.is_rolling = True
        # screen.blit(self.dice_roll_images[0], (250, 150))

        for dice_index in range(1, 8):
            time.sleep(0.1)
            rolling_dice = self.dice_roll_images[dice_index]
            screen.blit(rolling_dice, (const.GAME_WIDTH / 2 - rolling_dice.get_width() / 2, const.GAME_HEIGHT / 2 - rolling_dice.get_height() / 2))
            pygame.display.update()
        
        self.value = random.randint(1, 6)
        dice_image = self.dice_images[self.value-1]
        screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))

        



    #  is_rolling = True
    #     rolling_aud.play()
    #     rand_num = random.randint(0, 5)
    #     dice_num_image = dice_images[rand_num]
    #     screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
    #     rolling_images_counter += 1
    #     first = True

    #     start rolling and calculate dice num
    # else:
    #     if is_rolling:
    #         screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
    #         rolling_images_counter += 1
    #         if rolling_images_counter >= 8:
    #             is_rolling = False
    #             rolling_images_counter = 0

    #     else:
    #         screen.blit(dice_num_image, (250, 150))
    #         if first:
    #             rolling_stop_aud.play()
    #             first = False


    def determine_dice(self):
        if(self.is_rolling):
            #dice_image = 
            return self.dice_roll_images[self.value - 1]
            #screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))
        else:    
            #dice_image = 
            return self.dice_images[self.value - 1]
            #screen.blit(dice_image, (const.GAME_WIDTH / 2 - dice_image.get_width() / 2, const.GAME_HEIGHT / 2 - dice_image.get_height() / 2))