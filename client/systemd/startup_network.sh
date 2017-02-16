#!/bin/bash

HOME=/home/pi/raspberry-home-auto

cd $HOME
source $HOME/client/venv/bin/activate
python -m client.run.network_run
deactivate
cd
