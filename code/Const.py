# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_LIGHT_GREEN = (150, 255, 150)
C_LIGHT_CYAN = (150, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy3': 4,
}

ENTITY_HEALTH = {
    '1': 999,
    '2': 999,
    '3': 999,
    '4': 999,
    '5': 999,
    '6': 999,
    '7': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 10,
    'Player1Shot': 1,
    'Player2': 10,
    'Player2Shot': 1,
    'Enemy1': 125,
    'Enemy3': 50,
}

ENTITY_DAMAGE = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy3': 1,
}


ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
}

# M
MENU_OPTION = ('COMEÇAR JOGO',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_SPACE}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 120000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
GROUND_Y = WIN_HEIGHT - 30

# Player Animations
PLAYER_ANIMATION = {
    'Player1': {
        'Idle': 'Walk',
        'Walk': 'Walk',
        'Attack': 'Shot',
        'Jump': 'Jump',
        'Dead': 'Dead'
    },
    'Player2': {
        'Idle': 'Walk',
        'Walk': 'Walk',
        'Attack': 'Shot',
        'Jump': 'Jump',
        'Dead': 'Dead'
    }
}

ENEMY_ANIMATION = {
    'Enemy1': {
        'Walk': 'enemyWalk',
        'Attack1': 'enemyAttack1',
        'Attack2': 'enemyAttack2',
        'Dead': 'enemyDeath'
    },
    'Enemy3': {
        'Walk': 'enemyRun',
        'Dead': 'DeadEnemy3'
    }
}

