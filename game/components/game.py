from game.components.drawPoints import DrawPoints
from game.components.menu import Menu
from game.components.bullets.explosion import Explosion
from game.components.enemies.enemyManager import EnemyManager
from game.components.spaceship import Spaceship
from game.components.bullets.bulletManager import BulletManager
from game.components.buttons import  Button
import pygame

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemyManager = EnemyManager()
        self.bulletManager = BulletManager()
        self.explosion = Explosion()
        self.menu = Menu(self.screen)
        self.running = False
        self.death_counter = 0
        self.score = 0
        self.drawPoints = DrawPoints(self.screen)
        self.score_max = 0
        self.button = Button(self.screen)

    
    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
    
    def run(self):
        # Game loop: events - update - draw
        self.bulletManager.reset()
        self.enemyManager.reset()
        self.player.reset()
        self.score = 0
        self.enemyManager.reset()
        self.bulletManager.reset()
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemyManager.update(self)
        self.bulletManager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemyManager.draw(self.screen)
        self.bulletManager.draw(self.screen)
        self.drawPoints.draw_score(self.score,SCREEN_WIDTH - 100, 50)#
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.update(self)
        self.menu.drawImageFondo(self.screen)
        if self.death_counter == 0:
            self.button.drawButtonPlay()
            
        self.menu.drawIcono(self.screen)
        if self.death_counter > 0:
            self.menu.drawGameOver("GAME OVER")
            self.drawPoints.draw_message_points('Your score: ' + str(self.score),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 70)
            
            if self.score > self.score_max:
                self.score_max = self.score
                self.drawPoints.draw_message_points('Highest score: ' + str(self.score),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 105)
            else:
                self.drawPoints.draw_message_points('Highest score: ' + str(self.score_max),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 105)
            self.drawPoints.draw_message_points('Total deaths: ' + str(self.death_counter),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 140)
            self.button.drawButtonRestart()
            self.menu.drawIcono(self.screen)
       

