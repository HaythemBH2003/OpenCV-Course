import cv2

### COLOR CONVENTION ------------------------> BGR ###

img = cv2.imread("F:\Haythem\codes\opencv\Tutorial\Resources\lena.JPG")

### cvtColor ### CONVERT IMAGE TO B&W ### cvtColor ###
img_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray image", img_gray_scale)
cv2.waitKey(0)


### cvtColor ### CONVERT IMAGE TO HSV ### cvtColor ###
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV image", img_HSV)
cv2.waitKey(0)

### GaussianBlur #### BLUR IMAGE #### GaussianBlur ###
img_blur = cv2.GaussianBlur(img, (7, 7), 0)
                    # img ---------------> img_to_blur
                    # (7, 7) == (X, X) --> BLUR DEGREE
                    # 0 ---------------------> SYGMA_X

cv2.imshow("blurred image", img_blur)
cv2.waitKey(0)

######### Canny #### CANNY  IMAGE #### Canny #########
img_blur = cv2.Canny(img, 100, 100)
                    # img --------------> img_to_canny
                    # 100, 100 --> ksize = Kernel Size

cv2.imshow("blurred image", img_blur)
cv2.waitKey(0)
