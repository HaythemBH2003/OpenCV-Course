import cv2
import numpy as np
from chapter6StackImagesFunction import stackImages

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

###################   COLOR DETECTION   ###################

def empty(a):     # FUNCTION CALLED AFTER A TRACKBAR CHANGE
    pass          # USELESS FUNCTION 

cv2.namedWindow("trackbars") 
                # cv2.namedWindow ----> INITIATE NEW WINDOW
                #         "trackbars" --------> WINDOW NAME
cv2.resizeWindow("trackbars", 640, 240)
                # cv2.resizeWindwow --------> RESIZE WINDOW
                #         "trackbars" ---> WINDOW TO RESIZE
                #           (WINDOW, NEW_WIDTH, NEW_HEIGHT)

##################### CREATE TRACKBAR #####################
#------------------>   GENERAL  FORM   <------------------#     
#   cv2.createTrackbar(TRACKBAR_NAME, WINDOW_NAME, MIN_VAL,
#                                       MAX_VAL, ON_CHANGE)

#-------------------->   EXAMPLES   <---------------------#
cv2.createTrackbar("Hue Min", "trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "trackbars", 23, 179, empty)
cv2.createTrackbar("Sat Min", "trackbars", 103, 255, empty)
cv2.createTrackbar("Sat Max", "trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "trackbars", 58, 255, empty)
cv2.createTrackbar("Val Max", "trackbars", 255, 255, empty)


while True:
    
    success, img = cap.read()
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    # CONVERT IMAGE TO HSV | CHECK CHAPTER2
    
  # getTrackbarPos # GET TRACKBAR VALUE # getTrackbarPos #
    #-----------------> GENERAL FORM <-----------------#
    # VALUE = cv2.getTrackbarPos(TRAC_NAME, TRAC_WINDOW)

    #-------------------> EXAMPLES <-------------------#
    Hue_Min = cv2.getTrackbarPos("Hue Min", "trackbars")
    Hue_Max = cv2.getTrackbarPos("Hue Max", "trackbars")
    Sat_Min = cv2.getTrackbarPos("Sat Min", "trackbars")
    Sat_Max = cv2.getTrackbarPos("Sat Max", "trackbars")
    Val_Min = cv2.getTrackbarPos("Val Min", "trackbars")
    Val_Max = cv2.getTrackbarPos("Val Max", "trackbars")
    
            # COMMENT LINE OUT TO CHECK VALUES #       
    '''print(Hue_Min, Hue_Max, Sat_Min, Sat_Max, Val_Min, Val_Max)'''
    
    ##### inRange ##### CREATE MASK ##### inRange ####
    # A MASK: Hide some portions of an image 
    #         and reveal other portions.
    # Hidden Parts: BLACK | Revealed Parts: WHITE
    lower = np.array([Hue_Min, Sat_Min, Val_Min])
    upper = np.array([Hue_Max, Sat_Max, Val_Max])
    
    mask = cv2.inRange(img_HSV, lower, upper)

    # bitwise_and # MASK REVEALED PARTS WITH COLOR # bitwise_and #
    img_result = cv2.bitwise_and(img, img, mask=mask)
    
    img_stack = stackImages(0.6, ([img, img_HSV], [mask, img_result]))
    cv2.imshow("stacked images", img_stack)

    cv2.waitKey(1)