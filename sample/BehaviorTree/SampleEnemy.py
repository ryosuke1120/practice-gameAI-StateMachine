#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BehaviorTree

#要最適化
class SampleEnemy(object):

	def __init__(self):
		self.behavior_tree = BehaviorTree.BehaviorTree()

	def enemy_conflict_act(self):
		action_list = self.behavior_tree.get_conflict_behavior()
		# print("conflict", action_list)
		return action_list

	def enemy_effort_act(self):
		action_list = self.behavior_tree.get_effort_behavior()
		# print("effort", action_list)
		return action_list
		
if __name__ == "__main__":
	enemy = SampleEnemy()
	print("conflict action", enemy.enemy_conflict_act())
	print("effort action", enemy.enemy_effort_act())
