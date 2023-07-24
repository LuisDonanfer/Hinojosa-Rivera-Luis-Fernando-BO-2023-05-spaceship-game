import pygame
from pygame.sprite import Sprite

from game.utils.constants import EXPLOSION_LIST

class Explosion(Sprite):
    def __init__(self,spaceship):
        self.center_s = spaceship.center_nave
        self.index = 0

    def update(self):
        self.image = EXPLOSION_LIST[0]
        self.image = pygame.transform.scale(image,(60, 80))
        self.rect = image.get_rect(center = (self.center_s))
        image = EXPLOSION_LIST[0] if self.index < 5 else EXPLOSION_LIST[1]
        self.index +=1
        if self.index >= 10:
            self.index = 0
    def draw(self,screen):
         pass#screen.blit(image,rect)
    
        
            
