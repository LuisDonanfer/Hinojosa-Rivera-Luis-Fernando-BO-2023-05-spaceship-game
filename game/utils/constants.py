import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

POINT_EXTRA  = pygame.image.load(os.path.join(IMG_DIR, "Other/point_extra.png"))
RELOJ = pygame.image.load(os.path.join(IMG_DIR, "Other/reloj.png")) 
BULLET_MULTI = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bala_multiple.png"))

POINT_EXTRA_TYPE = 'point'
DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
RELOF_TYPE = 'reloj'
BULLET_MULTI_TYPE = 'multi'
HEART_TYPE = "heart"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_EXTRA = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_extra.png"))
SPACESHIP_MULTI_SHOOT = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_multi_shoot.png"))
SPACESHIP_RELOJ = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_reloj.png"))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart1.png'))

ENEMY_LIST = [pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png")),
           #pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png")),
           #pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))
           ]
EXPLOSION_LIST= [pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex1.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex2.png"))            
             ]


BUTTON_PLAY = pygame.image.load(os.path.join(IMG_DIR, 'Other/buttonPlay.png'))
BUTTON_RESTART = pygame.image.load(os.path.join(IMG_DIR, 'Other/buttonRestart.png'))

FONDO_INICIO = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondo_gta.png'))


ALIEN = pygame.image.load(os.path.join(IMG_DIR, "Enemy/alien.png"))

FONT_STYLE = 'freesansbold.ttf'
