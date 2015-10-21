#!/bin/sh

sudo apt-get update
sudo apt-get install git -y
sudo apt-get install python-pip -y
sudo apt-get install rabbitmq-server
sudo apt-get install python-swiftclient


git clone https://github.com/saro6971/lab3.git
curl -O http://smog.uppmax .uu.se:8080/swift/v1/tweets/tweets_0.txt


