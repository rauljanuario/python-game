#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from src.Background import Background
from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.Enemy import Enemy
from src.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1p':
                list_bg = []
                for i in range(2):  # level1bg images number
                    list_bg.append(Background(f'level1p{i}', (0, 0)))
                    list_bg.append(Background(f'level1p{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'level2p':
                list_bg = []
                for i in range(4):  # level2bg images number
                    list_bg.append(Background(f'level2p{i}', (0, 0)))
                    list_bg.append(Background(f'level2p{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('player1', (10, WIN_HEIGHT / 2 - 30))
            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
