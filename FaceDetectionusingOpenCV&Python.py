# first let's import OpenCV
import cv2

# Loading Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray, frame):
    #converting into gray scale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        radius = w//2
        
        #drawing cicle over the face
        cv2.circle(frame, center, radius, (255, 255, 255), 1)            
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for(ex, ey, ew, eh) in eyes:     
                               
            #drawing circle over the eyes
            cv2.circle(roi_color, (ex + ew//2, ey + eh//2), (ew//2), (255, 255, 255), 1)
        
    return frame

# detecting face with live video camera 
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)

    # give the name of the window
    cv2.imshow('Face Detection using OpenCV and Python', canvas)
    
    # press Esc to close the window
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video_capture.release()         
cv2.destroyAllWindows()         