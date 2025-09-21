import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT
# C
COLOR_BLUE = (51, 110, 221)
COLOR_ORANGE = (215, 113, 8)
COLOR_YELLOW = (255, 255, 0)

# M
MENU_OPTION = ( 'NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P- COMPETITIVE',
                'SCORE',
                'EXIT')

# K
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                     'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                      'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                     'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 3,
    'Level1Bg3': 2,
}