#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


# 抽象クラス
class AbstractBaseSampleClass(object):
    __metaclass__ = ABCMeta


    # # 抽象メソッド
    # @abstractmethod
    # def sample_method(self):
    #     pass

    #状態変更の最初に１回だけ実行される
    #fun enter( fox: Fox )
    @abstractmethod
    def enter(self, fox):
    	pass
 
     #その状態のときに何度も実行される
     #この中でFox.changeState(新しいState)が呼ばれ、状態が変更される
     #fun execute( fox: Fox )
     @abstractmethod
    def execute(self, fox):
    	pass
 
    #次の状態に移行するときに一度だけ実行される
    #fun exit( fox: Fox )
    @abstractmethod
    def exit(self, fox)
    	pass

 #--------------------------------------------------------------------------


# 抽象クラスのサブクラス (ただし抽象メソッドを実装しない)
class AbstractSubClass(AbstractBaseSampleClass):
    pass


# 更にそのサブクラス (今度は抽象メソッドを実装する)
class ConcreteClass(AbstractSubClass):

    # 抽象メソッドの実装
    def sample_method(self):
        super(ConcreteClass, self).sample_method()
        print('Concrete')

if __name__ == '__main__':
    # AbstractBaseSampleClass() # TypeError (抽象メソッドが残っている)
    # AbstractSubClass() # TypeError (抽象メソッドが残っている)
    ConcreteClass().sample_method()  # OK