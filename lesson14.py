import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# ---------------------------------------------------------------------
# ------------- this code find an image in another image --------------
# -------- this code is basic, sometimes it doesn't work well ---------
# ---------------------------------------------------------------------

# read images
desk = cv.imread('desk.jpg', 0)
dog = cv.imread('dog.jpg', 0)

# select algorithm
orb = cv.ORB_create()

# apply algorithm on both images
kp1, desc1 = orb.detectAndCompute(desk, None)
kp2, desc2 = orb.detectAndCompute(dog, None)

# compare images
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)

# stores result of comparison
matches = bf.match(desc1, desc2)
matches = sorted(matches, key=lambda x: x.distance)

# draw lines between matched points
imgOut = cv.drawMatches(desk, kp1, dog, kp2, matches[:10], None, flags=2)

plt.imshow(imgOut)
plt.show()

