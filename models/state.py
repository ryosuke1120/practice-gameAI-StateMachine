#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

#abstract class
class State(object):
    __metaclass__ = ABCMeta

    #状態変更の最初に１回だけ実行される
    @abstractmethod
    def enter(self, state_t):
        pass

     #その状態のときに何度も実行される
     #この中でchangeState(新しいState)が呼ばれ、状態が変更される
    @abstractmethod
    def execute(self, state_t):
        pass

    #次の状態に移行するときに一度だけ実行される
    @abstractmethod
    def exit(self, state_t):
        pass

    #メッセージディスパッチャからメッセージを受け取ったら実行する
    @abstractmethod
    def onMessage(self, entity_type, telegram):
        pass