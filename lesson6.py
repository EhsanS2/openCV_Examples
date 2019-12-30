import cv2
import numpy as np


img = cv2.imread('pix.jpg', cv2.IMREAD_COLOR)

pixel = img[190:200, 190:200]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(pixel)