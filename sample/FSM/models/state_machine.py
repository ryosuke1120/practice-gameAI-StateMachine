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

    def setNextExecute(self):
        self.m_nowExecute = ( self.m_nowExecute + 1 ) % 3

    def update(self):
        if self.m_nowExecute == self.NOW_EXECUTE:
            if self.m_pGlobalState != None:
                self.m_pGlobalState.execute(self.m_pOwner)
                if (self.m_pCurrentState != self.m_pGlobalState) and (self.m_nowExecute == self.NOW_EXECUTE):
                    self.m_pCurrentState.execute(self.m_pOwner)
        else:
            self.changeState(self.m_pCurrentState)

    def changeState(self, pNewState):

        if self.m_nowExecute == self.NOW_EXECUTE:
            self.m_pPreviousState = self.m_pCurrentState
            self.m_pCurrentState.exit(self.m_pOwner)
            self.setNextExecute()
            self.m_pCurrentState = pNewState
            self.setNextExecute()

        elif self.m_nowExecute == self.NOW_ENTER :
            self.m_pCurrentState.enter(self.m_pOwner)
            self.setNextExecute()
 
    def revertToPreviousState(self):
        self.changeState(self.m_pPreviousState)
