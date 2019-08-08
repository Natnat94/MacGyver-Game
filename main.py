#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module"""
import os
import pygame
from module.graphic import Graphic
from module.environment import Environment
from module.macgyver import Macgyver


def main():
    """Run the game in graphic mode"""
        # Setting the variables
    win = pygame.display.set_mode((600, 600))
    directory = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(directory, "module", "Labyrinthe.txt")
    content = Environment()
    graphic = Graphic(win, directory)
        # Setting the game structure
    content.read_file(path_to_file)
    content.lab_coord()
    content.rand_position()
        # Setting the inloop game variables
    wall_coord = content.wall_coord
    objects = content.objects
    mac_position = content.mac_position
    hero = Macgyver(mac_position)
        # Initializing the game
    pygame.init()
    pygame.display.set_caption("---=== MacGyver Maze ===---")
    run = True
    game_won = False
    game_lose = False
        # Game main loop
    while run:
        pygame.time.Clock().tick(30)
        direction = [0, 0]
        obj_count = hero.object_count
            # Drawing the game
        graphic.draw_bg()
        graphic.draw_walls(wall_coord)
            # Checking if winning condition meet
        if hero.mac_position == content.guardian:
            if obj_count == 3:
                    # Win game
                run = False
                game_won = True
                game_lose = False
            else:
                    # lose game
                run = False
                game_won = False
                game_lose = True
        if objects != []:
            graphic.draw_tools(objects)
            # Checking for an exit game input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Waiting for an user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = [-40, 0]
        if keys[pygame.K_RIGHT]:
            direction = [40, 0]
        if keys[pygame.K_UP]:
            direction = [0, -40]
        if keys[pygame.K_DOWN]:
            direction = [0, 40]
            # Moving the hero if not hitting a wall and grabing object
        hero.move(direction)
        hero.hit_wall(wall_coord, content.guardian)
        hero.tools(objects)
        objects = hero.new_objet
            # Drawing the guardian & the hero new position
        graphic.draw_guard(content.guardian)
        graphic.draw_cara(hero.mac_position)
        pygame.display.flip()
        # Display a win message loop
    while game_won:
        graphic.draw_win()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_won = False
        pygame.display.flip()
        # Display a lose message loop
    while game_lose:
        graphic.draw_lose()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_lose = False
        pygame.display.flip()
        # Exiting the game
    pygame.quit()

def test():
    """Command line version of the game for testing purpose"""
    runloop = True
    etat = 20
    content= Environment()
    directory = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(directory, "module", "Labyrinthe.txt")
    content.read_file(path_to_file)
    content.lab_coord(True)
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
        print("debut du mode test")
        test()
    else:
        print("erreur de choix")

else:
    print("non non ce n'est pas un module !")
