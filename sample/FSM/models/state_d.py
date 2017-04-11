#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import state_a

class StateD(state.State):

	def enter(self, entity):
		entity.setMessage("寝ます")

	def execute(self, entity):
		entity.setMessage("ぐーぐー")
		entity.digestSomething(random.randint(1,2))
		if entity.isHungry():
			entity.getFsm().changeState(state_a.StateA())

	def exit(self, entity):
		entity.setMessage("ふぁー、よく寝た")