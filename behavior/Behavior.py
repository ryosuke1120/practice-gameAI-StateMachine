#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pydot
import box

class Behavior(object):
	
	def __init__(self, name):
		self.name = name
		self.box = box.Box() # 子ビヘイビアはただの配列ではなく「選択方法」を知っている配列でないといけない

	def add_behavior(self, bhv):
		self.box.add_list(bhv)

	def executable(self):
		# 各ビヘイビアは現在の状況で実行可能かどうかを自分自身で宣言する→宣言的手法
		#今回は一旦Trueとしておく
		return True

	def children(self):
		#このBHVobjectのboxが持つBHVobjectらをリターン
		return self.box.get_list()

	def get_name(self):
		return self.name
