#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import sleep_state
import stroll_state

class FeelSorrowState(state.State):

	#FindAndFireSomethingから遷移した際に一度だけ実行される
	def enter(self, entity):
		entity.set_message("LittleGirl : さみしぃなぁ…")

	#条件が満たされるまで実行される
	def execute(self, entity):
		#精神消費
		entity.stress(random.randint(1,2))
		entity.set_message("LittleGirl : しくしく…")
		#心、もしくは体力がつかれきっているか？
		if entity.is_stamina_bad() or entity.is_mental_bad():
			# entity.changeState(Sleep.Sleep())
			entity.get_fsm().change_state(sleep_state.SleepState())
		#確率で立ち直る
		elif random.randint(1,9) % 7 == 0:
			entity.get_fsm().change_state(stroll_state.StrollState())

	def exit(self, entity):
		if entity.is_stamina_bad() or entity.is_mental_bad():
			entity.set_message("LittleGirl : 疲れたし、今日は寝よう…")
		else:
			entity.set_message("LittleGirl : うーん、気晴らしをしたいなぁ…")

	def on_message(self, entity, telegram):
		pass