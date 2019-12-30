import cv2 as cv
import numpy as np

# read main image
main = cv.imread('main.jpg')

# convert to gray
mainGray = cv.cvtColor(main, cv.COLOR_BGR2GRAY)

# read pattern
pattern = cv.imread('ptr.jpg', 0)

w, h = pattern.shape[::-1]

# match pattern with main image
res = cv.matchTemplate(mainGray, pattern, cv.TM_CCOEFF_NORMED)

# set accuracy
threshhold = 0.76

loc = np.where(res >= threshhold)

# draw a rectangle around detected pattern
for pt in zip(*loc[::-1]):
    cv.rectangle(main, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 1)


cv.imshow('PIC', main)
cv.waitKey(0)