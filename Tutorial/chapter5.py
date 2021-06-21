import cv2
import numpy as np

img = cv2.imread("Tutorial\Resources\lenaresized.JPG") 

#################  FLATTEN OBJECTS IN IMAGE  ####################

'''                         STEP 1                            '''
#  1- DETERMINE CORNERS (= pts1) COORDINATES IN IMAGE WITH PAINT. 
#  2- ORGANIZE THE COORDINATES IN AN ARRAY IN THE FOLLOWING FORM:
#       pts1 = np.float32( [  [TL_CORNER_COOR], [TR_CORNER_COOR],
#                         [BL_CORNER_COOR], [BR_CORNER_COOR]  ] )
pts1 = np.float32([[295, 93], [311, 87], [334, 283], [350, 277]])

'''                         STEP 2                            '''
# SET OUTPUT IMG SIZE AND REPRESENT EACH P1 WITH CORRESPONDING P2
# LIKE THE FOLLOWING : 
#  pts2 = np.float32( [[0, 0], [WIDTH, 0], [0, HEIGHT], [W, H]] )
pts2 = np.float32([[0, 0], [250, 0], [0, 800], [250, 800]])

'''                         STEP 3                            '''
# 1- SET MATRIX: matrix = cv2.getPerspectiveTransform(pts1, pts2)
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# 2- CERATE FLAT IMG:    cv2.warpPerspective(img, matrix, (W, H))
imgout = cv2.warpPerspective(img, matrix, (250, 800))

cv2.imshow("imaga", imgout)    
cv2.waitKey(0)