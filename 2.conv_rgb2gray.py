import cv2
import numpy as np

image = cv2.imread('lane.jpg')

array = np.copy(image)
# if we do array = image -- it will modify the original when array variable changes

convgray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)

cv2.imshow('window', convgray)
cv2.waitKey(0)
