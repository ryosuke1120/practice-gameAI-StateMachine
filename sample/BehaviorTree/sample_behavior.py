#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sample_box

class Behavior():
	def __init__(self, name):
		self.name = name
		self.box = sample_box.Box() 

	def add_behavior(self, bhv):
		self.box.add_list(bhv)

	def executable(self):
		return True

	def children(self):
		return self.box.get_list()

	def get_name(self):
		return self.name
