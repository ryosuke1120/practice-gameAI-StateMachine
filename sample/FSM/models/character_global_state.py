#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import state

class CharacterGlobalState(state.State): 

	def __init__(self):
		self.random_num = 1

	def enter(self, entity):
		entity.setMessage("ふあああ・・")

	def execute(self, entity):
		if entity.getFsm().m_pCurrentState == self:
			entity.getFsm().revertToPreviousState()
		else:
			self.random_num = random.randint(0,9)

		if self.random_num % 6 == 0 :
			entity.getFsm().changeState(self)

	def exit(self, entity):
		entity.setMessage("なんだか疲れたなあ")