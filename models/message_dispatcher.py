#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import telegram as tm
import sorted_set_of

#メッセージの送信を司るシングルトンのクラス
#object MessageDispatcher {
class MessageDispatcher(object):

	def __init__(self, main_activity):
		self.main_activity = main_activity
		self.SEND_MESSAGE_IMMEDIATELY = 0 #long

		#遅延型メッセージのためのキュー
		#重複不可のソートされたTreeSetで対応：
		#Telegramの中でComparableを継承して、送信時刻でソートするようにしている
		#self.priorityQ : TreeSet<Telegram> = SortedSetOf()
		self.priority_q = sorted_set_of.SortedSetOf()
 
	#受け取り側のメッセージ処理用のメンバー関数を呼ぶ
	#pReceiver : BaseGameEntity?
	#telegram : Telegram 
	def disCharge(self, pReceiver, telegram):
		if not pReceiver.handleMessage( telegram ):
		# if( done !== null && !done )
			#即時実行できなければ、５秒後のリトライ
			#currentTime = Calendar.getInstance().timeInMillis
			currentTime = time.time()
			telegram.dispatchTime = currentTime + 5
			self.priority_q.add( telegram )

	#メッセージを送信する
	#delay : Long, sender : Int, eceiver : Int, message : MessageType, extraInfo : Any? 
	def dispatchMessage(self, delay, sender, receiver, message, extraInfo):
		pReceiver = self.main_activity.a_entity_manager.getEntityFromId( receiver )
		telegram = tm.Telegram( self.SEND_MESSAGE_IMMEDIATELY, sender, receiver, message, extraInfo )

		if delay <= self.SEND_MESSAGE_IMMEDIATELY :
			self.disCharge( pReceiver, telegram )
		else:
			#currentTime = Calendar.getInstance().timeInMillis
			currentTime = time.time()
			telegram.dispatchTime = currentTime + delay
			self.priority_q.add( telegram )

	#メッセージを遅延送信する。
	#メインループで実行し、しかるべきタイミングでメッセージが送信されるようにすべき
	def dispatchDelayedMessages(self):
		#currentTime = Calendar.getInstance().timeInMillis
		currentTime = time.time()
		while (len(self.priority_q._treeset) > 0) and (self.priority_q.get_last().dispatchTime < currentTime) and (self.priority_q.get_last().dispatchTime > 0) :
			#キューの先頭からTelegramを読む
			telegram = self.priority_q.get_last()

			#受信者を見つける
			# pReceiver = EntityManager.getEntityFromId( telegram.receiver )
			pReceiver = self.main_activity.a_entity_manager.getEntityFromId( telegram.receiver )

			#受信者にTelegramを送る
			self.disCharge( pReceiver, telegram )

			#終わったらキューから削除
			self.priority_q.remove( telegram )