import pygame
from pygame.sprite import Sprite
import random
from game.utils.constants import ALIEN,SCREEN_HEIGHT, SCREEN_WIDTH

class EnemyAlien(Sprite):
    ENEMY_WIDTH = 90
    ENEMY_HEIGHT = 60
    Y_POS = -(ENEMY_HEIGHT +5)
   
    
    def __init__(self):
        self.image = ALIEN
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop =(-100, 200))  
        self.SPEED_ON_X = random.randint(-2,2)
        self.type = 'enemy'

    def update(self, enemies,game):
       
        self.rect.x += game.game_speed 

        if self.rect.top > SCREEN_WIDTH:
            enemies.remove(self)
            
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)