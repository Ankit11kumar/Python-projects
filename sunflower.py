import cv2
import numpy as np

## Read
img = cv2.imread(r'C:\Users\ANKIT\Downloads\C++\C++\file\sunflower.jpg')

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))

## mask o yellow (15,0,0) ~ (36, 255, 255)
mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))

## final mask and masked
mask = cv2.bitwise_or(mask1, mask2)
target = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow("hsv", hsv)
cv2.imshow("masky", mask2)
cv2.imshow("maskg", mask1)
cv2.imshow("final", target)
