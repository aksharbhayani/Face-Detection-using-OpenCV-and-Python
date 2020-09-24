# first let's import OpenCV
import cv2

# Loading Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

img = cv2.imread('test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     #converting into gray scale
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
smile = smile_cascade.detectMultiScale(gray, 1.6, 26)

for(x, y, w, h) in faces:
    center = (x + w//2, y + h//2)
    radius = w//2
    cv2.circle(img, center, radius, (255, 255, 255), 1)
        
        
        
for(sx, sy, sw, sh) in smile:
    cv2.rectangle(img, (sx, sy), (sx + sw, sy + sh), (0, 255, 255), 2)
    
# give the name of the window
cv2.imshow('Face and Smile Detection ', img)
cv2.waitKey()
