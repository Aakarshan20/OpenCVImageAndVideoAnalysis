import cv2
import numpy as np

cap = cv2.VideoCapture(0)

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter('out1.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, size,1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == True:
        #frame = cv2.flip(frame,0)
        
        out.write(frame)
    
        #cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
