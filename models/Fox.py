#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BaseGameEntity
import SearchSomething
import StateMachine
import Sleep
import FoxGlobalState

#キツネの状態を持つ

class Fox(BaseGameEntity.BaseGameEntity): 

	def __init__(self, m_ID, m_STOMACH_SIZE):

		self.m_ID = m_ID
		self.m_STOMACH_SIZE = m_STOMACH_SIZE
		#現在の状態を保持
		#self.m_pCurrentState = SearchSomething.SearchSomething()
		#private var m_pStateMachine = StateMachine<Fox>( this, SearchSomething, Sleep, null )
		#self.m_pStateMachine = StateMachine.StateMachine(self, SearchSomething.SearchSomething(), Sleep.Sleep(), None)
		#private var m_pStateMachine = StateMachine<Fox>( this, SearchSomething, Sleep, FoxGlobalState )
		self.m_pStateMachine = StateMachine.StateMachine(self, SearchSomething.SearchSomething(), Sleep.Sleep(), FoxGlobalState.FoxGlobalState())

		#現在のお腹の空き具合：0が空腹状態
		self.m_nowStomachDegree = 5

		#獲物の焼き具合：0になると焼き切った状態
		self.m_donenessLevel = 0

		#獲物の大きさ（大きいほど食べるのに時間がかかる）
		self.m_eatSize = 0

		#TODO 今いる場所（今回は利用しない）一旦文字列代入
		self.m_location = "LocationType.Field"

		#TODO 表示するメッセージ（今後メッセージではなく画像等に変更されるもの）
		self.m_message = "焼けるものを探します"

#------------------------------------------------------------------------------------------------------------------------------------

	#ループで実行される
	def update(self):
		#self.m_pCurrentState.execute(self)
		self.m_pStateMachine.update()

	#状態を変更するときにStateの実装クラス（SearchSomething.ktなど）から呼ばれる
	# def changeState(self, pNewState):
	# 	#現在のステートのexit処理
	# 	self.m_pCurrentState.exit(self)

	# 	#新しいステートに変更し、enter処理
	# 	self.m_pCurrentState = pNewState
	# 	self.m_pCurrentState.enter(self)
	def getFsm(self):
		return self.m_pStateMachine

	#現在のロケーションを返す
	#Stateの実装クラスから呼ばれる
	def getLocation(self): 
		LocationType = self.m_location

	#ロケーションを変更する
	#Stateの実装クラスから呼ばれる
	def changeLocation(self, newLocation):
		self.m_location = newLocation

	#焼き終わったかを返す
	#Stateの実装クラスであるFindAndFireSomething.ktから呼ばれる
	def isDonenessFull(self):
		if self.m_donenessLevel <= 0:
			return True
		else:
			return False

	#焼く
	def fireSomething(self, fireCount):
		self.m_donenessLevel -= fireCount

	#食べる
	def eatSomething(self, eatCount):
		self.m_eatSize -= eatCount
		self.m_nowStomachDegree += eatCount

	#食べ終わったかどうかを返す
	def isAte(self):
		if self.m_eatSize <= 0:
			return True
		else:
			return False

	#お腹がいっぱいかどうかを返す
	#（EatSomethingからSleep・SearchSomethingのどちらに移行するかを判定する際に呼ばれる）
	def isStomachFull(self):
		if self.m_nowStomachDegree >= self.m_STOMACH_SIZE:
			return True
		else: 
			return False

	#消化 
	def digestSomething(self, digestCount):
		self.m_nowStomachDegree -= digestCount

	#お腹がすいたかどうかを返す
	#（SleepからSearchSomethingに移行するかの判定で呼ばれる）
	def isHungry(self):
		if self.m_nowStomachDegree <= 0:
			return True
		else: 
			return False

	#お腹の空き具合を変更する
	def changeNowStomachDegree(self, changeCount):
		self.m_nowStomachDegree += changeCount

	#獲物の大きさから、どれくらい焼けば良いのか・食べたらどれくらい満たされるのかを設定する
	def setGameSize(self, size):
		self.m_donenessLevel = size
		self.m_eatSize = size

	#メッセージを取得する
	#（MainActivityから呼ばれる）
	def getMessage(self):
		return self.m_message

	#メッセージを設定する
	def setMessage(self, newMessage):
		self.m_message = newMessage
