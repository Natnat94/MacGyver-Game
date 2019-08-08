#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Graphic"""
import os
import pygame


class Graphic:
    """Class of graphic"""
    def __init__(self, win, directory):
        self.win = win
        self.directory = directory

    def _load_image(self, picture):
        image = pygame.image.load(os.path.join(self.directory, "ressource", picture))
        image = pygame.transform.scale(image, (40, 40))
        return image

    def draw_bg(self):
        """draw the background in the maze"""
        bg1 = pygame.image.load(os.path.join(self.directory, "ressource", "floor.png"))
        backg = pygame.Surface(self.win.get_size())
        background = backg.convert()
        background.fill((250, 250, 250))
        for i in range(8):  #Fit the position to scale
            for j in range(30):
                background.blit(bg1, (i*80, j*20), (0, 60, 80, 20))
        self.win.blit(background, (0, 0))

    def draw_tools(self, tool_coord):
        """draw the tools in the maze"""
        for key, value in tool_coord.items():
            self.win.blit(self._load_image(key), value)

    def draw_walls(self, wall_coord):
        """draw the walls in the maze"""
        wall = pygame.image.load(os.path.join(self.directory, "ressource", "floor.png")).convert()
        wall1 = pygame.transform.scale2x(wall)
        for i in wall_coord:
            self.win.blit(wall1, i, (0, 440, 40, 40))

    def draw_cara(self, mac_position):
        """draw the hero in the maze"""
        self.win.blit(self._load_image("Macgyver.png") , mac_position)

    def draw_guard(self, guard_position):
        """draw the guard in the maze"""
        self.win.blit(self._load_image("Gardien.png"), guard_position)

    def draw_win(self):
        """draw a win text"""
        winner = pygame.image.load(os.path.join(self.directory, "ressource", "trophy.png")) # mettre une variable pour le cas de perdu
        background = pygame.Surface(self.win.get_size())
        background = background.convert()
        winner = pygame.transform.scale(winner, (600, 600))
        background.blit(winner, (0, 0))
        if pygame.font:
            font = pygame.font.Font(None, 42)
            text = font.render("Congratulations you saved him !!!", 1, (10, 10, 10)) # mettre le message en variable pour le cas de perdu
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos = textpos.move(0, 50)
            background.blit(text, textpos)
        self.win.blit(background, (0, 0))
        pygame.display.flip()

    def draw_lose(self):
        """draw a lose text"""
        winner = pygame.image.load(os.path.join(self.directory, "ressource", "gameover.png")) # mettre une variable pour le cas de perdu
        background = pygame.Surface(self.win.get_size())
        background = background.convert()
        winner = pygame.transform.scale(winner, (600, 600))
        background.blit(winner, (0, 0))
        self.win.blit(background, (0, 0))
        pygame.display.flip()
