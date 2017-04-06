#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お肉が焼けるまでやいてやく→EatSomething

import State
import random
import EatSomething

#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。

class FindAndFireSomething(State.State):

	#SearchSomethingから移動してきたときに一回だけ実行される
	def enter(self, fox):
		# if fox.getLocation() != LocationType.Field :
		# 	fox.changeLocation(LocationType.Field)
		# fox.setMessage("発見したのできつね色に焼きます")
		fox.setMessage("ゲームの準備をします")
		fox.setGameSize(random.randint(5,10))

	#この状態の時に何度も実行される
	#ランダムで取得した数値が3で割り切れる場合、お肉がやけて「食べる」状態に移行する
	def execute(self, fox):
		fox.fireSomething(random.randint(1,2))
		fox.setMessage("がちゃがちゃ")
		if fox.isDonenessFull():
			fox.changeState(EatSomething.EatSomething())

		# random_num = random.randint(0,9)
		# fox.setMessage("じゅーじゅー")

		# if random_num % 3 == 0 :
		# 	fox.changeState(EatSomething.EatSomething())

	#「食べる」状態に移行する前に一度だけ実行される
	def exit(self, fox):
		pass