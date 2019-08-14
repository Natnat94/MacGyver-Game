#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Graphic"""
import os
import pygame
from .config import SPRITE


class Graphic:
    """Class of graphic"""
    def __init__(self, win, directory):
        self.win = win
        self.directory = directory

    def _load_image(self, picture):
        """load the image of the game"""
        image = pygame.image.load(os.path.join(self.directory, "ressource",
                                               picture))
        return image

    def draw_bg(self, road_coord):
        """draw the background of the maze"""
        image = pygame.transform.scale2x(self._load_image("floor.png"))
        for i in road_coord:
            self.win.blit(image, i, (400, 40, 40, 40))

    def draw_walls(self, wall_coord):
        """draw the walls of the maze"""
        image = pygame.transform.scale2x(self._load_image("floor.png"))
        for i in wall_coord:
            self.win.blit(image, i, (480, 440, 40, 40))

    def draw_cara(self, mac_position):
        """draw the hero into the maze"""
        image = pygame.transform.scale(self._load_image
                                       ("Macgyver.png"), (SPRITE, SPRITE))
        self.win.blit(image, mac_position)

    def draw_guard(self, guard_position):
        """draw the guard into the maze"""
        image = pygame.transform.scale(self._load_image
                                       ("Gardien.png"), (SPRITE, SPRITE))
        self.win.blit(image, guard_position)

    def draw_tools(self, tool_coord):
        """draw the tools into the maze"""
        for key, value in tool_coord.items():
            image = pygame.transform.scale(self._load_image
                                           (key), (SPRITE, SPRITE))
            self.win.blit(image, value)

    def draw_win(self, picture):
        """draw a win or lose picture"""
        image = pygame.transform.scale(self._load_image(picture), (600, 600))
        self.win.blit(image, (0, 0))

    def draw_counter(self, obj_count):
        """draw an object counter text"""
        pygame.draw.rect(self.win, (150, 150, 150), (0, 600, 600, SPRITE))
        if pygame.font:
            font = pygame.font.Font(None, 42)
            msg = "Vous avez {} objet(s) sur vous".format(obj_count)
            text = font.render(msg, 1, (10, 10, 10))
            textpos = text.get_rect(centerx=self.win.get_width()/2)
            textpos = textpos.move(0, 605)
            self.win.blit(text, textpos)
        self.win.blit(self.win, (0, 0))
