# -*- coding: utf-8 -*-


import os
import asyncio
import logging
import time
import uuid
from client.model.Camera import Camera


async def main():
    camera = Camera()
    while True:
        if not camera.running:
            logging.warning('-' * 10)
            logging.warning("Picamera taking a picture...")
            await capture_image(camera)
            logging.warning("Picamera goes to sleep for 1 second...")
            await asyncio.sleep(1)
            await remove_old_images()


async def capture_image(camera):
    image = camera.capture()
    ts = str(int(time.time()))
    hash = str(uuid.uuid4())
    # This makes, every image unique!
    path = os.path.dirname(os.path.abspath(__file__))
    image.save(path + '/../image/image.%s.%s.jpg' % (ts, hash))


async def remove_old_images():
    path = os.path.dirname(os.path.abspath(__file__)) + '/../image/'
    now = time.time()
    # cutoff = now - (5 * 86400)
    cutoff = now - 60
    for arquivo in os.listdir(path):
        filepath = str(path) + arquivo
        if os.path.isfile(filepath) and '.jpg' in arquivo:
            t = os.stat(filepath)
            c = t.st_ctime
            if c < cutoff:
                os.remove(filepath)


# Run using: python -m client.run.camera_run
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(main())
    loop.close()
