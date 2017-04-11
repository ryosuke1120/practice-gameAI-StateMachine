#!/usr/bin/env python
# -*- coding: utf-8 -*-

import behavior_tree

class SampleEnemy(object):

	def __init__(self):
		self.behavior_tree = behavior_tree.BehaviorTree()

	def enemy_conflict_act(self):
		action_list = self.behavior_tree.get_conflict_behavior()
		return action_list

	def enemy_effort_act(self):
		action_list = self.behavior_tree.get_effort_behavior()
		return action_list
		
if __name__ == "__main__":
	enemy = SampleEnemy()
	print("conflict action", enemy.enemy_conflict_act())
	print("effort action", enemy.enemy_effort_act())
