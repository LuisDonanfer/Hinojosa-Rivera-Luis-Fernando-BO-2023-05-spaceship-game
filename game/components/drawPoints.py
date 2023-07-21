import pygame

from game.utils.constants import FONT_STYLE
class DrawPoints():
    
    def __init__(self, screen):
        self.screen = screen
    
    def draw_message_points(self,message,posX,posY):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(message, False, 'Lime')
        text_rect = text.get_rect(center = (posX, posY))
        self.screen.blit(text, text_rect)

    def draw_score(self,message,posX,posY):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {message}', False, 'White')
        text_rect = text.get_rect(topright = (posX, posY))
        self.screen.blit(text, text_rect)