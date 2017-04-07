#!/usr/bin/env python
# -*- coding: utf-8 -*-

#食べる
#おななが減ってたら→SearchSomething
#お腹がいっぱいなら→Sleep

import State
import random
import SearchSomething
import Sleep
import FindAndFireSomething

#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。

class EatSomething(State.State):

	#SFindAndFireSomethingから移動してきたときに一回だけ実行される
	def enter(self, entity):
		# if fox.getLocation() != LocationType.Field :
		# 	fox.changeLocation(LocationType.Field)
		# fox.setMessage("食べます")
		entity.setMessage("スプラトゥーンをします")

	#この状態の時に何度も実行される
	#ランダムで取得した数値が3で割り切れる場合、お腹がいっぱいになり「眠る」状態に移行する
	#そうでない場合はもう一度探す
	def execute(self, entity):
		entity.eatSomething(random.randint(1,2))
		# fox.setMessage("もぐもぐ")
		entity.setMessage("ぴこぴこ")
		if entity.isAte():
			if entity.isStomachFull():
				# entity.changeState(Sleep.Sleep())
				entity.getFsm().changeState(Sleep.Sleep())
			else:
				# entity.changeState(FindAndFireSomething.FindAndFireSomething())
				entity.getFsm().changeState(FindAndFireSomething.FindAndFireSomething())

		# random_num = random.randint(0,9)
		# fox.setMessage("もぐもぐ")

		# if random_num % 3 == 0 :
		# 	fox.changeState(Sleep.Sleep())
		# else :
		# 	fox.changeState(SearchSomething.SearchSomething())

	#「」状態に移行する前に一度だけ実行される
	def exit(self, entity):
		pass