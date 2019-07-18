#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import Environment.py as Enviro


class Macgyver:

    def __init__ (self, mac_position, runloop):
        self.runloop = runloop
        self.mac_position = mac_position
        print("voici la variable pendant l'initialisation {}".format(mac_position))

    def keyboard(self):

        ### detecte une entrée  ###

        direct = input("quelle direction ?")
        if direct == "e": # deplacement en haut #
            haut = [1,1]
            self.mac_position = [self.mac_position[i] + haut[i] for i in range(len(self.mac_position))]
        elif direct == "f": # deplacement a droite #
            droite = [0,1]
            self.mac_position = [self.mac_position[i] + droite[i] for i in range(len(self.mac_position))]
        elif direct == "s": # deplacement a gauche #
            gauche = [0,-1]
            self.mac_position = [self.mac_position[i] + gauche[i] for i in range(len(self.mac_position))]
        elif direct == "x": # deplacement en bas #
            bas = [-1,-1]
            self.mac_position = [self.mac_position[i] + bas[i] for i in range(len(self.mac_position))]
        elif direct == "1": # arret de la boucle #
            self.runloop = False
        else: # touche non configure #
            print("uniquement les lettres E F S X !!!")

    #def move(user_input):
        ### deplace le personnage selon le choix ###


def main():
    print("voici le hero :) ")
    runloop = True
    mac_position = [3, 5]
    mac = Macgyver(mac_position, runloop)
    etat = 5

    while runloop == True and etat > 0:
        mac.keyboard()
        print("voici la variable apres a fonction {}".format(mac.mac_position))
        runloop = mac.runloop
        print(runloop)
        etat -= 1

    else:
        print("fin")

if __name__ == "__main__":
    main()
