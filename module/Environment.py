#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Environment:

    def __init__ (self):
    ### loading the labyrinth file ###
        self.needle = [] #setting the 1st object with null coordinate
        self.ether = [] #setting the 2nd object with null coordinate
        self.tube = [] #setting the 3rd object with null coordinate
        self.guardian = [] #setting the guardian object with null coordinate
        self.wall_coord = [] #setting the walls object with null coordinate
        self.road_coord = [] #setting the roads object with null coordinate

    def lab_coord (self, level):
        ### Fonction that translate draw maze into coordinate ###
        self.level = level
        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                painting = level [y][x]
                #print(x,y)
                if painting == "x":
                    print("/", end="")
                    self.wall_coord.append([x,y])
                elif painting == "g":
                    print("g", end="")
                    self.guardian.append([x,y])
                else:
                    print("@", end="")
                    self.road_coord.append([x,y])
            print()

    def rand_position (self):
        ### Fonction that randomly place an object in the maze ###
        object_coord = random.sample(self.road_coord, k=3)
        self.needle = object_coord[0]
        self.ether = object_coord[1]
        self.tube = object_coord[2]

def main():
    print("voici le niveau :) ")
    runloop = True
    level = [
    "xxxxxxxxxxgxxxx",
    "x    xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxxxxxxxxxxxxxx"]
    content = Environment()
    etat = 1
    while runloop == True and etat > 0:
        content.lab_coord(level)
        content.rand_position()
        print("voici la position de l'aiguille {}, du tube {} et l'ether {}"
            .format(content.needle, content.tube, content.ether))
        print("voici la position du gardien {}".format(content.guardian))
        etat -= 1
    else:
        pass


if __name__ == "__main__":
    main()
