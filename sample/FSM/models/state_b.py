#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import state_c

class StateB(state.State):

	def enter(self, entity):
		entity.setMessage("ゲームの準備をします")
		entity.setGameSize(random.randint(5,10))

	def execute(self, entity):
		entity.fireSomething(random.randint(1,2))
		entity.setMessage("がちゃがちゃ")
		if entity.isDonenessFull():
			entity.getFsm().changeState(state_c.StateC())

	def exit(self, entity):
		entity.setMessage("よし、準備できた")