#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お肉が焼けるまでやいてやく→EatSomething

import state
import random
import state_c

#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。

class StateB(state.State):

	#SearchSomethingから移動してきたときに一回だけ実行される
	def enter(self, entity):
		# if fox.getLocation() != LocationType.Field :
		# 	fox.changeLocation(LocationType.Field)
		# fox.setMessage("発見したのできつね色に焼きます")
		entity.setMessage("ゲームの準備をします")
		entity.setGameSize(random.randint(5,10))

	#この状態の時に何度も実行される
	#ランダムで取得した数値が3で割り切れる場合、お肉がやけて「食べる」状態に移行する
	def execute(self, entity):
		entity.fireSomething(random.randint(1,2))
		# entity.setMessage("がちゃがちゃ")
		#ビヘイビアツリーによる行動
		entity.setMessage("がちゃがちゃ")
		if entity.isDonenessFull():
			#entity.changeState(EatSomething.EatSomething())
			entity.getFsm().changeState(state_c.StateC())

		# random_num = random.randint(0,9)
		# fox.setMessage("じゅーじゅー")

		# if random_num % 3 == 0 :
		# 	fox.changeState(EatSomething.EatSomething())

	#「食べる」状態に移行する前に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("よし、準備できた")