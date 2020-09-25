import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip camera vertically
    frame = cv2.flip(frame, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('gray', gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()
