import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import json

def point_search(str, image_id, ignore_flag):
    point = []
    for i in range(len(str)):
        if str[i].get('image_id') == image_id and str[i].get('ignore') == ignore_flag:
            for j in range(4):
                point.append(str[i]['bbox'][j])

    return point

Pedestrian_Point = []
Cyclist_Point = []
f = open('C:/Users/HASEE/Desktop/Pycharm_Project/data/val_gt.json')
t = json.load(f)
a = t['annotations']
Pedestrian_Point = point_search(a, 1, 0)
Cyclist_Point = point_search(a, 2, 1)

img1 = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/data/images/frankfurt_000000_000294_leftImg8bit.png', 1)
img2 = cv.imread('C:/Users/HASEE/Desktop/Pycharm_Project/data/images/frankfurt_000000_000576_leftImg8bit.png', 1)
cv.rectangle(img1, (Pedestrian_Point[0], Pedestrian_Point[1]), (Pedestrian_Point[0]+Pedestrian_Point[2], Pedestrian_Point[1]+Pedestrian_Point[3]), (0, 0, 255), 2)
cv.rectangle(img1, (Pedestrian_Point[4], Pedestrian_Point[5]), (Pedestrian_Point[4]+Pedestrian_Point[6], Pedestrian_Point[5]+Pedestrian_Point[7]), (0, 0, 255), 2)
cv.rectangle(img1, (Pedestrian_Point[8], Pedestrian_Point[9]), (Pedestrian_Point[8]+Pedestrian_Point[10], Pedestrian_Point[9]+Pedestrian_Point[11]), (0, 0, 255), 2)
cv.rectangle(img1, (Pedestrian_Point[12], Pedestrian_Point[13]), (Pedestrian_Point[12]+Pedestrian_Point[14], Pedestrian_Point[13]+Pedestrian_Point[15]), (0, 0, 255), 2)
cv.rectangle(img2, (Cyclist_Point[0], Cyclist_Point[1]), (Cyclist_Point[0]+Cyclist_Point[2], Cyclist_Point[1]+Cyclist_Point[3]), (0, 0, 255), 2)
cv.rectangle(img2, (Cyclist_Point[4], Cyclist_Point[5]), (Cyclist_Point[4]+Cyclist_Point[6], Cyclist_Point[5]+Cyclist_Point[7]), (0, 0, 255), 2)
cv.rectangle(img2, (Cyclist_Point[8], Cyclist_Point[9]), (Cyclist_Point[8]+Cyclist_Point[10], Cyclist_Point[9]+Cyclist_Point[11]), (0, 0, 255), 2)
cv.imshow("image1", img1)
cv.imshow("image2", img2)
cv.imwrite('C:/Users/HASEE/Desktop/Pycharm_Project/images/img1.png', img1)
cv.imwrite('C:/Users/HASEE/Desktop/Pycharm_Project/images/img2.png', img2)
cv.waitKey(0)
