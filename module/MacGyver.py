#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import Environment.py as Enviro




def keyboard(Mac_position):

    ### detecte une entrée  ###
    print(Mac_position)
    direct = input("quelle direction ?")
    if direct == "e":
        haut = [1,1]
        new_position = [Mac_position[i] + haut[i] for i in range(len(Mac_position))]
        Mac_position = new_position
        keyboard(Mac_position)
    elif direct == "f":
        droite = [0,1]
        new_position = [Mac_position[i] + droite[i] for i in range(len(Mac_position))]
        Mac_position = new_position
        keyboard(Mac_position)
    elif direct == "s":
        gauche = [0,-1]
        new_position = [Mac_position[i] + gauche[i] for i in range(len(Mac_position))]
        Mac_position = new_position
        keyboard(Mac_position)
    elif direct == "x":
        bas = [-1,-1]
        new_position = [Mac_position[i] + bas[i] for i in range(len(Mac_position))]
        Mac_position = new_position
        keyboard(Mac_position)
    elif direct == "1":
        print("fin")
    else:
        print("uniquement les lettres E F S X !!!")
        keyboard(Mac_position)

def move(user_input):
    ### deplace le personnage selon le choix ###

    pass

def main():
    print("voici le hero :) ")
    Mac_position = [3, 5]
    keyboard(Mac_position)



if __name__ == "__main__":
    main()
