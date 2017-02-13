# -*- coding: utf-8 -*-


import asyncio
from model.Camera import Camera
from time import sleep


async def main():
    camera = Camera()
    while True:
        capture_image(camera)


async def capture_image(camera):
    image = camera.capture()
    image.save('img/image.jpg')
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(main())
    loop.close()
