from settings import *
# Hp, Atk, Spd
player_cards = {1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0],5:[0,0,0]}
player_card_rect = [[(200,375/2-95/2),False],
                    [(200,625/2-95/2),False],
                    [(100,155/2),False],
                    [(100,155 -95/2 + card_height),False],
                    [(100,500-155/2-card_height),False]]
player_card_img = {0:False,
                   1:False,
                   2:False,
                   3:False,
                   4:False}
current_turn = 1
current_select = -1
team_stats = []
player_card_colors = {0:GRAY,1:LIGHT_GRAY}
player_damage_bars = [0,0,0,0,0]
player_toucan_death = [False,False,False,False,False]