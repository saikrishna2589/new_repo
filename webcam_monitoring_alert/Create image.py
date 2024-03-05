import numpy

import cv2
import numpy as np

#feeding the array of image pixels to the array variable
#this would be 4 columns 3 rows so 12 pixels.
#each bucket 255,0,0 is one color
array = np.array([[[255, 0, 0],
                   [255, 255, 255],
                   [255, 255, 255],
                   [187, 41, 160]],

                  [[255, 255, 255],
                   [255, 255, 255],
                   [255, 255, 255],
                   [255, 255, 255]],

                  [[255, 255, 255],
                   [0, 0, 0],
                   [47, 255, 173],
                   [255, 255, 255]]])

cv2.imwrite('image1.png',array)