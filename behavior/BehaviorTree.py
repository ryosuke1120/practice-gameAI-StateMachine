#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Behavior

#要最適化
class BehaviorTree(object):

	def __init__(self):
		self.root = Behavior.Behavior("<root>")
		a = Behavior.Behavior("交戦")
		b = Behavior.Behavior("撃退")
		c = Behavior.Behavior("休憩")

		a_a = Behavior.Behavior("攻撃")
		a_b = Behavior.Behavior("防御")
		b_a = Behavior.Behavior("足止めする")
		b_b = Behavior.Behavior("逃走する")
		c_a = Behavior.Behavior("立ち止まる")
		c_b = Behavior.Behavior("回復する")

		a_a_a = Behavior.Behavior("剣を振る")
		a_a_b = Behavior.Behavior("攻撃魔法")
		a_a_c = Behavior.Behavior("盾で剣をはじく")
		a_b_a = Behavior.Behavior("一歩後退する")
		a_b_b = Behavior.Behavior("盾で身を隠す")
		b_a_a = Behavior.Behavior("トラップをしかける")
		b_a_b = Behavior.Behavior("弓矢を放つ")
		c_b_a = Behavior.Behavior("回復魔法")
		c_b_b = Behavior.Behavior("回復薬を飲む")

		a_a_b_a = Behavior.Behavior("召喚A")
		a_a_b_b = Behavior.Behavior("召喚B")


		a_a_b.add_behavior(a_a_b_a)
		a_a_b.add_behavior(a_a_b_b)

		a_a.add_behavior(a_a_a)
		a_a.add_behavior(a_a_b)
		a_a.add_behavior(a_a_c)
		a_b.add_behavior(a_b_a)
		a_b.add_behavior(a_b_b)
		b_a.add_behavior(b_a_a)
		b_a.add_behavior(b_a_b)
		c_b.add_behavior(c_b_a)
		c_b.add_behavior(c_b_b)

		a.add_behavior(a_a)
		a.add_behavior(a_b)
		b.add_behavior(b_a)
		b.add_behavior(b_b)
		c.add_behavior(c_a)
		c.add_behavior(c_b)

		self.root.add_behavior(a)
		self.root.add_behavior(b)
		self.root.add_behavior(c)

	def get_behavior(self):
		behavior_list = []
		node = self.root
		while True:
			#break if node.children.empty?
			if node.children() != []: 
				node = node.box.get_by_selector()
				behavior_list.append(node.get_name())
			else:
				break

		return behavior_list

if __name__ == "__main__":
	behavior_tree = BehaviorTree()
	print(behavior_tree.get_behavior())
	