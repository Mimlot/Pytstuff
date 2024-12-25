import cv2 as cv
img= cv.imread('opencv_pract/photo/Face.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
harr_cascade = cv.CascadeClassifier('opencv_pract/harr.xml')

face_rectang = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 3)
print(f"So khuon mat trong hinh: {len(face_rectang)}")
for (x,y,w,h) in face_rectang:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Face', img)