# -*- coding: utf-8 -*-


from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image


class Camera():

    def __init__(self):
        """Construtor."""
        self.picamera = PiCamera()

    def capture(self):
        stream = BytesIO()
        self.picamera.start_preview()
        sleep(2)
        self.picamera.capture(stream, format='jpeg')
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        return Image.open(stream)
