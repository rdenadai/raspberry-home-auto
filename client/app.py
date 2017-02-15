# -*- coding: utf-8 -*-


import asyncio
from model.Scanner import NetworkScanner
from model.Camera import Camera


async def main():
    camera = Camera()
    ns = NetworkScanner()
    while True:
        await capture_image(camera)
        await capture_network(ns)
        await asyncio.sleep(1)


async def capture_image(camera):
    image = camera.capture()
    image.save('image/image.jpg')


async def capture_network(ns):
    ns.scan()
    print(ns.data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(main())
    loop.close()
