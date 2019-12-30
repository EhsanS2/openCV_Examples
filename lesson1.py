import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pix.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('Canavas', img)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([400, 500], [500, 272], 'r', linewidth=2)
plt.show()

cv2.imwrite('pixout.jpg', img)