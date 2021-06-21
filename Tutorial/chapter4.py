import cv2
import numpy as np

######## INITIATE PIXELS ARRAY ########
img = np.zeros((512, 512, 3), np.uint8)
        # INIATING LVL 3 ARRAY 
        # (512, 512, 3) --> (H, W, LVL)
        # TO BE LEARNED (NO EXP SO FAR)
print(img.shape)

img[100: 200, 100: 200] = 255, 0, 0
    # [100: 200, 100: 200] ...........
    # [START_H: END_H, START_W, END_W]
print(img.shape)

########################      CREATE A LIGN      ######################## 
#------------------------->   GENERAL  FORM   <-------------------------#     
# cv2.line(img, (START_X, START_Y), (END_X, END_Y), COLOR_BGR, THICKNESS)


#--------------------------->    EXAMPLE    <---------------------------#  
cv2.line(img, (100, 100), (200, 200), (0, 255, 0), 2)

#########################   CREATE RECTANGLE   ##########################

#-------------------------->  GENERAL FORM  <---------------------------# 
#  cv2.rectangle(img, (START_X, START_Y), (END_X, END_Y), CLR, THICKNESS)

#-------------------------->     EXAMPLE    <---------------------------#
cv2.rectangle(img, (0, 0), (100, 100), (0, 0, 255), cv2.FILLED)
                                          # cv2.FILLED --> FILL RECTANGLE            

##########################   CREATE CIRCLE   ############################

#-------------------------->  GENERAL FORM  <---------------------------# 
#     cv2.circle(img, (CENTER_X, CENTER_Y), RADUIS, COLOR, THICKNESS)

#-------------------------->     EXAMPLE    <---------------------------#
cv2.circle(img, (256, 256), 30, (255, 137, 0), 2)

###########################   CREATE TEXT   #############################

#-------------------------->  GENERAL FORM  <---------------------------#
#  cv2.putText(img, TEXT, (x, Y), cv2.FONT_..., SIZE, COLOR, THICKNESS)

#-------------------------->     EXAMPLE    <---------------------------#
cv2.putText(img, "T", (256, 256), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)