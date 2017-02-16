#!/bin/bash

HOME=/home/pi/raspberry-home-auto

cd $HOME
source $HOME/client/venv/bin/activate
python -m client.run.camera_run
deactivate
cd
