from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_MULTI_TYPE, DEFAULT_TYPE, POINT_EXTRA, POINT_EXTRA_TYPE, RELOF_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, SPACESHIP, SPACESHIP_EXTRA, SPACESHIP_MULTI_SHOOT, SPACESHIP_RELOJ, SPACESHIP_SHIELD
import pygame
from pygame.sprite import Sprite


class Spaceship(Sprite):
    SPACESHIP_WIDHT = 60
    SPACESHIP_HEIGHT = 80
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500

    def __init__(self): 
        self.image_spaceship = {DEFAULT_TYPE:SPACESHIP, SHIELD_TYPE:SPACESHIP_SHIELD, POINT_EXTRA_TYPE:SPACESHIP_EXTRA,
                                BULLET_MULTI_TYPE:SPACESHIP_MULTI_SHOOT, RELOF_TYPE:SPACESHIP_RELOJ}
        self.image = self.image_spaceship[DEFAULT_TYPE]
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDHT, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom =(self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player'
        self.pressed = False
        self.has_power_up = False #tiene poder?
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.active_multi_shoot = False


    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.rect.x -=10
            if self.rect.x < -self.SPACESHIP_WIDHT:
                self.rect.x = SCREEN_WIDTH

        if user_input[pygame.K_RIGHT]: 
            self.rect.x +=10
            if self.rect.x > SCREEN_WIDTH:
                self.rect.x = -self.SPACESHIP_WIDHT


        if user_input[pygame.K_UP] and self.rect.top > 40:
            self.rect.y -=10
            
        if user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y +=10
        if user_input[pygame.K_SPACE] and not self.pressed:
            self.pressed = True
            self.shoot(game.bulletManager)
        elif not user_input[pygame.K_SPACE]:
            self.pressed = False

        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def shoot(self, bulletManager):
        if not self.active_multi_shoot:
            bullet = Bullet(self)
            bulletManager.add_bullet(bullet)
        else:
            separation = -30
            number_bullets = 5
            for i in range(number_bullets):
                bullet = Bullet(self)
                bullet.rect.midbottom = self.rect.center  
                bullet.rect.x += separation
                separation +=70
                bulletManager.add_bullet(bullet)
    
    def reset(self):
        self.rect = self.image.get_rect(midbottom =(self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
    
    def set_image(self,type_image = DEFAULT_TYPE,multi_shoot = False):
        self.active_multi_shoot = multi_shoot
        self.power_up_type = type_image
        self.image = self.image_spaceship[self.power_up_type]
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDHT, self.SPACESHIP_HEIGHT))
