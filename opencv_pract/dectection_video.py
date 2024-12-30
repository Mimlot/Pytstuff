import cv2 as cv
video = cv.VideoCapture('opencv_pract/video/tyler1.mp4')
harr_cascade = cv.CascadeClassifier('opencv_pract/harr.xml')
def resize_img(frame, scale=1):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rectang = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in face_rectang:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    frame_resized = resize_img(frame, scale= .4)
    cv.imshow('video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()