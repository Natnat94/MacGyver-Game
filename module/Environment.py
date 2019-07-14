#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

level = [
"xxxxxxxxxxxxxxx",
"x    xxx    xxx",
"xxx  xxx    xxx",
"xxx  xxx    xxx",
"xxx  xxx    xxx",
"xxx  xxx    xxx",
"xxx  xxx    xxx",
"xxx  xxx    xxx",
"xxxxxxxxxxxxxxx"]


level1 = [
"xxxxxxxxxxxxxxx",
"x    xxx    xxx",
"x    xxx    xxx",
"x    xxx    xxx",
"x    xxx    xxx",
"x    xxx    xxx",
"x    xxx    xxx",
"x    xxx    xxx",
"xxxxxxxxxxxxxxx"]


class Environment:

    def __init__ (self):

    #loading the labyrinth file
        needle = [0,0] #setting the 1st object with null coordinate
        ether = [0,0] #setting the 2nd object with null coordinate
        tube = [0,0] #setting the 3rd object with null coordinate
        MAX_WIDTH = 16
        MAX_LENGHT = 16
        guardian = [0,0] #setting the gard variable with the exit of lab position

    def lab_coord (self):
        ### Fonction that translate draw maze into coordinate ###
        wall_coord=[]
        road_coord=[]

        for y in range(len(self)):
            for x in range(len(self[y])):
                painting = self [y][x]
                #print(x,y)
                if painting == "x":
                    print("/", end="")
                    wall_coord.append([x,y])
                else:
                    print("@", end="")
                    road_coord.append([x,y])
                ### --- ajouter une condition qui repers la position du gardien --- ###
            print()

    def rand_position (lab_coord):
        ### Fonction that randomly place an object in the maze ###
        object_coord = random.sample(road_coord, k=3)
        print(object_coord)
        needle = object_coord[0]
        ether = object_coord[1]
        tube = object_coord[2]
        print("voici le 1er", needle)
        print("voici le 2eme", ether)

Environment.lab_coord(level1)
