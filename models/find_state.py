#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ランダム→FindAndFireSomething

import state
import random
import enjoy_state
 
class FindState(state.State):

	def enter(self, entity):
		# entity.setMessage("捜索を開始します")
		entity.setMessage("LittleGirl : うさぎさんかな？")

	#条件が満たされるまで実行される
	def execute(self, entity):
		# entity.setMessage("きょろきょろ")
		entity.setMessage("LittleGirl : きょろきょろ")

		random_num = random.randint(1,9)
		if random_num % 3 == 0 :
			# 	#entity.changeState(FindAndFireSomething.FindAndFireSomething())
			# 	entity.getFsm().changeState(fire_state.FireState())
			#Monsterにメッセージを送る
			entity.message_dispatcher.dispatchMessage(
					entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
					entity.m_ID,
					2, #EntityNames.Monster.ID
					"WALK_STATE", #MessageType
					None )

	#FindAndFireSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("LittleGirl : わー、ふしぎないきものっ！")

	def onMessage(self, entity, telegram):
		if telegram.message != None :
			if telegram.message == "FIND_STATE" :
				entity.getFsm().changeState(enjoy_state.EnjoyState())
