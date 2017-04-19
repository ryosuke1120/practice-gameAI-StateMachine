#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import state_b


class StateA(state.State):

    def enter(self, entity):
        entity.setMessage("活動を開始します")

    def execute(self, entity):
        random_num = random.randint(0, 9)
        entity.setMessage("だらだら")

        if random_num % 3 == 0:
            entity.getFsm().changeState(state_b.StateB())

    def exit(self, entity):
        entity.setMessage("ゲームでもするか")
