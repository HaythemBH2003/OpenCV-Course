import cv2
import numpy as np
from chapter6StackImagesFunction import stackImages

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 2000:
            cv2.drawContours(drawings_img, contour, -1, (0, 0, 255), 3)
            
            perimeter = cv2.arcLength(contour, True)
            detected_corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            number_of_corners = len(detected_corners)
            
            x, y, width, height = cv2.boundingRect(detected_corners)
            cv2.rectangle(drawings_img, (x, y), (x + width, y + height), (255, 0, 255), 3)

            if number_of_corners == 3:
                shape = "triangle"
            elif number_of_corners == 4:
                if 0.95 < width / height < 1.05:
                    shape = "square"
                else :
                    shape = "rectangle"
            elif number_of_corners == 8:
                shape = "circle"
            cv2.putText(drawings_img, shape, (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)

img = cv2.imread("Resources\shapes.jpg")
drawings_img = img.copy()
blank_img = np.zeros_like(img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (7, 7), 1)
canny_img = cv2.Canny(blur_img, 200, 200)
get_contours(canny_img)
stack = stackImages(0.6, ([img, gray_img, blur_img], [canny_img, drawings_img, blank_img]))

cv2.imshow("stack", stack)
cv2.waitKey(0)