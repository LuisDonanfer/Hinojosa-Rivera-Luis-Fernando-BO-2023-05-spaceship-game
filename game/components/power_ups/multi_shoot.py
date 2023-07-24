import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET_MULTI, BULLET_MULTI_TYPE

class MultiShot(PowerUp):
    def __init__(self):
        super().__init__(BULLET_MULTI, BULLET_MULTI_TYPE)