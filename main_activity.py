#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from models.fox import *

class MainActivity(object): 

	def __init__(self):
		self.my_fox = Fox(1, 10)
 
	def run_fox(self): 
		self.my_fox.update()
		# fox_message.text = myFox.getMessage()
		print(self.my_fox.getMessage())

if __name__ == "__main__":
	a_game = MainActivity()
	while True:
		a_game.run_fox()
		time.sleep(1)
