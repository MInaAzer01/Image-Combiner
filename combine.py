import cv
import numpy as np
from random import randint
from Imagecombination import *
from Image import *


def saveImg(img, path):
    with open(path, 'wb') as f:
        f.write(img)


def get_combined(option, edges1, edges2, uniform_phase_bool, uniform_Magnitude_bool):
    img_1 = Image("static/images/input/original1.png")
    img_2 = Image("static/images/input/original2.png")
    ImageProcessing_1 = ImageProcessing(
        edges1, (option == "option1"), uniform_Magnitude_bool, uniform_phase_bool, img_1.getfourier()).get_cropped()
    ImageProcessing_2 = ImageProcessing(
        edges2, (option != "option1"), uniform_Magnitude_bool, uniform_phase_bool, img_2.getfourier()).get_cropped()
    img_combined = ImageCombination(ImageProcessing_1, ImageProcessing_2)

    path_img = f"static/images/output/{randint(1,100000)}.png"
    Image.save(path_img, img_combined.combine())
    return path_img
