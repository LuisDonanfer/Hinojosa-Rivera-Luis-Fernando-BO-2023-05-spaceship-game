from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP
import pygame
from pygame.sprite import Sprite


class Spaceship(Sprite):
    SPACESHIP_WIDHT = 60
    SPACESHIP_HEIGHT = 80
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDHT, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom =(self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player'


    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.rect.x -=10
            if self.rect.x < -self.SPACESHIP_WIDHT:
                self.rect.x = SCREEN_WIDTH

        elif user_input[pygame.K_RIGHT]: 
            self.rect.x +=10
            if self.rect.x > SCREEN_WIDTH:
                self.rect.x = -self.SPACESHIP_WIDHT


        elif user_input[pygame.K_UP] and self.rect.top > 40:
            self.rect.y -=10
            
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y +=10
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)