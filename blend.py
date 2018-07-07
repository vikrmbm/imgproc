import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread('moon.jpg')
img2 = cv2.imread('sea.jpg')

dst = cv2.addWeighted(img1,0.2,img2,0.8,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()