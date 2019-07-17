#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module.MacGyver as mc
import module.Environment as enviro

def main():

    enviro.Environment.main(level)
    mc.main(Mac_position)
    print("fin du programme")

if __name__ == "__main__":

    level = [
    "xxxxxxxxxxxxxxx",
    "x    xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxx  xxx    xxx",
    "xxxxxxxxxxxxxxx"]
    Mac_position = [3, 5]
    print("execution du programme principale")
    main()

else:
    print("non non ce n'est pas un module !")
