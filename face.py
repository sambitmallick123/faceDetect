import cv2

##Face Detect :
face_cascade = cv2.CascadeClassifier('/Users/sambitmallick/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

##Eye Detect :
#face_cascade = cv2.CascadeClassifier('/Users/sambitmallick/Downloads/opencv-master/data/haarcascades/haarcascade_eye.xml')


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('image window', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()