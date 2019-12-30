import cv2
import numpy as np

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cv2.line(frame, (100, 200), (200, 350), (25, 250, 30), 10)
    # cv2.rectangle(frame, (100, 200), (200, 400), (50, 50, 255), 6)
    # cv2.circle(frame, (150, 250), 70, (255, 50, 50), 4)
    pts = np.array([[20, 40], [10, 120], [200, 240], [300, 370], [400, 80], [20, 40]])
    # cv2.polylines(frame, [pts], False, (220, 218, 60), 6)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, 'Ehsan', (5, 55), font, 2, (60, 21, 160), 2)
    cv2.putText(frame, 'Hatefi', (5, 120), font, 2, (60, 160, 40), 2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()