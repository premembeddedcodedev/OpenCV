import cv2

image = cv2.imread('lane.jpg')
cv2.imshow('window', image)
cv2.waitKey(0)
