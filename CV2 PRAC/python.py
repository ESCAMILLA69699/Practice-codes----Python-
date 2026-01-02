import cv2
import numpy as np

# cap is short for capture
# 0 is the webcam you are using, 
# For instance if you have mulitple cameras is useful
cap = cv2.VideoCapture(1)



# Going to use a while loop
# Going to stop displaying when I press on a key

# Frame is the image itself turned into an array
# Ret is going to tell you if the capture worked properly

while True:
    ret, frame = cap.read()
    

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)


## THIS CODE IS TO BASICALLY DISPLAY THE CAMERA 


