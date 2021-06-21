import cv2
import numpy as np

img = cv2.imread("Tutorial\Resources\lenaresized.JPG")

###################### STACK IMAGES WITH NUMPY ######################

#-----------------------------> LIMITS <----------------------------# 
  # 1- UNABLE TO RESIZE STACKED IMAGES
  # 2- DOES NOT WORK WITH IMAGES OF DIFFERENT COLOR CHANNELS (LEVELS)

#---------------------------> SOLUTIONS <---------------------------#
# BY -> MURTAZA'S WORKSHOP | OPENCV BEGINNER'S COURSE | IN LINK BELOW
# https://www.computervision.zone/courses/learn-opencv-in-3-hours/lesson/chapter-6-joining-images/
# LINK TO VIDEO --> https://www.youtube.com/watch?v=WQeoO7MI0Bs | TIMESTAMP --> 53:00
# CHECH THIS FILE:  Tutorial\chapter6-StackImagesFunction.py

##### np.hstack ##### STACK IMAGES HORIZONTALLY ##### np.hstack #####
horizontally_stacked_image = np.hstack((img, img))
                             #      (img, img) = tup --> (img1, img2)
                             #      X AXIS

cv2.imshow("Horizontally Stacked Images", horizontally_stacked_image)
cv2.waitKey(0)

##### np.vstack ###### STACK IMAGES VERTICALLY ###### np.vstack #####
vertically_stacked_image = np.vstack((img, img))
                             #      (img, img) = tup --> (img1, img2)
                             #      Y AXIS

cv2.imshow("Vertically Stacked Images", vertically_stacked_image)
cv2.waitKey(0)