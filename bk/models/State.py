#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# 抽象クラス
class State(object):
    __metaclass__ = ABCMeta

    # # 抽象メソッド
    # @abstractmethod
    # def sample_method(self):
    #     pass

    #状態変更の最初に１回だけ実行される
    @abstractmethod
    def enter(self, fox):
    	pass
 
     #その状態のときに何度も実行される
     #この中でchangeState(新しいState)が呼ばれ、状態が変更される
    @abstractmethod
    def execute(self, fox):
    	pass
 
    #次の状態に移行するときに一度だけ実行される
    @abstractmethod
    def exit(self, fox):
    	pass