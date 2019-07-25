#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  Graphic import *
from Environment import *
from MacGyver import *
import pygame
import os


graphic_mode = True
tool_file = "ether.png"
mac_position = [4, 9]
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
    "xxxx         xx",
    "xxxxxxxxxxxxxxx"]
content = Environment()
hero = Macgyver(mac_position)
content.lab_coord(level)
content.rand_position()
wall_coord = content.wall_coord
vel = 40
needle = content.objett
print(content.objett)
pygame.init()
pygame.display.set_caption("                   ---=== MacGyver Maze ===---")
win = pygame.display.set_mode((600, 600))
bg = pygame.image.load(os.path.join("../ressource","floor.png"))
macgyver1 = pygame.image.load(os.path.join("../ressource","Macgyver.png"))

#needle1 = [i * 40 for i in content.needle]

run = True
while run:
    pygame.time.Clock().tick(30)
    pygame.time.delay(100)
    direction = [0,0]
    obj_count = hero.object_count
    Graphic.draw_bg(win)
    Graphic.draw_walls(win, wall_coord)
    if obj_count == 3:
        run = False
    if needle != []:
        Graphic.draw_tools(win, tool_file, needle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = [-1,0]
    if keys[pygame.K_RIGHT]:
        direction = [1,0]
    if keys[pygame.K_UP]:
        direction = [0,-1]
    if keys[pygame.K_DOWN]:
        direction = [0,1]
    hero.move(direction)
    hero.hit_wall(wall_coord)
    hero.tools(needle)
    needle = hero.new_objet
    print(needle)
    Graphic.draw_cara(win, hero.mac_position)
    pygame.display.flip()

pygame.quit()
