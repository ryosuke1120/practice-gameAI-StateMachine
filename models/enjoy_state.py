#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お肉が焼けたならば（isDonenessFull = true）→EatSomething

import state
import random
import feel_sorrow_state

class EnjoyState(state.State):

	def enter(self, entity):
		entity.setMessage("LittleGirl : わたしとあそぼっ！")
		entity.setGameSize(random.randint(5,10))

	#条件が満たされるまで実行される
	def execute(self, entity):
		# entity.fireSomething(random.randint(1,2))
		# entity.setMessage("じゅーじゅー")
		entity.setMessage("LittleGirl : あははー♪")
		#精神回復
		entity.recover_mental(1)
		#体力消費
		entity.exhaust(random.randint(1,2))

		#ビヘイビアツリーによる行動
		#entity.setMessage(entity.conflict_act())
		#ニューラルネットワークによる行動
		# entity.train_act()	
		# if entity.isDonenessFull():
		# 	#entity.changeState(EatSomething.EatSomething())
		# 	entity.getFsm().changeState(eat_state.EatState())

	#EatSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("LittleGirl : えっ、もうかえっちゃうの？")
		entity.message_dispatcher.dispatchMessage(
					entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
					entity.m_ID,
					2, #EntityNames.Monster.ID
					"PLAY_STATE", #MessageType
					None )

	def onMessage(self, entity, telegram):
		if telegram.message != None :
			if telegram.message == "ENJOY_STATE" :
				entity.getFsm().changeState(feel_sorrow_state.FeelSorrowState())