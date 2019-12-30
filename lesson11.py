import cv2
import numpy as np

# select a source
cap = cv2.VideoCapture(1)

while 1:
    # read from source
    _, frame = cap.read()

    # apply different algorithms to video
    lapacian = cv2.Laplacian(frame, cv2.CV_8U)
    sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=1)
    canny = cv2.Canny(frame, 100, 160)

    # show output
    cv2.imshow('Original', frame)
    cv2.imshow('Converted', lapacian)
    cv2.imshow('SobelX', sobelx)
    cv2.imshow('Canny', canny)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()