import skimage.data
import numpy as np

img = skimage.data.chelsea()

img = skimage.color.rgb2gray(img)

filter = np.zeros((2, 3, 3)) #Two filters with 3x3 dimmensions

filter[0, :, :] = [[1, 1, 1],
                   [0, 0, 0], 
                   [-1, -1, -1]]

filter[1, :, :] = [[1, 0, -1],
                   [1, 0, -1], 
                   [1, 0, -1]]
