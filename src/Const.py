# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'level1p0': 0,
    'level1p1': 1,
    'level2p0': 0,
    'level2p1': 1,
    'level2p2': 2,
    'level2p3': 3,
    'player1': 3,
    'player1shot': 3,
    'enemy1': 1,
    'enemy1shot': 5,
    'enemy2': 1,
    'enemy2shot': 2,
}

ENTITY_HEALTH = {
    'level1p0': 999,
    'level1p1': 999,
    'level2p0': 999,
    'level2p1': 999,
    'level2p2': 999,
    'level2p3': 999,
    'player1': 300,
    'player1shot': 1,
    'enemy1': 50,
    'enemy1shot': 1,
    'enemy2': 60,
    'enemy2shot': 1,
}

ENTITY_DAMAGE = {
    'level1p0': 0,
    'level1p1': 0,
    'level2p0': 0,
    'level2p1': 0,
    'level2p2': 0,
    'level2p3': 0,
    'player1': 1,
    'player1shot': 25,
    'enemy1': 1,
    'enemy1shot': 20,
    'enemy2': 1,
    'enemy2shot': 15,
}

ENTITY_SCORE = {
    'level1p0': 0,
    'level1p1': 0,
    'level2p0': 0,
    'level2p1': 0,
    'level2p2': 0,
    'level2p3': 0,
    'player1': 0,
    'player1shot': 0,
    'enemy1': 100,
    'enemy1shot': 0,
    'enemy2': 125,
    'enemy2shot': 0,
}

ENTITY_SHOT_DELAY = {
    'player1': 20,
    'enemy1': 100,
    'enemy2': 200,
}

# M
MENU_OPTION = ('NEW GAME',
               'SPACE - SHOT',
               'ARROW KEYS - MOVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,}
PLAYER_KEY_SHOOT = {'player1': pygame.K_SPACE,}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
