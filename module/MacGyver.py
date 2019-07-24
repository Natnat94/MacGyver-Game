#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Macgyver:

    def __init__ (self, mac_position, runloop):
        self.runloop = runloop
        self.mac_position = mac_position
        self.direction = []
        self.new_mac_position = []
        self.object_count = 0

    def keyboard(self, direct):

        ### detecte une entrée et deplace le héro( <- à retirer) ###
        self.direct = direct
        if self.direct == "e": # deplacement en haut #
            self.direction = [1,0]
        elif self.direct == "f": # deplacement a droite #
            self.direction = [0,1]
        elif self.direct == "s": # deplacement a gauche #
            self.direction = [0,-1]
        elif self.direct == "x": # deplacement en bas #
            self.direction = [-1,0]
        elif self.direct == "1": # arret de la boucle #
            self.runloop = False
        else: # touche non configure #
            print("uniquement les lettres E F S X !!!")

    def move(self):
        ### move to new coordinate the hero ###
        self.new_mac_position = [self.mac_position[i] + self.direction[i] for i in range(len(self.mac_position))]

    def tools(self, objet):
        ### fonction qui determine si on a recuperé un objet ###
        if self.mac_position in objet:
            self.object_count += 1
            print(self.object_count)
            objet.remove(self.mac_position)
        else:
            pass

    def hit_wall(self, wall):
        ### fonction qui determine si il peut se deplacer dans cette direction ###
        self.wall = wall
        if self.new_mac_position in self.wall:
            print("mur")
        else:
            print("route")
            self.mac_position = self.new_mac_position

def main():
    runloop = True
    mac_position = [3, 5]
    etat = 10
    objet = [[7, 6], [6, 6], [5,6]]
    wall = [0,0]
    mac = Macgyver(mac_position, runloop)

    while runloop == True and etat > 0:
        print("voici la position du héros {}".format(mac.mac_position))
        direct = input("quelle direction ?")
        mac.keyboard(direct)
        mac.move()
        mac.hit_wall(wall)
        mac.tools(objet)
        runloop = mac.runloop
        etat -= 1
    else:
        pass

if __name__ == "__main__":
    main()
