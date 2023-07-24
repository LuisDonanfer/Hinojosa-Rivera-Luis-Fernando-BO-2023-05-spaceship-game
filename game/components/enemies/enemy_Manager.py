from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_Alien import EnemyAlien
from game.utils.constants import  ENEMY_LIST

class EnemyManager:

    def __init__(self):
        self.enemyImageList = ENEMY_LIST
        self.enemies = []
        self.slow = False

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            if self.slow:
                print("entre lento")
                enemy.SPEED_ON_X =1
                enemy.SPEED_ON_Y = 1
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        self.slow_enemy()
        if len(self.enemies) <len(self.enemyImageList)-1:
            self.enemies.append(EnemyAlien())
            for image in self.enemyImageList:
                enemy = Enemy(image)
                self.enemies.append(enemy)
    def slow_enemy(self, slow = False):
        self.slow = slow

    def reset(self):
        self.enemies = []
    