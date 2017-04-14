#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import state

class FoxGlobalState(state.State): 

	def __init__(self):
		self.random_num = 1

	#遷移した際に一回だけ実行される
	def enter(self, entity):
		entity.setMessage("ふあああ・・")

	#あくびイベント実行
	def execute(self, entity):
		if entity.getFsm().m_pCurrentState == self:
			#このグローバルステート実行中なら1ターンで終了する
			#終了時は必ず、もとのステートに戻る
			entity.getFsm().revertToPreviousState()
		else:
			#ランダムであくびイベント発生
			self.random_num = random.randint(0,9)

		if self.random_num % 6 == 0 :
			entity.getFsm().changeState(self)

	#出るときつかれたなあ、とつぶやく#
	# def execute(self, entity)でentity.getFsm().revertToPreviousState()を行うのでglobalStateのexitは絶対に呼ばれない仕様がある
	def exit(self, entity):
		entity.setMessage("なんだか疲れたなあ")