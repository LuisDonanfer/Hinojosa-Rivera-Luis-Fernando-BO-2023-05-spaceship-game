import random
import pygame
from game.components.power_ups.extra_points import ExtraPoints
from game.components.power_ups.multi_shoot import MultiShot
from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart
from game.components.power_ups.slow_enemies import SlowEnemies
from game.utils.constants import BULLET_MULTI_TYPE, HEART_TYPE, POINT_EXTRA_TYPE, RELOF_TYPE

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            if game.player.rect.colliderect(power_up):
                if power_up.type == HEART_TYPE and game.life_Bar.amount_life < 5:
                    game.life_Bar.amount_life +=1
               
                elif power_up.type == BULLET_MULTI_TYPE:
                    game.player.set_image(power_up.type,True)
                    power_up.start_time = pygame.time.get_ticks()# hora de inicio
                    game.player.has_power_up = True
                    game.player.power_up_time_up = power_up.start_time + self.duration #si llega a este tiempo obtenido se acaba el power up
               
                elif power_up.type == POINT_EXTRA_TYPE:
                    power_up.start_time = pygame.time.get_ticks()# hora de inicio
                    game.player.has_power_up = True
                    game.player.power_up_time_up = power_up.start_time + self.duration #si llega a este tiempo obtenido se acaba el power up
                    game.player.set_image(power_up.type)
                else:
                    power_up.start_time = pygame.time.get_ticks()# hora de inicio
                    game.player.has_power_up = True
                    game.player.power_up_time_up = power_up.start_time + self.duration #si llega a este tiempo obtenido se acaba el power up
                    game.player.set_image(power_up.type)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def generate_power_up(self):
        list_random_power_ups = [Shield(),ExtraPoints(),MultiShot(),Heart()]
        power_up = random.choice(list_random_power_ups)
        self.power_ups.append(power_up)   
        self.when_appears += random.randint(5000, 10000)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now +5000, now + 10000)
    
