#!/usr/bin/env python
# -*- coding: utf-8 -*-

import State
import random
import FindAndFireSomething

#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。
 
class SearchSomething(State.State):

	#SleepまたはEatSomethingから移動してきたときに一回だけ実行される
	def enter(self, entity):
		# if fox.getLocation() != LocationType.Field :
		# 	fox.changeLocation(LocationType.Field)
		# fox.setMessage("捜索を開始します")
		entity.setMessage("活動を開始します")

	#この状態の時に何度も実行される
	#ランダムで取得した数値が3で割り切れる場合、獲物を発見したとして「焼く」状態に移行する
	def execute(self, entity):
		random_num = random.randint(0,9)
		# fox.setMessage("きょろきょろ")
		entity.setMessage("だらだら")

		if random_num % 3 == 0 :
			#fox.changeState(FindAndFireSomething.FindAndFireSomething())
			#entity_type.getFsm().changeState( FindAndFireSomething )
			entity.getFsm().changeState(FindAndFireSomething.FindAndFireSomething())

	#「焼く」状態に移行する前に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("ゲームでもするか")