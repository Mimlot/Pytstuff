import cv2 as cv
laptop = cv.imread('opencv_pract/photo/laptop.jpg')
def resize_img(frame, scale=0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resize = resize_img(laptop)
cv.imshow('lap', resize)
cv.waitKey(0)