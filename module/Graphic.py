#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import os



def draw_bg(win):

    bg1 = pygame.image.load(os.path.join("../ressource","floor.png"))
    backg = pygame.Surface(win.get_size())
    background = backg.convert()
    background.fill((250, 250, 250))
    for i in range(8):
        for c in range(30):
            background.blit(bg1, (i*80,c*20), (0, 60, 80,20))
    win.blit(background, (0, 0))
    pygame.display.update()

def draw_tools(win, tool_file, tool_coord):
    tool = pygame.image.load(os.path.join("../ressource",tool_file))
    tool = pygame.transform.scale(tool, (40, 40))
    win.blit(tool, tool_coord)
    pygame.display.update()

def draw_walls(win, wall_coord):
    wall = pygame.image.load(os.path.join("../ressource","floor.png")).convert()
    wall1 = pygame.transform.scale2x(wall)
    for i in wall_coord:
        taille = [40, 40]
        new_position = [i[c] * taille[c] for c in range(len(i))]
        win.blit(wall1, new_position, (0, 440, 40,40))
    pygame.display.update()

def draw_cara(x, y, win, graphic_mode, mac_position):
    macgyver1 = pygame.image.load(os.path.join("../ressource","Macgyver.png"))
    macgyver1 = pygame.transform.scale(macgyver1, (40, 40))
    if graphic_mode:
        win.blit(macgyver1, (x, y))
        pygame.display.update()
    else:
        win.blit(macgyver1, mac_position)
        pygame.display.update()

def run_game(x, y, vel, win, wall_coord, graphic_mode, mac_position, tool_file, tool_coord):

    run = True
    while run:
        pygame.time.delay(100)
        draw_bg(win)
        draw_walls(win, wall_coord)
        draw_tools(win, tool_file, tool_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if graphic_mode == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x -= vel
            if keys[pygame.K_RIGHT]:
                x += vel
            if keys[pygame.K_UP]:
                y -= vel
            if keys[pygame.K_DOWN]:
                y += vel
            draw_cara(x, y, win, graphic_mode, mac_position)
        else:
            draw_cara(x, y, graphic_mode, mac_position)

    pygame.quit()

def main():

    graphic_mode = True
    tool_file = "ether.png"
    tool_coord = [120, 200]
    x = 200
    y = 240
    vel = 40
    wall_coord = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0],
     [7, 0], [8, 0], [9, 0], [11, 0], [12, 0], [13, 0], [14, 0], [0, 1],
      [5, 1], [6, 1], [7, 1], [12, 1], [13, 1], [14, 1], [0, 2], [1, 2],
       [2, 2], [5, 2], [6, 2], [7, 2], [12, 2], [13, 2], [14, 2], [0, 3],
        [1, 3], [2, 3], [5, 3], [6, 3], [7, 3], [12, 3], [13, 3], [14, 3],
         [0, 4], [1, 4], [2, 4], [5, 4], [6, 4], [7, 4], [12, 4], [13, 4],
          [14, 4], [0, 5], [1, 5], [2, 5], [12, 5], [13, 5], [14, 5], [0, 6],
           [1, 6], [2, 6], [5, 6], [6, 6], [7, 6], [12, 6], [13, 6], [14, 6],
            [0, 7], [1, 7], [2, 7], [5, 7], [6, 7], [7, 7], [12, 7], [13, 7],
             [14, 7], [0, 8], [1, 8], [2, 8], [5, 8], [6, 8], [7, 8], [8, 8],
              [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [0, 9],
    [1, 9], [2, 9], [5, 9], [6, 9], [7, 9], [12, 9], [13, 9], [14, 9],
     [0, 10], [1, 10], [2, 10], [5, 10], [6, 10], [7, 10], [12, 10],
      [13, 10], [14, 10], [0, 11], [1, 11], [2, 11], [5, 11], [6, 11],
       [7, 11], [12, 11], [13, 11], [14, 11], [0, 12], [1, 12], [2, 12],
        [5, 12], [6, 12], [7, 12], [12, 12], [13, 12], [14, 12], [0, 13],
         [1, 13], [2, 13], [5, 13], [6, 13], [7, 13], [12, 13], [13, 13],
         [14, 13], [0, 14], [1, 14], [2, 14], [3, 14], [4, 14], [5, 14],
          [6, 14], [7, 14], [8, 14], [9, 14], [10, 14], [11, 14], [12, 14],
           [13, 14], [14, 14]]
    pygame.init()
    pygame.display.set_caption("                   ---=== MacGyver Maze ===---")
    win = pygame.display.set_mode((600, 600))
    bg = pygame.image.load(os.path.join("../ressource","floor.png"))
    macgyver1 = pygame.image.load(os.path.join("../ressource","Macgyver.png"))
    draw_bg(win)
    draw_walls(win, wall_coord)
    draw_tools(win, tool_file, tool_coord)
    run_game(x, y, vel, win, wall_coord, graphic_mode, 0, tool_file, tool_coord)

if __name__ == "__main__":
    main()
