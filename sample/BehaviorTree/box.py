#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Box(object):

	def __init__(self):
		self.selector = "確率的選択"
		self.a_list = []

	def add_list(self, bhv):
		self.a_list.append(bhv)

	def get_by_selector(self):
		children = [bhv for bhv in self.a_list if bhv.executable() == True]
		if self.selector in {'確率的選択'}:
			if children != []:
				a_selected_behavior	 = random.choice(children)
			else:
				a_selected_behavior = []
		elif self.selector in {'優先度リスト'}:
			# 優先度の高いもの順（未実装）
			pass
		elif self.selector in {'シーケンシャル'}:
			# 決まった順に（未実装）
			pass
		elif self.selector in {'シーケンシャルルーピング'}:
			# 決まった順に繰り返す（未実装）
			pass
		elif self.selector in {'オンオフ'}:
			# ランダムだけど一度選択したものは選択しない（未実装）
			pass

		return a_selected_behavior

	def get_list(self):
		return self.a_list

