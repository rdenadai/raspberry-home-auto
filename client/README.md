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
>
> $ pip install requirements.txt

- Also, don't forget do install the python3-smbus module:
> $ sudo apt install python3-smbus

- Register the services to run, using supervisor (circus), or in cron:
> $ python -m client.run.network_run
>
> $ python -m client.run.camera_run

- There are shell scripts prepared to be run using systemd (please, look inside systemd folder):
> $ startup_camera.sh
>
> and others... for each service!

- Edit picamera file in case of error:
> If you get the following error: "TypeError: __class__ set to <class 'picamera.mmal.MMAL_FOURCC_T'> defining 'MMAL_FOURCC_T' as <class 'picamera.mmal.MMAL_FOURCC_T'>"
>
> Please follow guidelines here: https://github.com/waveform80/picamera/issues/355
