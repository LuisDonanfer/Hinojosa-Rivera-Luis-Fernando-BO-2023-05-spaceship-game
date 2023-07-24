from game.components.draw_Points import DrawPoints
from game.components.life_bar import LifeBar
from game.components.menu import Menu
from game.components.bullets.explosion import Explosion
from game.components.enemies.enemy_Manager import EnemyManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.spaceship import Spaceship
from game.components.bullets.bullet_Manager import BulletManager
from game.components.buttons import  Button
import pygame
from game.utils.constants import BG, FONT_STYLE, ICON, POINT_EXTRA_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


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
        self.menu = Menu(self.screen)
        self.running = False
        self.death_counter = False
        self.score = 0
        self.drawPoints = DrawPoints(self.screen)
        self.score_max = 0
        self.button = Button(self.screen)
        self.power_up_manager = PowerUpManager()
       # self.explosion = Explosion()
        self.points_extra =0
        self.life_Bar = LifeBar()

    
    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
    
    def run(self):
        # Game loop: events - update - draw
        self.life_Bar.amount_life = 5
        self.player.reset()
        self.enemyManager.reset()
        self.bulletManager.reset()
        self.power_up_manager.reset()
        self.score = 0
        self.points_extra = 0
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
        self.power_up_manager.update(self)
        #self.explosion.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemyManager.draw(self.screen)
        self.bulletManager.draw(self.screen)
        self.drawPoints.draw_message_points('Score: '+str(self.score),SCREEN_WIDTH - 100, 50)#
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.life_Bar.draw(self.screen)
        #self.explosion.draw(self.screen)
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
        self.menu.draw_Image_Fondo()
        self.menu.draw_Icono()
        if self.death_counter <= 0:
            self.button.draw_Button_Play()

        else:
            self.menu.draw_Game_Over("GAME OVER")
            self.drawPoints.draw_message_points('Your score: ' + str(self.score),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 80)
            
            if self.score > self.score_max:
                self.score_max = self.score
                self.drawPoints.draw_message_points('Highest score: ' + str(self.score),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 120)
            else:
                self.drawPoints.draw_message_points('Highest score: ' + str(self.score_max),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 120)
            self.drawPoints.draw_message_points('Total deaths: ' + str(self.death_counter),(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 170)
            
            self.button.draw_Button_Restart()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,1)#resta el tiempo del power up menos el tiempo actual                                 #hasta llegar a cero
            if time_to_show >= 0:
                self.drawPoints.draw_message_points('tiempo: ' + str(time_to_show),SCREEN_WIDTH / 2,50)
                if self.player.power_up_type == POINT_EXTRA_TYPE:
                    self.drawPoints.draw_message_points('PONTS EXTRAS: ' + str(self.points_extra),SCREEN_WIDTH / 2,150,'Yellow')
            else:
                self.enemyManager.slow = False
                self.score +=self.points_extra
                self.points_extra = 0
                self.player.has_power_up = False
                self.player.set_image()
