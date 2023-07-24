
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import POINT_EXTRA, POINT_EXTRA_TYPE


class ExtraPoints(PowerUp):
     def __init__(self):
        super().__init__(POINT_EXTRA,POINT_EXTRA_TYPE)