import pygame
from game.components.bullets.explosion import Explosion

from game.utils.constants import ENEMY_LIST

class BulletManager:
    CANT = ENEMY_LIST

    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.explosion = Explosion()

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner =='enemy':
                #game.increase_deaht_counter()
                game.death_counter +=1
                game.playing = False
                pygame.time.delay(2000)
                break
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemyManager.enemies:
                if bullet.owner =='player' and bullet.rect.colliderect(enemy):
                    game.enemyManager.enemies.remove(enemy)
                   # game.increase_score()
                    game.score +=1


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if(bullet.owner == 'enemy' and len(self.enemy_bullets) < len(self.CANT)):
            self.enemy_bullets.append(bullet)
        if(bullet.owner == 'player' and len(self.player_bullets) < 20):
            print("si entra")
            self.player_bullets.append(bullet)

    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []

    