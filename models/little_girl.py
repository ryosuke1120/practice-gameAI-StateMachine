#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base_game_entity
import stroll_state
import state_machine
import sleep_state
import little_girl_global_state
import behavior_tree
import inspect

import neural


class LittleGirl(base_game_entity.BaseGameEntity):

    def __init__(self, message_dispatcher, m_ID, m_STOMACH_SIZE):

        self.message_dispatcher = message_dispatcher
        self.m_ID = m_ID
        self.m_STOMACH_SIZE = m_STOMACH_SIZE
        # 現在の状態を保持
        #self.m_pCurrentState = SearchSomething.SearchSomething()
        #self.m_pStateMachine = StateMachine.StateMachine(self, SearchSomething.SearchSomething(), Sleep.Sleep(), None)
        self.m_pStateMachine = state_machine.StateMachine(
            self,
            stroll_state.StrollState(),
            sleep_state.SleepState(),
            little_girl_global_state.LittleGirlGlobalState())

        # 現在のお腹の空き具合：0が空腹状態
        self.m_nowStomachDegree = 5

        # 現在の心の具合：0が疲れた状態
        self.m_nowMentalHealth = 5

        # 現在の体力の具合：0が疲れた状態
        self.m_nowStamina = 5

        # 獲物の焼き具合：0になると焼き切った状態
        self.m_donenessLevel = 0

        # 獲物の大きさ（大きいほど食べるのに時間がかかる）
        self.m_eatSize = 0

        # # 今いる場所（未使用）
        # self.m_location = "LocationType.Field"

        # 表示するメッセージ（今後メッセージではなく画像等に変更されるもの）
        self.m_message = "焼けるものを探します"

        # FoxのBehaviorTree（BehaviorTreehaは現状Fox専用のクラス）
        self.behavior_tree = behavior_tree.BehaviorTree()

        # Foxのニューラルネットワーク（neuralはFoxの専用クラス）
        self.neural = neural.Neural()

    # ループで実行される
    def update(self):
        # self.m_pCurrentState.execute(self)
        self.m_pStateMachine.update()

    # 状態を変更するときにStateの実装クラス（SearchSomethingなど）から呼ばれる
    # def changeState(self, pNewState):
    # 	#現在のステートのexit処理
    # 	self.m_pCurrentState.exit(self)

    # 	#新しいステートに変更し、enter処理
    # 	self.m_pCurrentState = pNewState
    # 	self.m_pCurrentState.enter(self)
    def get_fsm(self):
        return self.m_pStateMachine

    # #現在のロケーションを返す
    # #Stateの実装クラスから呼ばれる
    # def getLocation(self):
    # 	LocationType = self.m_location

    # #ロケーションを変更する
    # #Stateの実装クラスから呼ばれる
    # def changeLocation(self, newLocation):
    # 	self.m_location = newLocation

    # #焼き終わったかを返す
    # #Stateの実装クラスであるFindAndFireSomethingから呼ばれる
    # def isDonenessFull(self):
    # 	if self.m_donenessLevel <= 0:
    # 		return True
    # 	else:
    # 		return False

    # #焼く
    # #FindAndFireSomethingから呼ばれる
    # def fireSomething(self, fireCount):
    # 	self.m_donenessLevel -= fireCount

    # #食べる
    # #EatSomethingから呼ばれる
    # def eatSomething(self, eatCount):
    # 	self.m_eatSize -= eatCount
    # 	self.m_nowStomachDegree += eatCount

    # #食べ終わったかどうかを返す
    # #EatSomethingから呼ばれる
    # def isAte(self):
    # 	if self.m_eatSize <= 0:
    # 		return True
    # 	else:
    # 		return False

    # #お腹がいっぱいかどうかを返す
    # #EatSomethingからSleep・SearchSomethingのどちらに移行するかを判定する際に呼ばれる
    # def isStomachFull(self):
    # 	if self.m_nowStomachDegree >= self.m_STOMACH_SIZE:
    # 		return True
    # 	else:
    # 		return False

    # 精神消費
    def stress(self, stress):
        self.m_nowMentalHealth -= stress

    # 精神回復
    def recover_mental(self, recover):
        self.m_nowMentalHealth += recover

    # 心が回復したかどうかを返す
    def is_mental_good(self):
        if self.m_nowMentalHealth >= 10:
            return True
        else:
            return False

    # 心が消耗しきったかどうかを返す
    def is_mental_bad(self):
        if self.m_nowMentalHealth <= 0:
            return True
        else:
            return False

    # 体力消費
    def exhaust(self, exhaust):
        self.m_nowStamina -= exhaust

    # 体力回復
    def recover_stamina(self, stamina):
        self.m_nowStamina += stamina

    # 体力が回復したかどうかを返す
    def is_stamina_good(self):
        if self.m_nowStamina >= 5:
            return True
        else:
            return False

    # 体力が消耗しきったかどうかを返す
    def is_stamina_bad(self):
        if self.m_nowStamina <= 0:
            return True
        else:
            return False

    # #お腹の空き具合を変更する
    # def changeNowStomachDegree(self, changeCount):
    # 	self.m_nowStomachDegree += changeCount

    # 獲物の大きさから、どれくらい焼けば良いのか・食べたらどれくらい満たされるのかを設定する
    def set_game_size(self, size):
        self.m_donenessLevel = size
        self.m_eatSize = size

    # メッセージを取得する
    # MainActivityから呼ばれる
    def get_message(self):
        return self.m_message

    # メッセージを設定する
    def set_message(self, new_message):
        self.m_message = new_message

    # ステートがconflictの際のaction
    def conflict_act(self):
        action_list = self.behavior_tree.get_conflict_behavior()
        # print("conflict", action_list)
        return action_list

    # ステートがeffortの際のaction
    def effort_act(self):
        action_list = self.behavior_tree.get_effort_behavior()
        # print("effort", action_list)
        return action_list

    # neuralを取得する
    def get_neural(self):
        return self.neural

    # neural行動を起こし、学習する
    def train_act(self):
        self.get_neural().train()

    def handle_message(self, msg):
        return self.get_fsm().handle_message(msg)
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
