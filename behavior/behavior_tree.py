#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behavior import behavior

#要最適化
class BehaviorTree(object):

	def __init__(self):
		self.root_conflict = behavior.Behavior("<root>")
		a = behavior.Behavior("交戦")
		b = behavior.Behavior("撃退")
		c = behavior.Behavior("休憩")

		a_a = behavior.Behavior("攻撃")
		a_b = behavior.Behavior("防御")
		b_a = behavior.Behavior("足止めする")
		b_b = behavior.Behavior("逃走する")
		c_a = behavior.Behavior("立ち止まる")
		c_b = behavior.Behavior("回復する")

		a_a_a = behavior.Behavior("剣を振る")
		a_a_b = behavior.Behavior("攻撃魔法")
		a_a_c = behavior.Behavior("盾で剣をはじく")
		a_b_a = behavior.Behavior("一歩後退する")
		a_b_b = behavior.Behavior("盾で身を隠す")
		b_a_a = behavior.Behavior("トラップをしかける")
		b_a_b = behavior.Behavior("弓矢を放つ")
		c_b_a = behavior.Behavior("回復魔法")
		c_b_b = behavior.Behavior("回復薬を飲む")

		a_a_b_a = behavior.Behavior("召喚A")
		a_a_b_b = behavior.Behavior("召喚B")

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

		self.root_conflict.add_behavior(a)
		self.root_conflict.add_behavior(b)
		self.root_conflict.add_behavior(c)

		self.root_effort = behavior.Behavior("<root>")
		a = behavior.Behavior("交戦")
		b = behavior.Behavior("撃退")
		c = behavior.Behavior("休憩")

		a_a = behavior.Behavior("攻撃")
		a_b = behavior.Behavior("防御")
		b_a = behavior.Behavior("足止めする")
		b_b = behavior.Behavior("逃走する")
		c_a = behavior.Behavior("立ち止まる")
		c_b = behavior.Behavior("回復する")

		a_a_a = behavior.Behavior("剣を振る")
		a_a_b = behavior.Behavior("攻撃魔法")
		a_a_c = behavior.Behavior("盾で剣をはじく")
		a_b_a = behavior.Behavior("一歩後退する")
		a_b_b = behavior.Behavior("盾で身を隠す")
		b_a_a = behavior.Behavior("トラップをしかける")
		b_a_b = behavior.Behavior("弓矢を放つ")
		c_b_a = behavior.Behavior("回復魔法")
		c_b_b = behavior.Behavior("回復薬を飲む")

		a_a_b_a = behavior.Behavior("召喚A")
		a_a_b_b = behavior.Behavior("召喚B")

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

		self.root_effort.add_behavior(a)
		self.root_effort.add_behavior(b)
		self.root_effort.add_behavior(c)

	def get_conflict_behavior_tree_node(self):
		return self.root_conflict

	def get_effort_behavior_tree_node(self):
		return self.root_effort

	def get_conflict_behavior(self):
		behavior_list = []
		node = self.get_conflict_behavior_tree_node()
		while True:
			#break if node.children.empty?
			if node.children() != []: 
				node = node.box.get_by_selector()
				behavior_list.append(node.get_name())
			else:
				break

		return behavior_list

	def get_effort_behavior(self):
		behavior_list = []
		node = self.get_effort_behavior_tree_node()
		while True:
			#break if node.children.empty?
			if node.children() != []: 
				node = node.box.get_by_selector()
				behavior_list.append(node.get_name())
			else:
				break

		return behavior_list
