from settings import *

pull_button_rect = (pull_button_x,pull_button_y,pull_button_width,pull_button_height)
pull_button_text = (325,365,100,85)
pull_button_colors = {0:pygame.image.load("pull_button_dark.png"),1:pygame.image.load("pull_button_light.png")}

header_text_rect = (15,15,100,300)

button_dict = {1:(battle_button_x,battle_button_y,battle_button_width,battle_button_height),
               2:(pull_button_x2,pull_button_y2,pull_button_width2,pull_button_height2),
               3:(team_button_x,team_button_y,team_button_width,team_button_height)}
button_text = {1:'M',
               2:'P',
               3:'T'}
bg_dark = pygame.image.load("box_bg.png")
bg_light = pygame.image.load("box_bg_light.png")
button_colors = {1:{0:bg_dark,1:bg_light},
                 2:{0:bg_dark,1:bg_light},
                 3:{0:bg_dark,1:bg_light},
                 4:{0:bg_dark,1:bg_light}}
