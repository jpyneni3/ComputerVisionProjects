import cv2
import numpy as np
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y: y+h, x:x+w]
        roi_color = img[y: y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        setX = x
        setY = y
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color, (ex+math.floor(.5*ex), ey+math.floor(.5*ey)), 4, (0,255,0), 2)

    mirror_img = cv2.flip( img, 1 )
    cv2.putText(mirror_img,"You ugly!!!", (setX,setY), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("mirror image", mirror_img)
    k = cv2.waitKey(3) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
