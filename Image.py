import cv
import numpy as np


class Image:

    def __init__(self, img):
        self.img = img

    def __grayScale(self):
        self.img = cv.imread(self.img, cv.IMREAD_GRAYSCALE)

    def __resize(self):
        self.img = cv.resize(self.img, (640, 427))

    def __fourier(self):
        # fft2 for 2d fourier transform as the variation of the image happend in two dimension
        fourier_ = np.fft.fft2((self.img))
        # to avoid the repeation in the frequencies
        fourier_shifted = np.fft.fftshift(fourier_)
        self.img = fourier_shifted

    def getfourier(self):
        Image.__grayScale(self)
        Image.__resize(self)
        Image.__fourier(self)
        return self.img

    @staticmethod
    def save(path, img):
        with open(path, 'wb') as f:
            cv.imwrite(path, img)


class ImageProcessing:
    def __init__(self, edges, value, uniform_Magnitude_bool, uniform_phase_bool, fourier_shifted):
        self.edges = edges
        self.value = value
        self.uniform_Magnitude_bool = uniform_Magnitude_bool
        self.uniform_phase_bool = uniform_phase_bool
        self.fourier_shifted = fourier_shifted

    def __handel_croper(self):
        if self.value == 1:
            arr_ = np.abs(self.fourier_shifted)  # the magnitude after fourier
            arr_ = self.__crop(arr_)
            if self.uniform_Magnitude_bool == "true":
                arr_ = np.ones(arr_.shape)

        elif self.value == 0:
            arr_ = np.angle(self.fourier_shifted)  # the phase after fourier
            arr_ = self.__crop(arr_)
            if self.uniform_phase_bool == 'true':
                arr_ = np.zeros(arr_.shape)
            arr_ = np.exp(1j*arr_)
        return arr_

    def __crop(self, arr):
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                # the i and j axis are obtined according to the cropped image
                if (i < self.edges[0][0] or i >= self.edges[0][1]) or (j <= self.edges[1][0] or j >= self.edges[1][1]):
                    arr[i][j] = self.value
        return arr

    def get_cropped(self):

        return self.__handel_croper()
