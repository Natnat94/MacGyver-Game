#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module"""
import os
import pygame
from module.Graphic import Graphic
from module.Environment import Environment
from module.MacGyver import Macgyver

def main():
    """Run the game in graphic mode"""
        #setting the variables
    win = pygame.display.set_mode((600, 600))
    directory = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(directory, "module", "Labyrinthe.txt")
    content = Environment()
    graphic = Graphic(win)
        #setting the game structure
    content.read_file(path_to_file)
    content.lab_coord()
    content.rand_position()
        #setting the inloop game variables
    wall_coord = content.wall_coord
    needle = content.objects
    mac_position = content.mac_position
    hero = Macgyver(mac_position)
        #initializing the game
    pygame.init()
    pygame.display.set_caption("---=== MacGyver Maze ===---")
    run = True
        #game main loop
    while run:
        pygame.time.Clock().tick(30)
        pygame.time.delay(100)
        direction = [0, 0]
        obj_count = hero.object_count
            #Drawing the game
        graphic.draw_bg(directory)
        graphic.draw_walls(directory, wall_coord)
            #checking if winning condition meet
        if obj_count == 3:
            if hero.mac_position == content.guardian:
                print("winner !!")
                run = False
        if needle != []:
            graphic.draw_tools(directory, needle)
            #checking for an exit game input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #checking for a moving input from the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = [-1, 0]
        if keys[pygame.K_RIGHT]:
            direction = [1, 0]
        if keys[pygame.K_UP]:
            direction = [0, -1]
        if keys[pygame.K_DOWN]:
            direction = [0, 1]
            #moving the hero if not hitting a wall and grabing object
        hero.move(direction)
        hero.hit_wall(wall_coord, content.guardian)
        hero.tools(needle)
        needle = hero.new_objet
            #drawing the guardian & the hero new position
        graphic.draw_guard(directory, content.guardian)
        graphic.draw_cara(directory, hero.mac_position)
        pygame.display.flip()

        #exiting the game
    pygame.quit()

def test():
    """Command line version of the game for testing purpose"""
    runloop = True
    etat = 20
    content= Environment()
    directory = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(directory, "module", "Labyrinthe.txt")
    content.read_file(path_to_file)
    content.lab_coord()
    content.rand_position()
    mac_position = content.mac_position
    hero = Macgyver(mac_position)
    print("voici la position des objets {}".format(content.objects))
    print("voici la position du gardien {}".format(content.guardian))
    wall = content.wall_coord
    objet = content.objects
    while runloop and etat > 0:
        print("voici la position du héros {}".format(hero.mac_position))
        direct = input("quelle direction ?")
        hero.keyboard(direct)
        hero.move(hero.direction)
        hero.hit_wall(wall, content.guardian)
        hero.tools(objet)
        objet = hero.new_objet
        if hero.object_count == 3:
            runloop = False
        etat -= 1
        print(objet)
    print("fin du programme")

if __name__ == "__main__":
    print("execution du programme principale")
    mode = input("version graphique (1) ou non-graphique (2) ?")
    if mode == "1":
        main()
    elif mode == "2":
        test()
    else:
        print("erreur de choix")

else:
    print("non non ce n'est pas un module !")
