from settings import *
from random import *
from toucanspritearray import *
enemy_toucan_cards = []
enemy_card_rect = [(505,140),
                   (505,265),
                   (605,155/2),
                   (605,155-95/2+card_height),
                   (605,500-155/2-card_height)]
for enemy_toucan in range(TEAM_SIZE):
    chance = randint(1,100)
    if chance <= 1:
        img = randint(1,2)
    elif chance <= 10:
        img = randint(3,6)
    else:
        img = randint(6,10)
    enemy_toucan_cards.append(img-1)
enemy_damage_bars = [0,0,0,0,0]
enemy_toucan_death = [False,False,False,False,False]

