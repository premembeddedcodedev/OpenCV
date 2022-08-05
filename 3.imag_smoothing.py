import cv2
import numpy as np

image = cv2.imread('lane.jpg')

array = np.copy(image)
# if we do array = image -- it will modify the original when array variable changes

convgray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(convgray, (5, 5), 0) #it will reduce the noise in the image by smoothing

cv2.imshow('window', blur)
cv2.waitKey(0)
