#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お腹が減ったならば（isHungry = true）→SearchSomething

import state
import random
import search_state

class SleepState(state.State):

	#EatSomethingから遷移した際に一回だけ実行される
	def enter(self, entity):
		# if entity.getLocation() != LocationType.Field :
		# 	entity.changeLocation(LocationType.Field)
		entity.setMessage("寝ます")

	#条件が満たされるまで実行される
	def execute(self, entity):
		entity.setMessage("ぐーぐー")
		entity.digestSomething(random.randint(1,2))
		if entity.isHungry():
			# entity.changeState(SearchSomething.SearchSomething())
			entity.getFsm().changeState(search_state.SearchState())

	#SearchSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("ふぁー、よく寝た")