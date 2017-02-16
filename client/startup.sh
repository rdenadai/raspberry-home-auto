#!/bin/bash

HOME=/home/pi/raspberry-home-auto

cd $HOME
source venv/bin/activate
python -m client.run.network_run
python -m client.run.camera_run
deactivate
cd
