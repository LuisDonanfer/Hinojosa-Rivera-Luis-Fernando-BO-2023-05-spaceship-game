from game.utils.constants import RELOF_TYPE, RELOJ
from game.components.power_ups.power_up import PowerUp

class SlowEnemies(PowerUp):
    def __init__(self):
        super().__init__(RELOJ,RELOF_TYPE)