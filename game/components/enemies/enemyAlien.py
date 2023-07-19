import pygame
from pygame.sprite import Sprite
import random
from game.utils.constants import ALIEN,SCREEN_HEIGHT, SCREEN_WIDTH

class EnemyAlien(Sprite):
    ENEMY_WIDTH = 140
    ENEMY_HEIGHT = 160
    Y_POS = -(ENEMY_HEIGHT +5)#
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    SPEED_ON_Y = random.randrange(5,10)
    SPEED_ON_X = random.randrange(-2,2)

    def __init__(self):
        self.image = ALIEN
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y
        self.rect.x += self.SPEED_ON_X
        #print("speed x: ", self.rect.x)

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)
            self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
            self.SPEED_ON_Y = random.randrange(5,10)
            self.SPEED_ON_X = random.randrange(-2,2)
            #print("speed x: ", self.SPEED_ON_X)
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)