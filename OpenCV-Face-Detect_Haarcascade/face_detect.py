import cv2 as cv

img = cv.imread('lady.jpg')
cv.imshow("Lady",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(face_rect)}')

for(x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected faces',img)


cv.waitKey(0)

#haarcascade file are taken from opencv github rep --> data
#haarcascade is sensitive to noise so it can detect any unwanted part of the img as face. To debug this you can increase the number of minNeighbors