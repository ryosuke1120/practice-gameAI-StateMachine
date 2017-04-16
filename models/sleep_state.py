#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お腹が減ったならば（isHungry = true）→SearchSomething

import state
import stroll_state

class SleepState(state.State):

	def enter(self, entity):
		entity.setMessage("LittleGirl : ふぁ〜")

	#条件が満たされるまで実行される
	def execute(self, entity):
		entity.setMessage("LittleGirl : すやすや")
		entity.recover_stamina(1)
		if entity.is_stamina_good():
			# entity.changeState(SearchSomething.SearchSomething())
			entity.getFsm().changeState(stroll_state.StrollState())

	#SearchSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("LittleGirl : ふぁー、よく寝た")

	def onMessage(self, entity, telegram):
		pass