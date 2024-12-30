import cv2 as cv
import numpy as np
import os

harr_cascade = cv.CascadeClassifier('opencv_pract/harr.xml')
p = []
for i in os.listdir(r'opencv_pract\train'):
    p.append(i)
#features = np.load('fetures.npy')
#lables = np.load('name_lables.npy')
face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('opencv_pract/face_trained.yml')
img = cv.imread(r'C:\Users\admin\Desktop\New folder\PyStuff\opencv_pract\val\ben_afflek\2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('face_ben',gray)

face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in face_rect:
    faces_region = gray[y:y+h, x:x+w]
    lables, confidence = face_recognizer.predict(faces_region)
    print(f"lables: {p[lables]:} with confidence: {confidence}")
    cv.putText(img, str(p[lables]), (20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected face', img)
cv.waitKey(0)