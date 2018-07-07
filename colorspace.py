import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread ( 'blue.jpg' )
img2 = cv2.imread ( 'sea.jpg' )

hsv = cv2.cvtColor ( img2, cv2.COLOR_BGR2HSV )

cv2.imshow ( 'dst', hsv )
cv2.waitKey ( 0 )
cv2.destroyAllWindows ()

hsv = cv2.cvtColor ( img1, cv2.COLOR_BGR2HSV )
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img1,img1, mask= mask)

cv2.imshow('frame',img1)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey ( 0 )
cv2.destroyAllWindows()

