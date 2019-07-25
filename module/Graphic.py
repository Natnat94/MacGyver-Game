#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Graphic"""
import os
import pygame


class Graphic:
    """Class of graphic"""
    def __init__(self, win):
        self.win = win

    def draw_bg(self, directory):
        """draw the background in the maze"""
        bg1 = pygame.image.load(os.path.join(directory, "ressource", "floor.png"))
        backg = pygame.Surface(self.win.get_size())
        background = backg.convert()
        background.fill((250, 250, 250))
        for i in range(8):  #Fit the position to scale
            for j in range(30):
                background.blit(bg1, (i*80, j*20), (0, 60, 80, 20))
        self.win.blit(background, (0, 0))

    def draw_tools(self, directory, tool_file, tool_coord):
        """draw the tools in the maze"""
        tool = pygame.image.load(os.path.join(directory, "ressource", tool_file))
        tool = pygame.transform.scale(tool, (40, 40))
        for i in tool_coord:
            tool_coord = [c * 40 for c in i]  #Fit the position to scale
            self.win.blit(tool, tool_coord)

    def draw_walls(self, directory, wall_coord):
        """draw the walls in the maze"""
        wall = pygame.image.load(os.path.join(directory, "ressource", "floor.png")).convert()
        wall1 = pygame.transform.scale2x(wall)
        for i in wall_coord:
            taille = [40, 40]
            new_position = [i[c] * taille[c] for c in range(len(i))]  #fit the position to scale
            self.win.blit(wall1, new_position, (0, 440, 40, 40))

    def draw_cara(self, directory, mac_position):
        """draw the hero in the maze"""
        macgyver1 = pygame.image.load(os.path.join(directory, "ressource", "Macgyver.png"))
        macgyver1 = pygame.transform.scale(macgyver1, (40, 40))
        mac_position = [i * 40 for i in mac_position]  #Fit the position to scale
        self.win.blit(macgyver1, mac_position)

    def draw_guard(self, directory, guard_position):
        """draw the guard in the maze"""
        guard1 = pygame.image.load(os.path.join(directory, "ressource", "Gardien.png"))
        guard1 = pygame.transform.scale(guard1, (40, 40))
        guard_position = [i * 40 for i in guard_position]  #Fit the position to scale
        self.win.blit(guard1, guard_position)
