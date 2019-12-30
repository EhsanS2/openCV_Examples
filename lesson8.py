import cv2
import numpy as np

img1 = cv2.imread('pix.jpg')
img2 = cv2.imread('logo.jpg')

rows, cols, channels = img2.shape

# store a piece of main image same size with logo
roi = img1[5:rows+5, 5:cols+5]

# Convert image color to gray
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# creating a mask
ret, MASK = cv2.threshold(img2_gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(MASK)  # inverted mask

# apply mask on cut piece of main image
img_bg = cv2.bitwise_and(roi, roi, mask = MASK)
img_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)

# add to pic together
dst = cv2.add(img_bg, img_fg)

# put cut piece of main picture back to its place
img1[5:rows+5, 5:cols+5] = dst

# showing Output
cv2.imshow('Logo', img2)
cv2.imshow('Final', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
