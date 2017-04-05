#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

#全ての動作主体のベースとなるEntity

#abstract class BaseGameEntity( val m_ID : Int )
# 抽象クラス
class BaseGameEntity(object):
	__metaclass__ = ABCMeta

	# init {
	#     #ここに本でいうSetIDの処理をいれる（IDが正しく設定されたのかを確認する処理）
	#     require(true)
	# }
	def __init__(self, m_ID):
		#ここに本でいうSetIDの処理をいれる（IDが正しく設定されたのかを確認する処理）
		self.require(True)

		# private companion object {
		#     var m_iNextVlidID = 0
		# }
		self.m_iNextVlidID = 0

	#動作をアップデートする処理。下位クラスでの実装を必須にする
	@abstractmethod
	def update():
		pass	
