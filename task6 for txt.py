import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import re

# search point from file
def point_search(target_str, key_str):
    num = 0
    point_store = []
    start_index = [m.start() for m in re.finditer(key_str, target_str)]
    for i in range(len(start_index)):
        index_store = []
        for j in range(start_index[i], len(target_str)):
            if target_str[j] == ' ':
                index_store.append(j)
                num += 1
                if num >= 5:
                    num = 0
                    break
        for m in range(len(index_store) - 1):
            diff = index_store[m + 1] - index_store[m] - 1
            # for n in range(diff):
            #     point += int(target_str[index_store[m] + n + 1])
            if diff == 2:
                point = target_str[index_store[m]+1] + target_str[index_store[m]+2]
            elif diff == 3:
                point = target_str[index_store[m]+1] + target_str[index_store[m]+2] + target_str[index_store[m]+3]
            elif diff == 4:
                point = target_str[index_store[m]+1] + target_str[index_store[m]+2] + target_str[index_store[m]+3] + target_str[index_store[m]+4]
            else:
                point = -1
            point_store.append(int(point))

    return point_store

# read information from file
Point1 = []
Point2 = []
str1 = 'Pedestrian'
str2 = 'Cyclist'
with open('C:/Users/HASEE/Desktop/Pycharm_Project/data/annotations/frankfurt_000000_000294_leftImg8bit.png.txt') as file:
    data1 = file.read()
with open('C:/Users/HASEE/Desktop/Pycharm_Project/data/annotations/frankfurt_000000_000576_leftImg8bit.png.txt') as file:
    data2 = file.read()
Point1 = point_search(data1, str1)
Point2 = point_search(data2, str2)

# display the picture
img1 = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/data/images/frankfurt_000000_000294_leftImg8bit.png', 1)
img2 = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/data/images/frankfurt_000000_000576_leftImg8bit.png', 1)
cv.rectangle(img1, (Point1[0], Point1[1]), (Point1[0]+Point1[2], Point1[1]+Point1[3]), (255, 0, 0), 2)
cv.rectangle(img1, (Point1[4], Point1[5]), (Point1[4]+Point1[6], Point1[5]+Point1[7]), (255, 0, 0), 2)
cv.rectangle(img1, (Point1[8], Point1[9]), (Point1[8]+Point1[10], Point1[9]+Point1[11]), (255, 0, 0), 2)
cv.rectangle(img1, (Point1[12], Point1[13]), (Point1[12]+Point1[14], Point1[13]+Point1[15]), (255, 0, 0), 2)
cv.rectangle(img2, (Point2[0], Point2[1]), (Point2[0]+Point2[2], Point2[1]+Point2[3]), (255, 0, 0), 2)
cv.rectangle(img2, (Point2[4], Point2[5]), (Point2[4]+Point2[6], Point2[5]+Point2[7]), (255, 0, 0), 2)
cv.imshow("image1", img1)
cv.imshow("image2", img2)
cv.imwrite('C:/Users/HASEE/Desktop/Pycharm_Project/images/img1.png', img1)
cv.imwrite('C:/Users/HASEE/Desktop/Pycharm_Project/images/img2.png', img2)
cv.waitKey(0)
