# Prototype development of game AI using neural network

## Demo (current development situation)
![demo](https://github.com/ryosuke1120/proto-dev-gameAI-byNN/blob/master/DEMO-proto-dev-gameAI-byNN.gif)

## How to run  
`$ python3 main_activity.py`

If your environment does not work, please use the Vagrant file as below.  
`$ vagrant box add trusty64 https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box`  
`$ vagrant up`  
`$ vagrant ssh`  
`$ export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/agent:$PYTHONPATH"`  
`$ export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/behavior:$PYTHONPATH"`  
`$ export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/models:$PYTHONPATH"`  

## Effect
I am a beginner developer of game AI,  
because I started development in April 2017.  
In this repository, development is proceeding with personal interest.  

I am developing game AI using Python,  
but I am planning to rewrite it simply in a programming language (eg C ++) that has affinity with the game.  

There are few samples of the game AI program.  
Therefore, if you have an expert, I would like to ask for your help at any time. :)  

As an initial goal,  
I'm trying to realize a simple simulation game using "FSM : FiniteStateMachine", "BehaviorTree", "RL :ReinforcementLearning" on the console.  

Currently, each sample program has already been developed.  
So we will show how to run the sample.  

## How to run sample programs

* **FiniteStateMachine**  
`$ cd sample/FSM`  
`$ pwd`  
`=>(your directory path)/proto-dev-gameAI-byNN/sample/FSM`    
Create the following paths by copy&paste, and through the Python path.  
`$ export PYTHONPATH="(your directory path)/proto-dev-gameAI-byNN/sample/FSM:$PYTHONPATH"`  
`$ python3 main_activity.py`    
When you execute it, sample FSM will start.  
Please use [ctr + c] if you want to stop.  

* **BehaviorTree**  
`$ cd sample/BehaviorTree`  
`$ python3 sample_enemy.py`    
Every time it is executed,  
Action can be taken out from the behavior tree.  

* **ReinforcementLearning**  
`$ cd sample/ReinforcementLearning`  
`$ python3 sample_rl.py`  

## MyTask
* Global state transition bug (behavior tree)  
* Reinforcement learning, how to incorporate neural network  
