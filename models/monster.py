#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state_machine
import base_game_entity
import walk_state
import return_state


# 少女の前に突如現れたモンスター
class Monster(base_game_entity.BaseGameEntity):
    def __init__(self, message_dispatcher, m_ID, m_size, m_STOMACH_SIZE):
        self.message_dispatcher = message_dispatcher
        self.m_ID = m_ID
        self.m_size = m_size
        self.stamina = self.m_size * 1
        self.m_STOMACH_SIZE = m_STOMACH_SIZE
        # 表示するメッセージ（今後メッセージではなく画像等に変更されるもの）
        self.m_message = "init"

        # 現在の状態を保持
        self.m_pStateMachine = state_machine.StateMachine(
            self, walk_state.WalkState(), return_state.ReturnState(), None)

        # #焼かれ具合。m_sizeにより焼かれ具合が変わる
        # self.m_donenessLevel = 0#DonenessLevel.DONENESS_UNDER.level

    # 	#存在場所
    # 	self.m_location = LocationType.Field

    # #場所を変更
    # def changeLocation(seld, newLocation):
    # 	self.m_location = newLocation

    # 体力を消費する
    def consume(self, consumed):
        self.stamina -= consumed

    # 体力を回復する
    def recover(self, recovered):
        self.stamina += recovered

    def is_stamina_less(self):
        if self.stamina <= 0:
            return True
        else:
            return False

    # StateMachineを取得する
    def get_fsm(self):
        return self.m_pStateMachine

    # ループで実行される
    def update(self):
        # self.m_pCurrentState.execute(self)
        self.m_pStateMachine.update()

    # #少女に焼かれたときの処理
    # def fired(self, fired):
    # 	firedPercent = int( ( float(fired) / float(self.m_size) ) * 100 )
    # 	if firedPercent >= 95:
    # 		m_donenessLevel = 3#DonenessLevel.DONENESS_BURNED.level
    # 	elif firedPercent >= 70:
    # 		m_donenessLevel = 2#DonenessLevel.DONENESS_GOLDEN_BROWN.level
    # 	else:
    # 		m_donenessLevel = 1#DonenessLevel.DONENESS_UNDER.level

    def handle_message(self, msg):
        return self.get_fsm().handle_message(msg)

    # メッセージを取得する
    # MainActivityから呼ばれる
    def get_message(self):
        return self.m_message

    # メッセージを設定する
    def set_message(self, new_message):
        self.m_message = new_message
