#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import os

class Graphic:
    def __init__(self):

        self.graphic_mode = graphic_mode
        self.tool_file = tool_file
        self.tool_coord = tool_coord

    def draw_bg(win):
        ### draw the background in the maze ###
        bg1 = pygame.image.load(os.path.join("../ressource","floor.png"))
        backg = pygame.Surface(win.get_size())
        background = backg.convert()
        background.fill((250, 250, 250))
        for i in range(8): #Fit the position to scale
            for c in range(30):
                background.blit(bg1, (i*80,c*20), (0, 60, 80,20))
        win.blit(background, (0, 0))
        #pygame.display.update()

    def draw_tools(win, tool_file, tool_coord):
        ### draw the tools in the maze ###
        tool = pygame.image.load(os.path.join("../ressource",tool_file))
        tool = pygame.transform.scale(tool, (40, 40))
        for i in tool_coord:
            tool_coord = [c * 40 for c in i] #Fit the position to scale
            win.blit(tool, tool_coord)
        #pygame.display.update()

    def draw_walls(win, wall_coord):
        ### draw the walls in the maze ###
        wall = pygame.image.load(os.path.join("../ressource","floor.png")).convert()
        wall1 = pygame.transform.scale2x(wall)
        for i in wall_coord:
            taille = [40, 40]
            new_position = [i[c] * taille[c] for c in range(len(i))] #fit the position to scale
            win.blit(wall1, new_position, (0, 440, 40,40))
        #pygame.display.update()

    def draw_cara(win, mac_position):
        ### draw the hero in the maze ###
        macgyver1 = pygame.image.load(os.path.join("../ressource","Macgyver.png"))
        macgyver1 = pygame.transform.scale(macgyver1, (40, 40))
        mac_position = [i * 40 for i in mac_position] #Fit the position to scale
        win.blit(macgyver1, mac_position)
