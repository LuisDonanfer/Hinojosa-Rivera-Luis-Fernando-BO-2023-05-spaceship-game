import pygame
from game.components.buttons import Button
from game.utils.constants import FONDO_INICIO, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDHT = SCREEN_WIDTH / 2
    
    def __init__(self, screen):
        self.screen = screen
        self.imageFondo = FONDO_INICIO
        self.imageFondo = pygame.transform.scale(self.imageFondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.imageFondo.get_rect(topleft = (0,0))
        self.button = Button(screen)
        
        self.icon = ICON
        self.icon = pygame.transform.scale((ICON), (80, 120))
        self.rectIcon = self.icon.get_rect(center = (SCREEN_WIDTH /2, (SCREEN_HEIGHT / 2) - 180))

    def update(self, game):
        pygame.display.update()
        self.handle_events(game)
    
    def drawGameOver(self,message):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(message, False, 'Purple')
        text_rect = text.get_rect(center = ((SCREEN_WIDTH /2), (SCREEN_HEIGHT / 2)))
        self.screen.blit(text, text_rect)



    def updateIcon(self):
        self.rectIcon.x +=1    
        if(self.rectIcon.left > (SCREEN_WIDTH /2) + 100 ) :
            self.rectIcon.x -=1
        if self.rectIcon.left < 100 :
            self.rectIcon.x +=1

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
        if self.button.buttonPlay() or self.button.buttonRestart():
            game.run()

    def drawImageFondo(self, screen):
        screen.blit(self.imageFondo, self.rect)

    def update_message(self, message):
        self.text = self.font.render(message, False, 'Black')
        self.text.get_rect(center = (self.SCREEN_HALF_WIDHT, self.SCREEN_HALF_HEIGHT))

    def drawIcono(self,screen):
        screen.blit(self.icon,self.rectIcon)


