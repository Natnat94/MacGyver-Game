#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Environment"""
import random


class Environment:
    """Classe of Environment"""
    def __init__(self):
        """loading the labyrinth file"""
        self.guardian = [] #setting the guardian variable with null coordinate
        self.wall_coord = [] #setting the wall variable with null coordinate
        self.road_coord = [] #setting the roads variable with null coordinate
        self.mac_position = None #setting the hero variable with null coordinate
        self.objects = []
        self.level = None
        self.names = ["ether.png", "needle.png", "tube.png"]

    def read_file(self, file_to_read):
        """Fonction that read the file and transform it to a list"""
        with open(file_to_read, "r") as text:
            self.level = text.read().splitlines()

    def lab_coord(self, command = False):
        """Fonction that translate draw maze into coordinate"""
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                painting = self.level[i][j]
                if painting == "x":
                    if command: print("/", end="")
                    self.wall_coord.append([(j-1)*40, (i-1)*40])
                elif painting == "g":
                    if command: print("g", end="")
                    self.guardian = [(j-1)*40, (i-1)*40]
                elif painting == "m":
                    if command: print("m", end="")
                    self.mac_position = [(j-1)*40, (i-1)*40]
                else:
                    if command: print("@", end="")
                    self.road_coord.append([(j-1)*40, (i-1)*40])
            if command: print()

    def rand_position(self):
        """Fonction that randomly place an object in the maze"""
        object_coord = random.sample(self.road_coord, k=3)
        dico_objects = dict(zip(self.names, object_coord))
        self.objects = dico_objects
        self.road_coord.append(self.guardian)
        self.road_coord.append(self.mac_position)
