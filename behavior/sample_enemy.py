#!/usr/bin/env python
# -*- coding: utf-8 -*-

import behavior_tree

# 要最適化


class SampleEnemy(object):

    def __init__(self):
        self.behavior_tree = behavior_tree.BehaviorTree()

    def enemy_conflict_act(self):
        action_list = self.behavior_tree.get_conflict_behavior()
        print("conflict", action_list)
        # return

    def enemy_effort_act(self):
        action_list = self.behavior_tree.get_effort_behavior()
        print("effort", action_list)


if __name__ == "__main__":
    enemy = SampleEnemy()
    for i in range(1, 10):
        enemy.enemy_conflict_act()
        enemy.enemy_effort_act()
