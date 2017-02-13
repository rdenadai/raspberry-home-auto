### About

This is the client app, used this in your Raspberry Pi with the picamera module.
In case you want, the client supports others hardware via client api code. There is a skematic to use some of them, fell free to implement your own (The code is based on the Adafruits example repository).

P.S.: Python 3 support only...

### Installation

- Enable Raspberry Pi I2C and other modules.

- Download the repository:
> git clone https://github.com/rdenadai/raspberry-home-auto.git

- Please create a virtualenv first:
> $ virtualenv venv
> $ pip install requirements.txt

- Also, don't forget do install the python3-smbus module:
> $ sudo apt install python3-smbus

- Register using supervisor, or in cron:
> $ python app.py
