import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)
    for (face_x, face_y, face_w, face_h) in faces:
        cv2.rectangle(img, (face_x, face_y), (face_x + face_w, face_y + face_h), (255, 0, 0), 2)
        roi_gray = gray_img[face_y: face_y + face_h, face_x: face_x + face_w]
        roi_original = img[face_y: face_y + face_h, face_x: face_x + face_w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)
        for (eye_x, eye_y, eye_width, eye_height) in eyes:
            cv2.rectangle(roi_original, (eye_x, eye_y), (eye_x + eye_width, eye_y + eye_height), (0, 255, 0), 2)

    cv2.imshow("output", img)

    if cv2.waitKey(1) == ord('q'):
        break