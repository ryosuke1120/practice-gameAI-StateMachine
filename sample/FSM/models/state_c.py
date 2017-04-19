#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import state_d
import state_b


class StateC(state.State):

    def enter(self, entity):
        entity.setMessage("スプラトゥーンをします")

    def execute(self, entity):
        entity.eatSomething(random.randint(1, 2))
        entity.setMessage("ぴこぴこ")
        if entity.isAte():
            if entity.isStomachFull():
                entity.getFsm().changeState(state_d.StateD())
            else:
                entity.getFsm().changeState(state_b.StateB())

    def exit(self, entity):
        if entity.isStomachFull():
            entity.setMessage("疲れたし、寝よう")
        else:
            entity.setMessage("うーん、まだゲームしたい")
