import cv2 as cv
import numpy as np

# ------------------------------------------------
# --- this example detect all corners in image ---
# ------------------------------------------------

# read image
img = cv.imread('rect.jpg')

# convert to gray
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgGray = np.float32(imgGray)

# detect corners
res = cv.goodFeaturesToTrack(imgGray, 200, 0.01, 10)
corners = np.int0(res)

for corner in corners:
    # draw a circle around corners
    x, y = np.ravel(corner)
    cv.circle(img, (x, y), 5, (0, 0, 255), 1)

cv.imshow('Result', img)
cv.waitKey(0)