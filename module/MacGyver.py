#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Macgyver:

    def __init__ (self, mac_position, runloop):
        self.runloop = runloop
        self.mac_position = mac_position
        self.direction = []

    def keyboard(self):

        ### detecte une entrée et deplace le héro( <- à retirer) ###

        direct = input("quelle direction ?")
        if direct == "e": # deplacement en haut #
            self.direction = [1,0]
        elif direct == "f": # deplacement a droite #
            self.direction = [0,1]
        elif direct == "s": # deplacement a gauche #
            self.direction = [0,-1]
        elif direct == "x": # deplacement en bas #
            self.direction = [-1,0]
        elif direct == "1": # arret de la boucle #
            self.runloop = False
        else: # touche non configure #
            print("uniquement les lettres E F S X !!!")
        self.mac_position = [self.mac_position[i] + self.direction[i] for i in range(len(self.mac_position))]

    #def tools():
        ### fonction qui determine si on a recuperé un objet ###
    #def hit_wall():
        ### fonction qui determine si il peut se deplacer dans cette direction ###


def main():
    runloop = True
    mac_position = [3, 5]
    mac = Macgyver(mac_position, runloop)
    etat = 10

    while runloop == True and etat > 0:
        print("voici la position du héros {}".format(mac.mac_position))
        mac.keyboard()
        runloop = mac.runloop
        etat -= 1
    else:
        pass

if __name__ == "__main__":
    main()
