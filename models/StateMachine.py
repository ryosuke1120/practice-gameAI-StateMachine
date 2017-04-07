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

 
    #Fox.update()の処理を移譲したもの
    def update(self):
        #グローバルステートの実装。
        #ない場合はnullが入るが、KotlinのNull安全によりifとかやらなくても大丈夫！
        if self.m_pGlobalState != None:
            self.m_pGlobalState.execute(self.m_pOwner)
        else:
            #グローバルステート処理中じゃない場合のみ実行
            if self.m_pCurrentState != self.m_pGlobalState :
                self.m_pCurrentState.execute(self.m_pOwner)
 
    #Fox.changeState()の処理を移譲したもの
    def changeState(self, pNewState):
        #現在の状態を保存
        self.m_pPreviousState = self.m_pCurrentState

        #終了処理
        self.m_pCurrentState.exit(self.m_pOwner)

        #新しい状態に置き換える
        self.m_pCurrentState = pNewState

        #開始処理
        self.m_pCurrentState.enter(self.m_pOwner)
    
 
    #もとの状態に戻す（グローバルステートから呼ばれる）
    def revertToPreviousState(self):
        changeState(self.m_pPreviousState)
