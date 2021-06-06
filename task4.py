import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/images/landscape_2.jpeg', 1)
img_B = img.copy()
img_G = img.copy()
img_R = img.copy()

# set channel of R to 0
img_R[81:110, 108:147, 0] = 0
ax1 = plt.subplot(221)
ax1.set_title('R')
plt.axis('off')
plt.imshow(img_R)

# set channel of G to 0
img_G[81:110, 108:147, 1] = 0
ax2 = plt.subplot(222)
ax2.set_title('G')
plt.axis('off')
plt.imshow(img_G)

# set channel of B to 0
img_B[81:110, 108:147, 2] = 0
ax3 = plt.subplot(223)
ax3.set_title('B')
plt.axis('off')
plt.imshow(img_B)

# display the raw image
ax4 = plt.subplot(224)
ax4.set_title('raw image')
plt.axis('off')
plt.imshow(img)
plt.show()
