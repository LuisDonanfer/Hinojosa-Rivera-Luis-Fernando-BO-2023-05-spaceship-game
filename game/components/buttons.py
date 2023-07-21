import pygame
from pygame.sprite import Sprite

from game.utils.constants import BUTTON_PLAY, BUTTON_RESTART, SCREEN_HEIGHT, SCREEN_WIDTH

class Button(Sprite):
    BOTTON_WIDHT = 200
    BOTTON_HEIGHT = 60
    def __init__(self,screen):
        self.screen = screen
        self.imageButtonPlay = BUTTON_PLAY
        self.imageButtonRestart = BUTTON_RESTART
        self.imageButtonPlay = pygame.transform.scale(self.imageButtonPlay,(self.BOTTON_WIDHT, self.BOTTON_HEIGHT))
        self.imageButtonRestart = pygame.transform.scale(self.imageButtonRestart,(self.BOTTON_WIDHT, self.BOTTON_HEIGHT))
        self.rectPlay = self.imageButtonPlay.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.rectRestart = self.imageButtonRestart.get_rect(center = (SCREEN_WIDTH / 2, 230))

    def drawButtonPlay(self):
        self.screen.blit(self.imageButtonPlay, self.rectPlay)
    
    def buttonPlay(self):
        run = False
        pos_mouse = pygame.mouse.get_pos() 
        if self.rectPlay.collidepoint(pos_mouse): 
            if pygame.mouse.get_pressed()[0] : 
                print("start")
                run = True
        return run

    def drawButtonRestart(self):
        self.screen.blit(self.imageButtonRestart, self.rectRestart)

    def buttonRestart(self):
        run = False
        pos_mouse = pygame.mouse.get_pos() 
        if self.rectRestart.collidepoint(pos_mouse): 
            if pygame.mouse.get_pressed()[0]: 
                print("reset")
                run = True
        return run

