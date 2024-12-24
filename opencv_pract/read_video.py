import cv2 as cv
cap = cv.VideoCapture('opencv_pract/video/plane.mkv')
def resize_img(frame, scale=0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def live_video_change_res(width, height):
    # resize live video
    cap.set(3, width)
    cap.set(4, height)
while True:
    isTrue, frame = cap.read()
    frame_resized = resize_img(frame, scale= .2)
    cv.imshow('video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows()
