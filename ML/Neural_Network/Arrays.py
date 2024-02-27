import skimage.data
import numpy as np
import sys

img = skimage.data.chelsea()

img = skimage.color.rgb2gray(img)

filter = np.zeros((2, 3, 3)) #Two filters with 3x3 dimmensions

filter[0, :, :] = [[1, 1, 1],
                   [0, 0, 0], 
                   [-1, -1, -1]]

filter[1, :, :] = [[1, 0, -1],
                   [1, 0, -1], 
                   [1, 0, -1]]



def convolution(img, filter):
    if len(img.shape) > 2 or len(filter.shape) > 3:
        print("Erro")
        sys.exit()
    if filter.shape[1] != filter.shape[2]:
        print("Erro")
        sys.exit()
    if filter.shape[1]%2 == 0:
        print("Erro")
        sys.exit()