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
        self.mac_position = [] #setting the hero variable with null coordinate
        self.objects = []
        self.level = ""
        self.names = ["ether.png", "needle.png", "tube.png"]

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
                    self.wall_coord.append([j-1, i-1])
                elif painting == "g":
                    print("g", end="")
                    self.guardian = [j-1, i-1]
                elif painting == "m":
                    print("m", end="")
                    self.mac_position = [j-1, i-1]
                else:
                    print("@", end="")
                    self.road_coord.append([j-1, i-1])
            print()

    def rand_position(self):
        """Fonction that randomly place an object in the maze"""
        object_coord = random.sample(self.road_coord, k=3)
        dico_objects = dict(zip(self.names, object_coord))
        self.objects = dico_objects


def main():
    """main fonction for testing"""
    print("voici le niveau :) ")
    content = Environment()
    content.lab_coord()
    content.rand_position()
    print("voici la position des objets {}".format(content.objects))

if __name__ == "__main__":
    main()
