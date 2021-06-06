import numpy as np
import cv2 as cv

img = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/images/landscape_2.jpeg', 1)
scale = 1.08
height, width = img.shape[:2]
# shrink the picture
img2 = cv.resize(img, (int(width / scale), int(height / scale)), cv.INTER_AREA)
img3 = cv.resize(img, (int(width / scale**2), int(height / scale**2)), cv.INTER_AREA)
img4 = cv.resize(img, (int(width / scale**3), int(height / scale**3)), cv.INTER_AREA)
img5 = cv.resize(img, (int(width / scale**4), int(height / scale**4)), cv.INTER_AREA)
img6 = cv.resize(img, (int(width / scale**5), int(height / scale**5)), cv.INTER_AREA)
print('size of image:', img6.shape)
# combine all the pictures
width_block = img.shape[1]+img2.shape[1]+img3.shape[1]+img4.shape[1]+img5.shape[1]+img6.shape[1]
height_block = img.shape[0]
img_block = np.zeros((height_block, width_block, 3), np.uint8)
img_block[0:192, 0:256] = img
img_block[0:177, 256:493] = img2
img_block[0:164, 493:712] = img3
img_block[0:152, 712:915] = img4
img_block[0:141, 915:1103] = img5
img_block[0:130, 1103:1277] = img6
# display and save the picture
cv.imshow('image_black', img_block)
cv.imwrite('C:/Users/HASEE/Desktop/Pycharm_Project/images/landscape_3.jpeg', img_block)
cv.waitKey(0)
