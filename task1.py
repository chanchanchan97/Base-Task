import numpy as np
import cv2 as cv

img = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/images/landscape.jpeg', 0)
print(img.shape)
cv.imshow("image", img)
cv.waitKey(0)
