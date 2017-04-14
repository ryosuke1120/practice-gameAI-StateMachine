#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from models.Fox import *

class MainActivity(object): 

	def __init__(self):
		self.myFox = Fox(1, 10)
 
	def run_fox(self): 
		self.myFox.update()
		# fox_message.text = myFox.getMessage()
		print(self.myFox.getMessage())

if __name__ == "__main__":
	a_game = MainActivity()
	while True:
		a_game.run_fox()
		time.sleep(1)
