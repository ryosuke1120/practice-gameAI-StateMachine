#!/usr/bin/env python
# -*- coding: utf-8 -*-

#パッケージはModelを記述？Stateをimport？
from abc import ABCMeta, abstractmethod
#package com.xiao.gameai.gameai.model
#import java.util.*
 
#Stateの実装クラスのひとつ。
#Singletonで状態は持たない。

#object SearchSomething : State 
class SearchSomething(State):
 
    #SleepまたはEatSomethingから移動してきたときに一回だけ実行される
    #override fun enter(fox: Fox) 
    def enter(self, fox):
        if fox.getLocation() != LocationType.Field :
       		fox.changeLocation( LocationType.Field )
        fox.setMessage("捜索を開始します")
 
    #この状態の時に何度も実行される
    #ランダムで取得した数値が3で割り切れる場合、獲物を発見したとして「焼く」状態に移行する
    #override fun execute(fox: Fox) 
    def execute(self, fox):
        val random = Random().nextInt()
        fox.setMessage("きょろきょろ")
 
        if random % 3 === 0 :
        	fox.changeState( FindAndFireSomething )
 
    #「焼く」状態に移行する前に一度だけ実行される
    #override fun exit(fox: Fox) 
    def exit(self, fox):
    	pass
 