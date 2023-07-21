from game.components.menu import Menu
from game.components.bullets.explosion import Explosion
from game.components.enemies.enemyManager import EnemyManager
from game.components.spaceship import Spaceship
from game.components.bullets.bulletManager import BulletManager
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
        self.menu = Menu(self.screen, "hola yufu")
        self.running = False
        self.death_counter = 0
        self.score = 0

    
    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
    
    def run(self):
        # Game loop: events - update - draw
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
        self.draw_score()
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
        self.menu.draw(self.screen)
        self.menu.update(self)
        self.menu.reset_screen(self.screen)
        if self.death_counter > 0:
            self.menu.update_message('Game over')

            icon = pygame.transform.scale((ICON), (80, 120))
            self.screen.blit(icon,(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2))
        self.menu.draw(self.screen)
        self.menu.update(self)

    def increase_deaht_counter(self):
        self.death_counter +=1

    def increase_score(self):
        self.score +=1
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', False, 'White')
        text_rect = text.get_rect(topright = (SCREEN_WIDTH - 100, 50))
        self.screen.blit(text, text_rect)

