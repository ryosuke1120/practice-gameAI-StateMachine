#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from models.character import *


class MainActivity(object):

    def __init__(self):
        self.myCharacter = Character(1, 10)

    def run_character(self):
        self.myCharacter.update()
        print(self.myCharacter.getMessage())


if __name__ == "__main__":
    a_game = MainActivity()
    while True:
        a_game.run_character()
        time.sleep(1)
