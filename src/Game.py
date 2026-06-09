#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_RED, C_WHITE
from src.Level import Level
from src.Menu import Menu
from src.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)
                
                if not level_return:
                    self.show_game_over_screen()

            elif menu_return == MENU_OPTION[1] or menu_return == MENU_OPTION[2]:
                pass
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()

    def show_game_over_screen(self):
        
        pygame.mixer_music.load('./assets/menu.ogg')
        pygame.mixer_music.play(-1)
        
        self.window.fill((0, 0, 0)) 
        
        font_title = pygame.font.SysFont('Arial', 60, bold=True)
        font_text = pygame.font.SysFont('Arial', 24)
      
        title_surf = font_title.render('GAME OVER', True, C_RED) 
        text_surf = font_text.render('Press any key to return to the menu.', True, C_WHITE) 
        
        title_rect = title_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30))
        text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 40))
        
        self.window.blit(title_surf, title_rect)
        self.window.blit(text_surf, text_rect)
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: 
                    waiting = False
