from settings import *
from random import *
from toucanspritearray import *
from cherished_berries import *
press_pull = False
paid = False
pull_animation_cooldown = 0
amount_of_cb = 1600
def generate_cards():
    cards_rect = []
    for row in range(2):
        for col in range(5):
            chance = randint(1,100)
            if chance <= 1:
                img = randint(1,2)
            elif chance <= 10:
                img = randint(3,6)
            else:
                img = randint(6,10)
            freq[img-1] += 1
            cards_rect.append([sprites[img-1],((col+1)*100+card_offset2,(row+1)*50 + card_offset*row)])
    return cards_rect