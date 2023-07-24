import pygame
from game.components.bullets.explosion import Explosion

from game.utils.constants import ENEMY_LIST, POINT_EXTRA_TYPE, SHIELD_TYPE

class BulletManager:
    CANT = len(ENEMY_LIST)

    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.list_explosion =[]
        #self.explosion = Explosion()

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner =='enemy':
                self.enemy_bullets.remove(bullet)
                if  game.player.power_up_type != SHIELD_TYPE:
                    game.life_Bar.amount_life -=1
                    if game.life_Bar.amount_life ==0:
                        game.death_counter +=1
                        game.playing = False
                        pygame.time.delay(500)
                        break
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemyManager.enemies:
                if bullet.owner =='player' and bullet.rect.colliderect(enemy):
                    #self.player_bullets.remove(bullet)
                    #self.add_list_explosion(enemy)
                    if game.player.power_up_type == POINT_EXTRA_TYPE:
                       game.points_extra += 5
                    game.enemyManager.enemies.remove(enemy)
                    game.score +=1


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.player_bullets:
            bullet.draw(screen)
        """for explo in self.list_explosion:
            explo.draw(screen)
"""
    """def add_list_explosion(self, spaceship):
        explo = Explosion(spaceship)
        self.list_explosion.append(explo)"""

    def add_bullet(self, bullet):
        if(bullet.owner == 'enemy' and len(self.enemy_bullets) < self.CANT):
            self.enemy_bullets.append(bullet)
        if(bullet.owner == 'player' and len(self.player_bullets) < 20):
            self.player_bullets.append(bullet)

    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []

    