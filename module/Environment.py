#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module Environment"""
import random


class Environment:
    """Classe of Environment"""
    def __init__(self):
        """loading the labyrinth file"""
        self.needle = [] #setting the 1st object with null coordinate
        self.ether = [] #setting the 2nd object with null coordinate
        self.tube = [] #setting the 3rd object with null coordinate
        self.guardian = [] #setting the guardian object with null coordinate
        self.wall_coord = [] #setting the walls object with null coordinate
        self.road_coord = [] #setting the roads object with null coordinate
        self.mac_position = [] #setting the hero object with null coordinate
        self.objett = []
        self.level = ""

    def read_file(self, file_to_read):
        """Fonction that read the file and transform it to a list"""
        with open(file_to_read, "r") as text:
            self.level = text.read().splitlines()

    def lab_coord(self):
        """Fonction that translate draw maze into coordinate"""
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                painting = self.level[i][j]
                if painting == "x":
                    print("/", end="")
                    self.wall_coord.append([j, i])
                elif painting == "g":
                    print("g", end="")
                    self.guardian = [j, i]
                elif painting == "m":
                    print("m", end="")
                    self.mac_position = [j, i]
                else:
                    print("@", end="")
                    self.road_coord.append([j, i])
            print()

    def rand_position(self):
        """Fonction that randomly place an object in the maze"""
        object_coord = random.sample(self.road_coord, k=3)
        self.needle = object_coord[0]
        self.ether = object_coord[1]
        self.tube = object_coord[2]
        self.objett = object_coord

def main():
    """main fonction for testing"""
    print("voici le niveau :) ")
    content = Environment()
    content.lab_coord()
    content.rand_position()
    print("voici la position de l'aiguille {}".format(content.needle))
    print("voici la position du tube {}".format(content.tube))
    print("voici la position de l'ether {}".format(content.ether))
    print("voici la position du gardien {}".format(content.guardian))

if __name__ == "__main__":
    main()
