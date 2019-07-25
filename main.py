#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module.MacGyver as macg
import module.Environment as content

def deco():

    runloop = True
    mac_position = [3, 5]
    etat = 20
    test1= content.Environment()
    test2 = macg.Macgyver(mac_position)
    level = [
    "xxxxxxxxxxgxxxx",
    "x             x",
    "x             x",
    "x             x",
    "x             x",
    "x             x",
    "x             x",
    "x             x",
    "xxxxxxxxxxxxxxx"]


    test1.lab_coord(level)
    test1.rand_position()
    print("voici la position de l'aiguille {}, du tube {} et l'ether {}"
        .format(test1.objett[0], test1.objett[1], test1.objett[2]))
    print("voici la position du gardien {}".format(test1.guardian))
    wall = test1.wall_coord
    objet = test1.objett
    while runloop == True and etat > 0:
        print("voici la position du héros {}".format(test2.mac_position))
        direct = input("quelle direction ?")
        test2.keyboard(direct)
        test2.move(test2.direction)
        test2.hit_wall(wall)
        test2.tools(objet)
        print(objet)
        if test2.object_count == 3:
            runloop = False
        etat -= 1

def main():

    deco()
    print("fin du programme")

if __name__ == "__main__":
    print("execution du programme principale")
    main()

else:
    print("non non ce n'est pas un module !")
