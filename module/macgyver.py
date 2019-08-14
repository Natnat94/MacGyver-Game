#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module de Macgyver"""
from .config import SPRITE


class Macgyver:
    """Class of Macgyver"""
    def __init__(self, mac_position):
        self.mac_position = mac_position
        self.new_mac_position = []
        self.object_count = 0
        self.new_objet = 0

    def keyboard(self, direct):
        """detect en input and move the hero (command line only)"""
        if direct == "e":  # deplacement en haut
            self.direction = [0, -SPRITE]
        elif direct == "f":  # deplacement a droite
            self.direction = [SPRITE, 0]
        elif direct == "s":  # deplacement a gauche
            self.direction = [-SPRITE, 0]
        elif direct == "x":  # deplacement en bas
            self.direction = [0, SPRITE]
        else:  # touche non configure
            print("uniquement les lettres E F S X !!!")
            self.direction = [0, 0]

    def move(self, direction):
        """move to new coordinate the hero"""
        self.new_mac_position = [self.mac_position[i] + direction[i] for i
                                 in range(len(self.mac_position))]

    def tools(self, objet):
        """fonction that check if there is an object and take it"""
        if self.mac_position in objet.values():  # check if the position
            delete = []                          # is in the dictionary
            for key, val in objet.items():    # loop for removing the object
                if val == self.mac_position:  # position in the dictionary
                    delete.append(key)
            for i in delete:
                del objet[i]
            self.object_count += 1
        else:
            self.new_objet = objet

    def hit_wall(self, wall, guard):
        """fonction that check if there is a wall"""
        if self.new_mac_position in wall:
            pass
        elif self.new_mac_position == guard:
            if self.object_count >= 1:
                self.mac_position = self.new_mac_position
        else:
            self.mac_position = self.new_mac_position
