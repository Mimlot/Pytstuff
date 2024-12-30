import cv2 as cv

# Load Haar cascade once (outside the loop)
harr_cascade = cv.CascadeClassifier('opencv_pract/harr.xml')

# Open the video
video = cv.VideoCapture('opencv_pract/video/tyler1.mp4')

def resize_img(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True: 
    isTrue, frame = video.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    face_rectang = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in face_rectang:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Resize frame for display
    frame_resized = resize_img(frame, scale=0.4)

    # Display the frame
    cv.imshow('Video - Face Detection', frame_resized)

    # Exit if 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release resources
video.release()
cv.destroyAllWindows()
