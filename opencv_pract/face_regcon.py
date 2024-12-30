import os
import cv2 as cv
import numpy as np

p = []
for i in os.listdir(r'opencv_pract\train'):
    p.append(i)
DIR = r'C:\Users\admin\Desktop\New folder\PyStuff\opencv_pract\train'
fetures =[]
name_lables = []
harr_cascade = cv.CascadeClassifier('opencv_pract/harr.xml')
def create_tranning():
    for ppl in p:
        path = os.path.join(DIR, ppl)
        lables = p.index(ppl)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_arry = cv.imread(img_path)
            
            gray_img = cv.cvtColor(img_arry, cv.COLOR_BGR2GRAY)
            face_rect= harr_cascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors=4)
            
            
            for (x,y,w,h) in face_rect:
                faces_region = gray_img[y:y+h, x:x+w]
                fetures.append(faces_region)
                name_lables.append(lables)
create_tranning()
fetures = np.array(fetures, dtype='object')
name_lables = np.array(name_lables)

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.train(fetures,name_lables)
face_recognizer.save('opencv_pract/face_trained.yml')
np.save('opencv_pract/fetures.npy', fetures)
np.save('opencv_pract/name_lables', name_lables)