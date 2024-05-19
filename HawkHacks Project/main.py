import pygame
import pygame.freetype
from settings import *
from buttons import *
from pulling import *
from time import *
from player import *
from enemy import *
from spritestats import *

pygame.init()
game_window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("TOUCAN GACHA SIMULATOR")
bg = pygame.image.load("background/main_background.png")
cherrished_berry = pygame.image.load("cherrished_berry.png")

game_running = True
while game_running:
    mouse_xpos,mouse_ypos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_collision(mouse_xpos,mouse_ypos,pull_button_x,pull_button_y,pull_button_width,pull_button_height):
                press_pull = True
                pull_animation_cooldown = 0
                cards_rect = generate_cards()
            for key,val in button_dict.items():
                rx,ry,rw,rh = val[0],val[1],val[2],val[3]
                if is_collision(mouse_xpos,mouse_ypos,rx,ry,rw,rh):
                    if key == 1:
                        combat_screen = True
                        pull_screen = False
                        team_screen = False
                    elif key == 2:
                        combat_screen = False
                        pull_screen = True
                        team_screen = False
                    elif key == 3:
                        combat_screen = False
                        pull_screen = False
                        team_screen = True
            if team_screen:
                for idx,info in enumerate(player_card_rect):
                    rect, is_card = info[0],info[1]
                    if is_collision(mouse_xpos,mouse_ypos,rect[0],rect[1],card_width,card_height):
                        current_select = idx
                if current_select != -1:
                    row,col = 1,5
                    for idx,img in enumerate(sprites):
                        if is_collision(mouse_xpos,mouse_ypos,col*100,row*100,card_width,card_height) and freq[idx] > 0:
                            player_card_rect[current_select][1] = True
                            player_card_img[current_select] = idx+1
                        if col*100 >= 700:
                            row += 1
                            col = 5
                        else:
                            col += 1

    game_window.fill(BLACK)
    game_window.blit(bg,(0,0))
    if pull_screen:
        pull_button_img = pull_button_colors[is_collision(mouse_xpos,mouse_ypos,pull_button_x,pull_button_y,pull_button_width,pull_button_height)]
        game_window.blit(pull_button_img,(pull_button_x,pull_button_y))
        if press_pull:
            for img,pos in cards_rect:
                game_window.blit(img,pos)
        GAME_FONT.render_to(game_window,pull_button_text,"PULL",WHITE)
    if combat_screen:
        team_count = 0
        for player_toucan in range(TEAM_SIZE):
            if player_card_img[player_toucan] != False:
                team_count += 1
        for idx,info in enumerate(player_card_rect):
            rect,is_card = info
            if not is_card:
                if current_select == -1 or idx != current_select:
                    player_card_color = player_card_colors[is_collision(mouse_xpos,mouse_ypos,rect[0],rect[1],card_width,card_height)]
                else:
                    player_card_color = player_card_colors[1]
                pygame.draw.rect(game_window,player_card_color,(rect[0],rect[1],card_width,card_height))
            else:
                if player_damage_bars[idx] > 75:
                    player_toucan_death[idx] = True
                    player_damage_bars[idx] = 75
                if player_toucan_death[idx]:
                    game_window.blit(alive_to_death[player_card_img[idx]-1],(rect[0],rect[1]))
                else:
                    game_window.blit(sprites[player_card_img[idx]-1],(rect[0],rect[1]))
                pygame.draw.rect(game_window,GREEN,(rect[0],rect[1]+card_height+3,card_width,5))
                pygame.draw.rect(game_window,RED,(rect[0],rect[1]+card_height+3,player_damage_bars[idx],5))
        for idx,img in enumerate(enemy_toucan_cards):
            x,y = enemy_card_rect[idx][0],enemy_card_rect[idx][1]
            if enemy_damage_bars[idx] > 75:
                enemy_toucan_death[idx] = True
                enemy_damage_bars[idx] = 75
            if enemy_toucan_death[idx]:
                game_window.blit(alive_to_death[img],(x,y))
            else:
                game_window.blit(sprites[img],(x,y))
            pygame.draw.rect(game_window,GREEN,(x,y+card_height+3,card_width,5))
            pygame.draw.rect(game_window,RED,(x,y+card_height+3,enemy_damage_bars[idx],5))
        if team_count == 5 and player_attack_cooldown >= 500:
            for player_toucan in range(TEAM_SIZE):
                if player_damage_bars[player_toucan] < 75:
                    random_enemy = randint(0,4)
                    pspd,patk,php = sprite_stats[player_card_img[player_toucan]-1]
                    espd,eatk,ehp = sprite_stats[enemy_toucan_cards[random_enemy]]
                    enemy_damage_bars[random_enemy] += int(card_width * (patk/ehp))
            for enemy_toucan in range(TEAM_SIZE):
                if enemy_damage_bars[enemy_toucan] < 75:
                    random_player = randint(0,4)
                    espd,eatk,ehp = sprite_stats[enemy_toucan_cards[enemy_toucan]]
                    pspd,patk,php = sprite_stats[player_card_img[random_player]-1]
                    player_damage_bars[random_player] += int(card_width * (eatk/php))
            player_attack_cooldown = 0
    if team_screen:
        TURN_FONT.render_to(game_window,header_text_rect,"Team Maker",WHITE)
        for idx,info in enumerate(player_card_rect):
            rect,is_card = info
            if not is_card:
                if current_select == -1 or idx != current_select:
                    player_card_color = player_card_colors[is_collision(mouse_xpos,mouse_ypos,rect[0],rect[1],card_width,card_height)]
                else:
                    player_card_color = player_card_colors[1]
                pygame.draw.rect(game_window,player_card_color,(rect[0],rect[1],card_width,card_height))
            else:
                game_window.blit(sprites[player_card_img[idx]-1],(rect[0],rect[1]))
        row,col = 1,5
        for idx,img in enumerate(sprites):
            game_window.blit(img,(col*100,row*100))
            TURN_FONT.render_to(game_window,(col*100,row*100,card_width,card_height),str(freq[idx]),WHITE)
            if col*100 >= 700:
                row += 1
                col = 5
            else:
                col += 1
    pygame.draw.line(game_window,GRAY,(SCREEN_WIDTH//2,0),(SCREEN_WIDTH//2,SCREEN_HEIGHT))
    for key,val in button_dict.items():
        rx,ry,rw,rh = val[0],val[1],val[2],val[3]
        img = button_colors[key][is_collision(mouse_xpos,mouse_ypos,rx,ry,rw,rh)]
        game_window.blit(img,(rx,ry))
        TURN_FONT.render_to(game_window,val,button_text[key],WHITE)
    game_window.blit(cherrished_berry,(720,0))
    player_attack_cooldown += 1
    pygame.display.flip()
    
pygame.quit()