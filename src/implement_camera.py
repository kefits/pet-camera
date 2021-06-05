import cv2
from PIL import Image
import os
import shutil
import time
import asyncio


# Config
image_dir = "../public/temporary_images/"
# image_dir = "../../temporary_images/"


# Empty directory
def empty_dir():
    shutil.rmtree(image_dir)
    os.mkdir(image_dir)

async def async_empty_dir():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, shutil.rmtree, image_dir)
    os.mkdir(image_dir)


# Implement camera
def implement_camera():
    camera = cv2.VideoCapture(0)

    empty_dir()

    i = 10000
    while True:
        ret, frame = camera.read()

        img = Image.fromarray(frame)
        img = img.resize((256, 256))
        img.save(image_dir + "img_" + str(i) + ".png")

        # cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        i += 1

        if (i % 100) == 0:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_empty_dir())
            # i = 1

        time.sleep(0.2)

    camera.release()


if __name__ == "__main__":
     implement_camera()
