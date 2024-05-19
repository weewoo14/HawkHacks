import pygame
import pygame.freetype
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
GAME_FONT = pygame.freetype.Font("COMICSANS.TTF", 65)
TURN_FONT = pygame.freetype.Font("COMICSANS.TTF",45)
TEXT_OFFSET = 10

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,158,0)
GRAY = (100,100,100)
LIGHT_GRAY = (160,160,160)
RED = (255,0,0)


TEAM_SIZE = 5

pull_button_x = 250
pull_button_y = 350
pull_button_width = 300
pull_button_height = 85

battle_button_x = 0
battle_button_y = 435
battle_button_width = 65
battle_button_height = 65

pull_button_x2 = 65
pull_button_y2 = 435
pull_button_width2 = 65
pull_button_height2 = 65

team_button_x = 130
team_button_y = 435
team_button_width = 65
team_button_height = 65

card_width = 75
card_height = 95
card_offset = 75
card_offset2 = 62.5

pull_screen = False
combat_screen = False
inventory_screen = False
team_screen = False

NUM_BLUE_TOUCAN_SPRITE = 5
NUM_PURPLE_TOUCAN_SPRITE = 3
NUM_YELLOW_TOUCAN_SPRITE = 2

player_attack_cooldown = 50

def is_collision(mx,my,rx,ry,width,height):
    return mx >= rx and mx <= rx+width and my >= ry and my <= ry+height