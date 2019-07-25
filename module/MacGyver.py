#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module de Macgyver"""

class Macgyver:
    """Class de Macgyver"""
    def __init__(self, mac_position):
        self.mac_position = mac_position
        self.new_mac_position = []
        self.object_count = 0
        self.new_objet = 0

    def keyboard(self, direct):
        """detecte une entrée et deplace le héro (en commande uniquement)"""
        self.direct = direct
        if self.direct == "e":  # deplacement en haut #
            self.direction = [1, 0]
        elif self.direct == "f":  # deplacement a droite #
            self.direction = [0, 1]
        elif self.direct == "s":  # deplacement a gauche #
            self.direction = [0, -1]
        elif self.direct == "x":  # deplacement en bas #
            self.direction = [-1, 0]
        else:  # touche non configure #
            print("uniquement les lettres E F S X !!!")

    def move(self, direction):
        """move to new coordinate the hero"""
        self.new_mac_position = [self.mac_position[i] + direction[i] for i in range(len(self.mac_position))]

    def tools(self, objet):
        """fonction qui determine si on a recuperé un objet"""
        if self.mac_position in objet:
            objet.remove(self.mac_position)
            self.object_count += 1
        else:
            self.new_objet = objet

    def hit_wall(self, wall):
        """fonction qui determine si il peut se deplacer dans cette direction"""
        self.wall = wall
        if self.new_mac_position in self.wall:
            pass
        else:
            self.mac_position = self.new_mac_position


def main():
    """main fonction pour le testing"""
    runloop = True
    mac_position = [3, 5]
    etat = 10
    objet = [[7, 6], [6, 6], [5, 6]]
    wall = [0, 0]
    mac = Macgyver(mac_position)

    while runloop and etat > 0:
        print("voici la position du héros {}".format(mac.mac_position))
        direct = input("quelle direction ?")
        mac.keyboard(direct)
        mac.move(mac.direction)
        mac.direction = [0, 0]
        mac.hit_wall(wall)
        mac.tools(objet)
        etat -= 1

if __name__ == "__main__":
    main()
