import cv2
import numpy as np


cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # image line set up across the frame
    # cv2.line(frame, starting position, ending position, color, thickness)
    # We made blue line across the frame (\)
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 50 )

    # We put a green line on top of img(1) (/)
    img = cv2.line(img, (0,height), (width, 0), (0,255,0), 50 )

    # We are drawing a rectangle 
    # (Source image, postion, radius, color, thickness)
    img = cv2.rectangle(img, (100,100), (200, 200), (128, 128, 128), 5)

    # We are drawing a circle
    # (Source image, postion, radius, color, thickness)
    img = cv2.circle(img, (650,650), 60 , (0, 0, 255), 5)

    # Inserting a text: To do so, one must choose a font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # (Source image, text, bottom left of the text, font, scale of the font, color, thickness, )
    img = cv2.putText(img, 'Alex is the goat', (100, height - 100), font, 1, (0,0,0), 5, cv2.LINE_AA)




    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

