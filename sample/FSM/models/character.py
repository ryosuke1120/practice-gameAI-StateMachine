#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base_game_entity
import state_a
import state_machine
import state_d
import character_global_state


class Character(base_game_entity.BaseGameEntity):

    def __init__(self, m_ID, m_STOMACH_SIZE):

        self.m_ID = m_ID
        self.m_STOMACH_SIZE = m_STOMACH_SIZE

        self.m_pStateMachine = state_machine.StateMachine(self, state_a.StateA(
        ), state_d.StateD(), character_global_state.CharacterGlobalState())

        self.m_nowStomachDegree = 5

        self.m_donenessLevel = 0

        self.m_eatSize = 0

        self.m_location = "LocationType.Field"

        self.m_message = "初期メッセージ"

    def update(self):
        self.m_pStateMachine.update()

    def getFsm(self):
        return self.m_pStateMachine

    def getLocation(self):
        LocationType = self.m_location

    def changeLocation(self, newLocation):
        self.m_location = newLocation

    def isDonenessFull(self):
        if self.m_donenessLevel <= 0:
            return True
        else:
            return False

    def fireSomething(self, fireCount):
        self.m_donenessLevel -= fireCount

    def eatSomething(self, eatCount):
        self.m_eatSize -= eatCount
        self.m_nowStomachDegree += eatCount

    def isAte(self):
        if self.m_eatSize <= 0:
            return True
        else:
            return False

    def isStomachFull(self):
        if self.m_nowStomachDegree >= self.m_STOMACH_SIZE:
            return True
        else:
            return False

    def digestSomething(self, digestCount):
        self.m_nowStomachDegree -= digestCount

    def isHungry(self):
        if self.m_nowStomachDegree <= 0:
            return True
        else:
            return False

    def changeNowStomachDegree(self, changeCount):
        self.m_nowStomachDegree += changeCount

    def setGameSize(self, size):
        self.m_donenessLevel = size
        self.m_eatSize = size

    def getMessage(self):
        return self.m_message

    def setMessage(self, newMessage):
        self.m_message = newMessage
