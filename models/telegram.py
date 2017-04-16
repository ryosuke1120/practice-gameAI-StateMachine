#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sorted_set_of

#メッセージパケット
class Telegram(object):
	#SEND_MESSAGE_IMMEDIATELY, sender, receiver, message, extraInfo 
	def __init__(self, dispatch_time, sender, receiver, message, extra_info):
		self.dispatch_time = dispatch_time# Long
		self.sender = sender# Int
		self.receiver = receiver# Int
		self.message = message# MessageType
		self.extra_info = extra_info# Any

	#時間感覚が4分の1秒よりも少ないTelegramは同じものとして処理。
	# （キューが集中したり、一度に多数送信されることを防ぐ）
	def compare_to(other):
		if self.dispatch_time - 0.25 <= other.dispatch_time and other.dispatch_time <= self.dispatch_time + 0.25 :
			#4分の1秒以内なら同じものとみなす
			return 0
		else:
			#送信時刻でソートしたいので比較。同じ時刻ならどっちでも。。
			if self.dispatch_time <= other.dispatch_time :
				return -1
			else:
				return 1
