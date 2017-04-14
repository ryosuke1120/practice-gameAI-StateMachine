#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base_game_entity
import search_state
import state_machine
import sleep_state
import fox_global_state
import behavior_tree

import neural

class Fox(base_game_entity.BaseGameEntity): 

	def __init__(self, m_ID, m_STOMACH_SIZE):

		self.m_ID = m_ID
		self.m_STOMACH_SIZE = m_STOMACH_SIZE
		#現在の状態を保持
		#self.m_pCurrentState = SearchSomething.SearchSomething()
		#self.m_pStateMachine = StateMachine.StateMachine(self, SearchSomething.SearchSomething(), Sleep.Sleep(), None)
		self.m_pStateMachine = state_machine.StateMachine(self, search_state.SearchState(), sleep_state.SleepState(), fox_global_state.FoxGlobalState())

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

		#FoxのBehaviorTree（BehaviorTreehaは現状Fox専用のクラス）
		self.behavior_tree = behavior_tree.BehaviorTree()

		#Foxのニューラルネットワーク（neuralはFoxの専用クラス）
		self.neural = neural.Neural()

	#ループで実行される
	def update(self):
		#self.m_pCurrentState.execute(self)
		self.m_pStateMachine.update()

	#状態を変更するときにStateの実装クラス（SearchSomethingなど）から呼ばれる
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
	#Stateの実装クラスであるFindAndFireSomethingから呼ばれる
	def isDonenessFull(self):
		if self.m_donenessLevel <= 0:
			return True
		else:
			return False

	#焼く
	#FindAndFireSomethingから呼ばれる
	def fireSomething(self, fireCount):
		self.m_donenessLevel -= fireCount

	#食べる
	#EatSomethingから呼ばれる
	def eatSomething(self, eatCount):
		self.m_eatSize -= eatCount
		self.m_nowStomachDegree += eatCount

	#食べ終わったかどうかを返す
	#EatSomethingから呼ばれる
	def isAte(self):
		if self.m_eatSize <= 0:
			return True
		else:
			return False

	#お腹がいっぱいかどうかを返す
	#EatSomethingからSleep・SearchSomethingのどちらに移行するかを判定する際に呼ばれる
	def isStomachFull(self):
		if self.m_nowStomachDegree >= self.m_STOMACH_SIZE:
			return True
		else: 
			return False

	#消化
	#Sleepから呼ばれる
	def digestSomething(self, digestCount):
		self.m_nowStomachDegree -= digestCount

	#お腹がすいたかどうかを返す
	#SleepからSearchSomethingに移行するかの判定で呼ばれる
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
	#MainActivityから呼ばれる
	def getMessage(self):
		return self.m_message

	#メッセージを設定する
	def setMessage(self, newMessage):
		self.m_message = newMessage

	#ステートがconflictの際のaction
	def conflict_act(self):
		action_list = self.behavior_tree.get_conflict_behavior()
		# print("conflict", action_list)
		return action_list

	#ステートがeffortの際のaction
	def effort_act(self):
		action_list = self.behavior_tree.get_effort_behavior()
		# print("effort", action_list)
		return action_list

	#neuralを取得する
	def get_neural(self):
		return self.neural

	#neural行動を起こし、学習する
	def train_act(self):
		self.get_neural().train()

	#--------------------未実装--------------------

	# #get next precept p
	# def get_next_precept(self):
	# 	pass

	# #世界を観察する
	# def observe(self):
	# 	pass

	# #belief revision function
	# #Beliefs : エージェントが世界について持っている情報
	# def belief(self, initial_belief, precept):
	# 	# return belief
	# 	pass

	# #beliefsとinitial_intentionsからdesiresを返す
	# #Desires : 理想的な世界の代理人がもたらしたいと望んでいる事柄の状態
	# def options(self, belief, initial_intentions):
	# 	# return desire
	# 	pass

	# #beliefからintentionsをかえす
	# #Intentions : エージェントが達成することを約束した欲求 
	# def filter(self, belief):
	# 	#return intention
	# 	pass

	# #beliefとintentionから実行すべき内容を計画(pi)する
	# def plan(self, belief, intention):
	# 	# return action_list
	# 	pass

	# #Piを実行する
	# def execute_pi(self, pi):
	# 	pass



