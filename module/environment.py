#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Environment"""
import random
from .config import SPRITE


class Environment:
    """Classe of Environment"""
    def __init__(self):
        """loading the labyrinth file"""
        self.guardian = []
        self.wall_coord = []
        self.road_coord = []
        self.mac_position = None
        self.objects = []
        self.level = None
        self.names = ["ether.png", "needle.png", "tube.png"]

    def read_file(self, file_to_read):
        """Fonction that read the file and transform it to a list"""
        with open(file_to_read, "r") as text:
            self.level = text.read().splitlines()

    def lab_coord(self, command=False):
        """Fonction that translate draw maze into coordinate"""
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                painting = self.level[i][j]
                if painting == "x":
                    if command: print("/", end="")
                    self.wall_coord.append([(j-1)*SPRITE, (i-1)*SPRITE])
                elif painting == "g":
                    if command: print("g", end="")
                    self.guardian = [(j-1)*SPRITE, (i-1)*SPRITE]
                elif painting == "m":
                    if command: print("m", end="")
                    self.mac_position = [(j-1)*SPRITE, (i-1)*SPRITE]
                else:
                    if command: print("@", end="")
                    self.road_coord.append([(j-1)*SPRITE, (i-1)*SPRITE])
            if command: print()

    def rand_position(self):
        """Fonction that randomly place an object in the maze"""
        object_coord = random.sample(self.road_coord, k=3)
        dico_objects = dict(zip(self.names, object_coord))
        self.objects = dico_objects
        self.road_coord.append(self.guardian)
        self.road_coord.append(self.mac_position)
