import numpy as np


class ImageCombination:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2

    def __multiply(img1, img2):
        return np.multiply(img1, img2)

    def combine(self):
        return np.real(np.fft.ifft2(np.fft.ifftshift(ImageCombination.__multiply(self.img1, self.img2))))
