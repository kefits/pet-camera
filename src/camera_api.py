import numpy as np
import glob
import pyper
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware


# Config
public_dir = "../public/temporary_images/"
image_dir = "../../temporary_images/"

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


class Key(BaseModel):
    key: str


@app.post("/pet_camera")
async def upload_data(key: Key):
    # Obtain new image file
    image_files = np.array(glob.glob(public_dir + "*"))
    image_num = np.array([int(file.split("_")[-1].split(".")[0]) for file in image_files])
    # new_image_file = image_files[image_num == np.max(image_num)][0][3:]
    new_image_file = image_files[image_num == np.max(image_num)][0]
    # print(image_dir + new_image_file.split("/")[-1])
    return {"Image": image_dir + new_image_file.split("/")[-1]}
