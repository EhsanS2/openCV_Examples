import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while 1:
    _, frame = cap.read()
    # convert color format to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define  range of colors to detect
    lower_red = np.array([0, 50, 20])
    upper_red = np.array([255, 100, 255])

    # define a mask
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # invert the mask
    mask_inv = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    if cv2.waitKey(5) & 0xFF == 27:
        break



cv2.destroyAllWindows()
cap.release()