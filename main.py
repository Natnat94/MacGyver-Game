#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module.MacGyver as mc
import module.Environment as enviro

def main():

    enviro.main()
    mc.main()
    print("fin du programme")

if __name__ == "__main__":
    print("execution du programme principale")
    main()

else:
    print("non non ce n'est pas un module !")
