import cv2
import numpy as np

img1 = cv2.imread('pic1.jpg')
img2 = cv2.imread('pic2.jpg')

# add = img1 + img2
# add = cv2.add(img1, img2)
# add = cv2.addWeighted(img1, 1, img2, 0.4, 0)

cv2.imshow('add', add)
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)

cv2.waitKey(0)
