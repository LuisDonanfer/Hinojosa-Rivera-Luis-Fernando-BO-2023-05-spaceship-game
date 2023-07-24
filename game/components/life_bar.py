import pygame

from game.utils.constants import HEART


class LifeBar():
    def __init__(self):
        self.amount_life = 5
        self.heart_image = HEART

    def draw(self,screen):
        pos_x = 50
        screen.blit(self.heart_image,(3,545))
        rectangulo = pygame.Rect(pos_x,550,420,20)
        pygame.draw.rect(screen,'Yellow',rectangulo)
        for index in range(self.amount_life):
            cuadro_rect = pygame.Rect(pos_x,550,100,20)
            pygame.draw.rect(screen,'Red',cuadro_rect)
            pos_x +=80
