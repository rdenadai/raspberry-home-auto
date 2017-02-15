# -*- coding: utf-8 -*-


import time
import asyncio
from model.Scanner import NetworkScanner
from model.Camera import Camera


async def main():
    camera = Camera()
    ns = NetworkScanner()
    while True:
        if not camera.running:
            await capture_image(camera)
            await asyncio.sleep(1)
        if not ns.running:
            await capture_network(ns)
            await asyncio.sleep(1)


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
