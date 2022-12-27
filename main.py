# Created by Ahmadreza Anaami
import cv2
import numpy as np

def nothing(x):
    pass


img = cv2.imread("RES/2.jpg" , 0)
cv2.namedWindow('main-window')
cv2.createTrackbar('lower' , 'main-window' , 0 , 1000 , nothing)
cv2.createTrackbar('upper' , 'main-window' , 0 , 1000 , nothing)



while (1):

    cv2.waitKey(1)

    upperValue = cv2.getTrackbarPos("upper","main-window")
    lowerValue = cv2.getTrackbarPos("lower","main-window")
    
    
    imgCanny = cv2.Canny(img , lowerValue , upperValue)


    cv2.imshow("main-window" , imgCanny)

# Created by Ahmadreza Anaami