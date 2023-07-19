from game.components.enemies.enemy import Enemy
from game.components.enemies.enemyAlien import EnemyAlien
from game.utils.constants import ENEMY_1, ALIEN

class EnemyManager:

    def __init__(self):
        self.enemyImageList = ENEMY_1
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <len(self.enemyImageList)-1:
            self.enemies.append(EnemyAlien())
            for image in self.enemyImageList:
                enemy = Enemy(image)
                self.enemies.append(enemy)