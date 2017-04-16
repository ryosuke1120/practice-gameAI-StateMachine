#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

class StateMachine(state.State):

    def __init__(self, m_pOwner, m_pCurrentState ,m_pPreviousState, m_pGlobalState):
        self.m_pOwner = m_pOwner
        self.m_pCurrentState = m_pCurrentState
        self.m_pPreviousState = m_pPreviousState
        self.m_pGlobalState = m_pGlobalState

        self.NOW_ENTER = 0
        self.NOW_EXECUTE = 1
        self.NOW_EXIT = 2
        self.m_nowExecute = self.NOW_ENTER

    #次の処理へ
    #enter() -> execute() -> exit() のメッセージ変更を
    #1ループに一度ずつにするための対応
    def set_next_execute(self):
        self.m_nowExecute = ( self.m_nowExecute + 1 ) % 3

    #entity.update()の処理を移譲したもの
    def update(self):
        #GlobalStateの実装
        if self.m_nowExecute == self.NOW_EXECUTE:
            if self.m_pGlobalState != None:
                self.m_pGlobalState.execute(self.m_pOwner)
            if (self.m_pCurrentState != self.m_pGlobalState) and (self.m_nowExecute == self.NOW_EXECUTE):
                self.m_pCurrentState.execute(self.m_pOwner)
        else:
            self.change_state(self.m_pCurrentState)
 
    #entity.change_state()の処理を移譲したもの
    def change_state(self, pNewState):
        # #現在の状態を保存
        # self.m_pPreviousState = self.m_pCurrentState

        # #終了処理
        # self.m_pCurrentState.exit(self.m_pOwner)

        # #新しい状態に置き換える
        # self.m_pCurrentState = pNewState

        # #開始処理
        # self.m_pCurrentState.enter(self.m_pOwner)
        if self.m_nowExecute == self.NOW_EXECUTE:
            #現在の状態を保存
            self.m_pPreviousState = self.m_pCurrentState
            #終了処理
            self.m_pCurrentState.exit(self.m_pOwner)
            #終了処理モード
            self.set_next_execute()
            #新しい状態に置き換える
            self.m_pCurrentState = pNewState
            #開始処理モードへ
            self.set_next_execute()

        elif self.m_nowExecute == self.NOW_ENTER :
            #開始処理
            self.m_pCurrentState.enter(self.m_pOwner)
            #処理モードへ
            self.set_next_execute()
 
    #もとの状態に戻す（GlobalStateから呼ばれる）
    def revert_to_previous_state(self):
        self.change_state(self.m_pPreviousState)

    def handle_message(self, msg):
        #ステートが有効で、メッセージを処理できる状態かを調べる
        if self.m_nowExecute == self.NOW_EXECUTE :
            self.m_pCurrentState.on_message(self.m_pOwner, msg)
            return True
        return False