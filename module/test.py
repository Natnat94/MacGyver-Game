#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module"""
import os
import pygame
from  Graphic import Graphic
from Environment import Environment
from MacGyver import Macgyver



def main():
    """Run the game in graphic mode"""
    tool_file = "ether.png"

    level = [
        "xxxxxxxxxxxgxxx",
        "x      xxx     ",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx         xx",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx  xxxx  xxx",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx  xxx    xx",
        "xxxx m       xx",
        "xxxxxxxxxxxxxxx"]
    win = pygame.display.set_mode((600, 600))
    content = Environment(level)
    graphic = Graphic(win)
    content.lab_coord()
    content.rand_position()
    wall_coord = content.wall_coord
    needle = content.objett
    mac_position = content.mac_position
    hero = Macgyver(mac_position)
    pygame.init()
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pygame.display.set_caption("                   ---=== MacGyver Maze ===---")


    #needle1 = [i * 40 for i in content.needle]

    run = True
    while run:
        pygame.time.Clock().tick(30)
        pygame.time.delay(100)
        direction = [0, 0]
        obj_count = hero.object_count
        graphic.draw_bg(directory)
        graphic.draw_walls(directory, wall_coord)
        if obj_count == 3:
            if hero.mac_position == content.guardian:
                print("winner !!")
                run = False
        if needle != []:
            graphic.draw_tools(directory, tool_file, needle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = [-1, 0]
        if keys[pygame.K_RIGHT]:
            direction = [1, 0]
        if keys[pygame.K_UP]:
            direction = [0, -1]
        if keys[pygame.K_DOWN]:
            direction = [0, 1]
        hero.move(direction)
        hero.hit_wall(wall_coord, content.guardian)
        hero.tools(needle)
        needle = hero.new_objet
        graphic.draw_guard(directory, content.guardian)
        graphic.draw_cara(directory, hero.mac_position)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
