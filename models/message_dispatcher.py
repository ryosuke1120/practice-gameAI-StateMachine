#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import telegram as tm
import sorted_set_of

#メッセージの送信を司るシングルトンのクラス
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
	def dis_charge(self, pReceiver, telegram):
		if not pReceiver.handle_message( telegram ):
		# if( done !== null && !done )
			#即時実行できなければ、５秒後のリトライ
			#current_time = Calendar.getInstance().timeInMillis
			current_time = time.time()
			telegram.dispatch_time = current_time + 5
			self.priority_q.add( telegram )

	#メッセージを送信する
	#delay : Long, sender : Int, eceiver : Int, message : MessageType, extraInfo : Any? 
	def dispatch_message(self, delay, sender, receiver, message, extra_info):
		pReceiver = self.main_activity.a_entity_manager.get_entity_from_id( receiver )
		telegram = tm.Telegram( self.SEND_MESSAGE_IMMEDIATELY, sender, receiver, message, extra_info )

		if delay <= self.SEND_MESSAGE_IMMEDIATELY :
			self.dis_charge( pReceiver, telegram )
		else:
			#current_time = Calendar.getInstance().timeInMillis
			current_time = time.time()
			telegram.dispatch_time = current_time + delay
			self.priority_q.add( telegram )

	#メッセージを遅延送信する。
	#メインループで実行し、しかるべきタイミングでメッセージが送信される
	def dispatch_delayed_messages(self):
		#current_time = Calendar.getInstance().timeInMillis
		current_time = time.time()
		while (len(self.priority_q._treeset) > 0) and (self.priority_q.get_last().dispatch_time < current_time) and (self.priority_q.get_last().dispatch_time > 0) :
			#キューの先頭からTelegramを読む
			telegram = self.priority_q.get_last()

			#受信者を見つける
			# pReceiver = EntityManager.get_entity_from_id( telegram.receiver )
			pReceiver = self.main_activity.a_entity_manager.get_entity_from_id( telegram.receiver )

			#受信者にTelegramを送る
			self.dis_charge( pReceiver, telegram )

			#終わったらキューから削除
			self.priority_q.remove( telegram )