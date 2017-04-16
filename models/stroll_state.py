#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ランダム→FindAndFireSomething

import state
import random
import find_state
 
class StrollState(state.State):

	#SleepまたはEatSomethingから遷移した際に一回だけ実行される
	def enter(self, entity):
		# entity.setMessage("捜索を開始します")
		entity.setMessage("LittleGirl : お散歩をしよう。")

	#条件が満たされるまで実行される
	def execute(self, entity):
		# random_num = random.randint(0,9)
		# entity.setMessage("きょろきょろ")
		entity.setMessage("LittleGirl : てくてく")

	#FindAndFireSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("LittleGirl : あれ？動物の足跡…？")

	def onMessage(self, entity, telegram):
		if telegram.message != None :
			if telegram.message == "STROLL_STATE" :
				entity.getFsm().changeState(find_state.FindState())
