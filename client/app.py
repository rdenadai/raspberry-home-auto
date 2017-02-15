# -*- coding: utf-8 -*-


import logging
import time
import asyncio
from model.Scanner import NetworkScanner
from model.Camera import Camera


async def main():
    camera = Camera()
    ns = NetworkScanner()
    while True:
        if not camera.running:
            logging.info('-' * 10)
            logging.info("Picamera taking a picture...")
            await capture_image(camera)
            logging.info("Picamera goes to sleep a little...")
            await asyncio.sleep(2)
        if not ns.running:
            logging.info('-' * 10)
            logging.info("Networking will be run...")
            await capture_network(ns)
            logging.info("Networking goes to sleep a little...")
            await asyncio.sleep(2)


async def capture_image(camera):
    image = camera.capture()
    ts = int(time.time())
    image.save(f'image/image.{ts}.jpg')


async def capture_network(ns):
    ns.scan()
    print(ns.data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(main())
    loop.close()
