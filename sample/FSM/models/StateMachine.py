#!/usr/bin/env python
# -*- coding: utf-8 -*-

# package com.xiao.gameai.gameai.model
import State

#状態に関するデータ・処理をカプセル化したクラス。



# class StateMachine<T>(
#         val m_pOwner         : T,
#         var m_pCurrentState  : State<T>,
#         var m_pPreviousState : State<T>,
#         var m_pGlobalState   : State<T>?
# ) {
class StateMachine(State.State):

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
    # private fun setNextExecute() {
    #     m_nowExecute = ( m_nowExecute + 1 ) % 3
    # }
    def setNextExecute(self):
        self.m_nowExecute = ( self.m_nowExecute + 1 ) % 3

    #Fox.update()の処理を移譲したもの
    def update(self):
        #グローバルステートの実装。
        #ない場合はnullが入るが、KotlinのNull安全によりifとかやらなくても大丈夫！
        if self.m_nowExecute == self.NOW_EXECUTE:
            if self.m_pGlobalState != None:
                self.m_pGlobalState.execute(self.m_pOwner)
                if (self.m_pCurrentState != self.m_pGlobalState) and (self.m_nowExecute == self.NOW_EXECUTE):
                    self.m_pCurrentState.execute(self.m_pOwner)
        else:
            self.changeState(self.m_pCurrentState)

    # if( m_nowExecute === NOW_EXECUTE ) {
    #     m_pGlobalState?.execute(m_pOwner)

    #     // グローバルステート処理中じゃない場合のみ実行
    #     if( m_pCurrentState !== m_pGlobalState && m_nowExecute === NOW_EXECUTE ) {
    #         m_pCurrentState.execute(m_pOwner)
    #     }
    # }
    # else {
    #     changeState( m_pCurrentState )
    # }

 
    #Fox.changeState()の処理を移譲したもの
    def changeState(self, pNewState):
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
            self.setNextExecute()
            #新しい状態に置き換える
            self.m_pCurrentState = pNewState
            #開始処理モードへ
            self.setNextExecute()

        elif self.m_nowExecute == self.NOW_ENTER :
            #開始処理
            self.m_pCurrentState.enter(self.m_pOwner)
            #処理モードへ
            self.setNextExecute()

        # if( m_nowExecute === NOW_EXECUTE ) {
        #     // 現在の状態を保存
        #     m_pPreviousState = m_pCurrentState

        #     // 終了処理
        #     m_pCurrentState.exit(m_pOwner)

        #     // 終了処理モード
        #     setNextExecute()

        #     // 新しい状態に置き換える
        #     m_pCurrentState = pNewState

        #     // 開始処理モードへ
        #     setNextExecute()
        # }
        # else if( m_nowExecute === NOW_ENTER ){
        #     // 開始処理
        #     m_pCurrentState.enter( m_pOwner )

        #     // 処理モードへ
        #     setNextExecute()
        # }
    
 
    #もとの状態に戻す（グローバルステートから呼ばれる）
    def revertToPreviousState(self):
        self.changeState(self.m_pPreviousState)
