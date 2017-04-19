#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from entity_names import EntityNames
from little_girl import *
from monster import *
import entity_manager
import message_dispatcher


class MainActivity(object):

    def __init__(self):
        self.md = message_dispatcher.MessageDispatcher(self)
        self.my_little_girl = LittleGirl(
            self.md, EntityNames.LITTLEGIRL.value, 10)
        self.my_monster = Monster(self.md, EntityNames.MONSTER.value, 5, 5)

        self.a_entity_manager = entity_manager.EntityManager()
        self.a_entity_manager.register_entity(self.my_little_girl)
        self.a_entity_manager.register_entity(self.my_monster)

    def run_world(self):
        self.my_little_girl.update()
        self.my_monster.update()
        # fox_message.text = myFox.getMessage()
        print(self.my_little_girl.get_message())
        print(self.my_monster.get_message())

        self.md.dispatch_delayed_messages()


if __name__ == "__main__":
    a_game = MainActivity()
    while True:
        a_game.run_world()
        time.sleep(1)
