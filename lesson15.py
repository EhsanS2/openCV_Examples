import cv2 as cv
import numpy as np

# ---------------------------------------------------------------------
# ----------------- this example remove background --------------------
# --- this code detect fixed pixel and considers them as background ---
# ---------------------------------------------------------------------

# select video source
cap = cv.VideoCapture(1)

# define a mask
fg = cv.createBackgroundSubtractorMOG2()

while 1:
    # read video from source
    _, frame = cap.read()

    # apply mask on video
    fmask = fg.apply(frame)

    # show output
    cv.imshow('original', frame)
    cv.imshow('fg', fmask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release memory
cv.destroyAllWindows()
cap.release()