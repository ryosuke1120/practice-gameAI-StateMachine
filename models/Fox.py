# -*- coding: utf-8 -*-

#package com.xiao.gameai.gameai.model
from .BaseGameEntity import BaseGameEntity
from .SearchSomething import SearchSomething

#キツネの状態を持つ

#class Fox( m_ID : Int, val m_STOMACH_SIZE : Int ) : BaseGameEntity( m_ID ) {
# class Fox(BaseGameEntity, m_ID, m_STOMACH_SIZE): 
class Fox(BaseGameEntity): 

	def __init__(self, m_ID, m_STOMACH_SIZE):

		self.m_ID = m_ID
		self.m_STOMACH_SIZE = m_STOMACH_SIZE
		#現在の状態を保持
		# private var m_pCurrentState : State = SearchSomething
		self.m_pCurrentState = SearchSomething()

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

	#ループで実行される
	# override fun update() {
	#     m_pCurrentState.execute(this)
	# }
	def update(self):
		self.m_pCurrentState.execute(self)

	#状態を変更するときにStateの実装クラス（SearchSomething.ktなど）から呼ばれる
	# fun changeState( pNewState: State ){
	#     // 現在のステートのexit処理
	#     m_pCurrentState.exit(this)

	#     // 新しいステートに変更し、enter処理
	#     m_pCurrentState = pNewState
	#     m_pCurrentState.enter(this)
	# }
	def changeState(self, pNewState):
		#現在のステートのexit処理
		self.m_pCurrentState.exit(this)

		#新しいステートに変更し、enter処理
		self.m_pCurrentState = pNewState
		self.m_pCurrentState.enter(this)

	#現在のロケーションを返す
	#Stateの実装クラスから呼ばれる
	# fun getLocation(): LocationType = m_location
	def getLocation(self): 
		LocationType = self.m_location

	#ロケーションを変更する
	#Stateの実装クラスから呼ばれる
	# fun changeLocation( newLocation : LocationType ) {
	#     m_location = newLocation
	# }
	def changeLocation(self, newLocation):
		self.m_location = newLocation

	#焼き終わったかを返す
	#Stateの実装クラスであるFindAndFireSomething.ktから呼ばれる
	# fun isDonenessFull() = if( m_donenessLevel <= 0 ) true else false
	def isDonenessFull(self):
		if self.m_donenessLevel <= 0:
			return True
		else:
			return False

	#焼く
	# fun fireSomething( fireCount : Int ){
	#     m_donenessLevel -= fireCount
	# }
	def fireSomething(self, fireCount):
		self.m_donenessLevel -= fireCount

	#食べる
	# fun eatSomething( eatCount : Int ){
	#     m_eatSize -= eatCount
	#     m_nowStomachDegree += eatCount
	# }
	def eatSomething(self, eatCount):
		self.m_eatSize -= eatCount
		self.m_nowStomachDegree += eatCount

	#食べ終わったかどうかを返す
	# fun isAte() = if( m_eatSize <= 0 ) true else false
	def isAte(self):
		if self.m_eatSize <= 0:
			return True
		else:
			return False

	#お腹がいっぱいかどうかを返す
	#（EatSomethingからSleep・SearchSomethingのどちらに移行するかを判定する際に呼ばれる）
	# fun isStomachFull() = if( m_nowStomachDegree >= m_STOMACH_SIZE ) true else false
	def isStomachFull(self):
		if self.m_nowStomachDegree >= m_STOMACH_SIZE:
			return True
		else: 
			return False

	#お腹がすいたかどうかを返す
	#（SleepからSearchSomethingに移行するかの判定で呼ばれる）
	# fun isHungry() = if( m_nowStomachDegree <= 0 ) true else false
	def isHungry(self):
		if self.m_nowStomachDegree <= 0:
			return True
		else: 
			return False

	#お腹の空き具合を変更する
	# fun changeNowStomachDegree( changeCount : Int ){
	#     m_nowStomachDegree += changeCount
	# }
	def changeNowStomachDegree(self, changeCount):
		self.m_nowStomachDegree += changeCount

	#獲物の大きさから、どれくらい焼けば良いのか・食べたらどれくらい満たされるのかを設定する
	# fun setGameSize( size : Int ){
	#     m_donenessLevel = size
	#     m_eatSize = size
	# }
	def setGameSize(self, size):
		self.m_donenessLevel = size
		self.m_eatSize = size

	#メッセージを取得する
	#（MainActivityから呼ばれる）
	# fun getMessage() = m_message
	def getMessage(self):
		return self.m_message

	#メッセージを設定する
	# fun setMessage( newMessage : String ){
	#     this.m_message = newMessage
	# }
	def setMessage(self, newMessage):
		self.m_message = newMessage
