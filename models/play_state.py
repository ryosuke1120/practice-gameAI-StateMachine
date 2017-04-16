#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import return_state

class PlayState(state.State):

	#遊びモードに入ったときに一度だけ実行される
	def enter(self, entity):
		# entity.changeLocation(LocationType.Field)
		entity.setMessage("Monster : …！！")
		entity.message_dispatcher.dispatchMessage(
					entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
					entity.m_ID,
					1, #EntityNames.LittleGirl.ID
					"FIND_STATE", #MessageType
					None )

	#条件が満たされるまで実行される
	def execute(self, entity):
		entity.setMessage("Monster : ぴょこっぴょこっ♪")
		#if 疲れて帰らなくちゃいけなくなったら
		entity.consume(random.randint(1,2))
		if entity.isStaminaLess() :
			# #LittleGirlににメッセージを送る
			entity.message_dispatcher.dispatchMessage(
								entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
								entity.m_ID,
								1, #EntityNames.LittleGirl.ID
								"ENJOY_STATE", #MessageType
								None )

	#に遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("Monster : こくこく…")
		pass

	def onMessage(self, entity, telegram):
		if telegram.message != None :
			if telegram.message == "PLAY_STATE" :
				entity.getFsm().changeState(return_state.ReturnState())