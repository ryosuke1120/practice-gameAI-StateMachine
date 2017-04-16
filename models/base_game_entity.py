#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

#全ての動作主体のベースとなるEntity

#abstract class
class BaseGameEntity(object):
	__metaclass__ = ABCMeta

	def __init__(self, m_ID):
		#SetIDの処理をいれる（IDが正しく設定されたのかを確認する処理）
		self.require(True)
		self.m_iNextVlidID = 0

	#動作をアップデートする処理。下位クラスでの実装を必須にする
	@abstractmethod
	def update():
		pass

	#def handleMessage( msg : Telegram )
	@abstractmethod
	def handleMessage(msg):
		pass