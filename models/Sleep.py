#!/usr/bin/env python
# -*- coding: utf-8 -*-

#眠りが十分→SearchSomething

import State
import random
import SearchSomething

#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。

class Sleep(State.State):

	#EatSomethingから移動してきたときに一回だけ実行される
	def enter(self, entity):
		# if fox.getLocation() != LocationType.Field :
		# 	fox.changeLocation(LocationType.Field)
		entity.setMessage("満たされたので寝ます")

	#この状態の時に何度も実行される
	#ランダムで取得した数値が3で割り切れる場合、休まった状態になり「探す」状態に移行する
	def execute(self, entity):
		entity.setMessage("ぐーぐー")
		entity.digestSomething(random.randint(1,2))
		if entity.isHungry():
			# entity.changeState(SearchSomething.SearchSomething())
			entity.getFsm(SearchSomething.SearchSomething())

		# random_num = random.randint(0,9)
		# if random_num % 3 == 0 :
		# 	fox.changeState(SearchSomething.SearchSomething())

	#「探す」状態に移行する前に一度だけ実行される
	def exit(self, entity):
		pass