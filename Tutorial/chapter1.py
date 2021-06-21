import cv2

############################ Display Webcam #############################

cap = cv2.VideoCapture(0) # LOADING CAM
cap.set(4, 640)           # ID 4 ----------------------------> SET HEIGHT
cap.set(3, 480)           # ID 3 -----------------------------> SET WIDTH
cap.set(10, 100)          # ID 10 -----------------------> SET BRIGHTNESS

while True:
    success, img = cap.read() # READ WEBCAM FOOTAGE FRAMES 
                              # succes ----------------------------> BOOL
                              # img ------------------------------> FRAME
    cv2.imshow("window", img) # SHOW FRAMES, "window" ----> output_window
                              # img --------------------> prev_read_frame
    if cv2.waitKey(1) & 0xFF == ord("q"): #---> BREAK OUT (to be learned)
        break

############################ Display Images #############################

image = cv2.imread("F:\Haythem\codes\opencv\Tutorial\Resources\lena.JPG")
                              # LOADING IMAGE   |   FULL OR RELATIVE PATH 
cv2.imshow("window", image)   # SHOW IMAGE, "window" -----> output_window
                              # image ------------------> prev_read_image
cv2.waitKey(0)                # 0 -> INF | DELAY: TYPE -> INT, UNIT -> ms

############################ Display Video ##############################

vid = cv2.VideoCapture("Tutorial\Resources\Test_vid.mp4") 
                          # LOADING VIDEO     |     FULL OR RELATIVE PATH
vid.set(3, 640)           # ID 3 ----------------------------> SET HEIGHT
vid.set(4, 480)           # ID 4 -----------------------------> SET WIDTH
vid.set(10, 100)          # ID 10 -----------------------> SET BRIGHTNESS

while True:
    success, frame = vid.read() # READ VIDEO FRAMES 
                                # succes --------------------------> BOOL
                                # frame---------------------------> FRAME
    cv2.imshow("window", frame) # SHOW FRAMES, "window" --> output_window
                                # frame ----------------> prev_read_frame
    if cv2.waitKey(1) & 0xFF == ord("q"): #---> BREAK OUT (to be learned)
        break