import cv2

############ COORDINATES CONVENTIONS ############
# (0, 0) --------------------------> (MAX_X, 0) #
#    |                                    |     #
#    |                                    |     #
#    |                                    |     #
#    |                                    |     #
#   \ /                                   |     #
# (0, MAX_Y) ------------------- (MAX_X, MAX_Y) #
############ COORDINATES CONVENTIONS ############

img = cv2.imread("Tutorial\Resources\lena.JPG")

################ GET IMAGE SHAPE ################

(height, width, level) = img.shape
      # .shape RETURN --> (IMG_H, IMG_W, IMG_LVL)

cv2.imshow("original image", img)
cv2.waitKey(0)

################  RESIZE IMAGE  #################

resized_img = cv2.resize(img, (300, 500))
       # cv2.resize(img, (NEW_HEIGHT, NEW_WIDTH))
cv2.imshow("resized image", resized_img)
cv2.waitKey(0)

#################  CROP IMAGE  ##################
''' image = Matrix of pixels -> Numpy to crop '''

import numpy as np

cropped_img = img[0: 200, 200: 500]
cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)