#!/bin/bash
echo "----------apt-get update----------"
sudo apt-get update
echo "----------apt-get upgrade----------"
sudo apt-get upgrade
echo "----------Installing git----------"
sudo apt-get install -y git
echo "----------Installing python----------"
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp34-cp34m-linux_x86_64.whl
sudo pip3 install numpy

#echo "----------Clone Repository----------"
#sudo git clone https://github.com/ryosuke1120/proto-dev-gameAI-byNN.git
#export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/agent:$PYTHONPATH"
#export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/behavior:$PYTHONPATH"
#export PYTHONPATH="/home/vagrant/proto-dev-gameAI-byNN/models:$PYTHONPATH"
