#!/usr/bin/env python
# -*- coding: utf-8 -*-

#お肉が焼けたならば（isDonenessFull = true）→EatSomething

import State
import random
import EatSomething

class FindAndFireSomething(State.State):

	#SearchSomethingから遷移した際に一回だけ実行される
	def enter(self, entity):
		# if entity.getLocation() != LocationType.Field :
		# 	entity.changeLocation(LocationType.Field)
		# entity.setMessage("発見したのできつね色に焼きます")
		entity.setMessage("ゲームの準備をします")
		entity.setGameSize(random.randint(5,10))

	#条件が満たされるまで実行される
	def execute(self, entity):
		entity.fireSomething(random.randint(1,2))
		# entity.setMessage("じゅーじゅー")
		entity.setMessage("がちゃがちゃ")
		#ビヘイビアツリーによる行動
		#entity.setMessage(entity.conflict_act())
		#ニューラルネットワークによる行動
		entity.train_act()	
		if entity.isDonenessFull():
			#entity.changeState(EatSomething.EatSomething())
			entity.getFsm().changeState(EatSomething.EatSomething())

	#EatSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		entity.setMessage("よし、準備できた")