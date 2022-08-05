import cv2
import numpy as np

image = cv2.imread('lane.jpg')

array = np.copy(image)
# if we do array = image -- it will modify the original when array variable changes

convgray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(convgray, (5, 5), 0) #it will reduce the noise in the image by smoothing

canny = cv2.Canny(blur, 50, 150) # 2nd, 3rd arguements are for threshold Low and High respectively
#also canny applies 5x5 matrix (kernel) to identify the edges(black meeting white in the lanes image)

cv2.imshow('window', canny)
cv2.waitKey(0)
