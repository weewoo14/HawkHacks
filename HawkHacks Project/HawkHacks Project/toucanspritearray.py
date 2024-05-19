import pygame
from settings import *
pygame.init()
sprites = []
alive_to_death = []
freq = [0,0,0,0,0,0,0,0,0,0]
for toucan_sprite in range(NUM_YELLOW_TOUCAN_SPRITE):
    img = pygame.image.load(f"Toucan Sprites/yellow/yellowSprite{toucan_sprite+1}.png")
    sprites.append(img)
    alive_to_death.append(pygame.image.load(f"Toucan Sprites/dead_yellow/dySprite{toucan_sprite+1}.png"))
for toucan_sprite in range(NUM_PURPLE_TOUCAN_SPRITE):
    img = pygame.image.load(f"Toucan Sprites/purple/purpleSprite{toucan_sprite+1}.png")
    sprites.append(img)
    alive_to_death.append(pygame.image.load(f"Toucan Sprites/dead_purple/dpSprite{toucan_sprite+1}.png"))
for toucan_sprite in range(NUM_BLUE_TOUCAN_SPRITE):
    img = pygame.image.load(f"Toucan Sprites/blue/blueSprite{toucan_sprite+1}.png")
    sprites.append(img)
    alive_to_death.append(pygame.image.load(f"Toucan Sprites/dead_blue/dbSprite{toucan_sprite+1}.png"))

