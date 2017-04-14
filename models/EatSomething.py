#!/usr/bin/env python
# -*- coding: utf-8 -*-

#食事をするState
#お腹が満たされているなら（isStomachFull = true）→SleepState
#お腹が満たされていないなら（else）→SearchSomethingState

import State
import random
import SearchSomething
import Sleep
import FindAndFireSomething

class EatSomething(State.State):

	#FindAndFireSomethingから遷移した際に一度だけ実行される
	def enter(self, entity):
		# if entity.getLocation() != LocationType.Field :
		# 	entity.changeLocation(LocationType.Field)
		# entity.setMessage("食べます")
		entity.setMessage("スプラトゥーンをします")

	#条件が満たされるまで実行される
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

	#Sleepもしくは、SearchSomethingに遷移する際に一度だけ実行される
	def exit(self, entity):
		if entity.isStomachFull():
			# entity.changeState(Sleep.Sleep())
			entity.setMessage("疲れたし、寝よう")
		else:
			entity.setMessage("うーん、まだゲームしたい")