#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import sleep_state
import stroll_state

class FeelSorrowState(state.State):

	#FindAndFireSomethingから遷移した際に一度だけ実行される
	def enter(self, entity):
		entity.setMessage("LittleGirl : さみしぃなぁ…")

	#条件が満たされるまで実行される
	def execute(self, entity):
		#精神消費
		entity.stress(random.randint(1,2))
		entity.setMessage("LittleGirl : しくしく…")
		#心、もしくは体力がつかれきっているか？
		if entity.is_stamina_bad() or entity.is_mental_bad():
			# entity.changeState(Sleep.Sleep())
			entity.getFsm().changeState(sleep_state.SleepState())
		#確率で立ち直る
		elif random.randint(1,9) % 7 == 0:
			# entity.changeState(FindAndFireSomething.FindAndFireSomething())
			entity.getFsm().changeState(stroll_state.StrollState())

	def exit(self, entity):
		if entity.is_stamina_bad() or entity.is_mental_bad():
			# entity.changeState(Sleep.Sleep())
			entity.setMessage("LittleGirl : 疲れたし、今日は寝よう…")
		else:
			entity.setMessage("LittleGirl : うーん、気晴らしをしたいなぁ…")

	def onMessage(self, entity, telegram):
		pass