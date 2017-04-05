# -*- coding: utf-8 -*-

# package com.xiao.gameai.gameai.activities
 
# import android.support.v7.app.AppCompatActivity
# import android.os.Bundle
# import android.os.Handler
# import com.xiao.gameai.gameai.R
# import com.xiao.gameai.gameai.model.Fox
# import kotlinx.android.synthetic.main.activity_main.*
import time
import "/Users/RNakamura/Project/practice-gameAI-StateMachine/models/*" 

 
# class MainActivity : AppCompatActivity() 
class MainActivity(): 

	def __init__(self):
		self.myFox = Fox( 1, 10 )
		# handler = Handler()
 
    # override fun onCreate(savedInstanceState: Bundle?) {
    #     super.onCreate(savedInstanceState)
    #     setContentView(R.layout.activity_main)
 
    #     button_start.setOnClickListener {
    #         handler.postDelayed( runFox(), 1000 )
    #     }
    # }
 
    # fun runFox() : Runnable = object : Runnable {
    #     override fun run(){
    #         myFox.update()
    #         fox_message.text = myFox.getMessage()
    #         handler.postDelayed(this, 1000)
    #     }
    # }
	def runFox(): 
		myFox.update()
		# fox_message.text = myFox.getMessage()
		print(myFox.getMessage())
            

if __name__ == "__main__":
	a_game = MainActivity()
	while True:
		a_game.runFox()
		time.sleep(1)
