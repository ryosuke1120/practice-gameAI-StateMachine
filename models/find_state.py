#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ランダム→FindAndFireSomething

import state
import random
import enjoy_state
 
class FindState(state.State):

	def enter(self, entity):
		entity.set_message("LittleGirl : うさぎさんかな？")

	#条件が満たされるまで実行される
	def execute(self, entity):
		entity.set_message("LittleGirl : きょろきょろ")

		random_num = random.randint(1,9)
		if random_num % 3 == 0 :
			# 	#entity.changeState(FindAndFireSomething.FindAndFireSomething())
			# 	entity.getFsm().changeState(fire_state.FireState())
			#Monsterにメッセージを送る
			entity.message_dispatcher.dispatch_message(
					entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
					entity.m_ID,
					2, #EntityNames.Monster.ID
					"WALK_STATE", #MessageType
					None )

	def exit(self, entity):
		entity.set_message("LittleGirl : わー、ふしぎないきものっ！")

	def on_message(self, entity, telegram):
		if telegram.message != None :
			if telegram.message == "FIND_STATE" :
				entity.get_fsm().change_state(enjoy_state.EnjoyState())
