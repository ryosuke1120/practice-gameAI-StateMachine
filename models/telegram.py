#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sorted_set_of

#メッセージパケット
class Telegram(object):
	#SEND_MESSAGE_IMMEDIATELY, sender, receiver, message, extraInfo 
	def __init__(self, dispatchTime, sender, receiver, message, extraInfo):
		self.dispatchTime = dispatchTime#: Long,
		self.sender = sender#: Int,
		self.receiver = receiver#: Int,
		self.message = message#: MessageType,
		self.extraInfo = extraInfo#: Any?
		#) : Comparable<Telegram> {

	#時間感覚が4分の1秒よりも少ないTelegramは同じものとして処理。
	# （キューが集中したり、一度に多数送信されることを防ぐ）
	def compareTo(other):
		if self.dispatchTime - 0.25 <= other.dispatchTime and other.dispatchTime <= self.dispatchTime + 0.25 :
			#4分の1秒以内なら同じものとみなす
			return 0
		else:
			#送信時刻でソートしたいので比較。同じ時刻ならどっちでも。。
			if self.dispatchTime <= other.dispatchTime :
				return -1
			else:
				return 1
