# -*- coding: utf-8 -*-

import time
from models.Fox import Fox

 
# class MainActivity : AppCompatActivity() 
class MainActivity(object): 

	def __init__(self):
		self.myFox = Fox(1, 10)
		# handler = Handler()
 
	def runFox(self): 
		self.myFox.update()
		# fox_message.text = myFox.getMessage()
		print(self.myFox.getMessage())
            

if __name__ == "__main__":
	a_game = MainActivity()
	while True:
		a_game.runFox()
		time.sleep(1)
