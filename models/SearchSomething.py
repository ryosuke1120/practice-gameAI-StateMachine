#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ランダム→FindAndFireSomething

import State
import random
import FindAndFireSomething
 
class SearchSomething(State.State):

	#SleepまたはEatSomethingから遷移した際に一回だけ実行される
	def enter(self, entity):
		# if entity.getLocation() != LocationType.Field :
		# 	entity.changeLocation(LocationType.Field)
		# entity.setMessage("捜索を開始します")
		entity.setMessage("活動を開始します")

	#条件が満たされるまで実行される
	def execute(self, entity):
		random_num = random.randint(0,9)
		# entity.setMessage("きょろきょろ")
		entity.setMessage("だらだら")

		if random_num % 3 == 0 :
			#entity.changeState(FindAndFireSomething.FindAndFireSomething())
			entity.getFsm().changeState(FindAndFireSomething.FindAndFireSomething())

	#FindAndFireSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("ゲームでもするか")