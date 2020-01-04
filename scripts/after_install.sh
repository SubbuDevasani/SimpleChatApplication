#!/bin/bash

cd /home/ubuntu/chatproject/ChatApp/
sudo virtualenv venv
source venv/bin/activate
cd SimpleChatApplication
pip3 install -r requirments.txt
cd ..

