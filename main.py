import cv2
import numpy as np

init_img = cv2.imread('/Users/gustave/Downloads/IMG_9244.png')

x, y, w, h = 600, 1500, 1700, 1400
init_img = init_img[y:y+h, x:x+w]

gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)
_, edges = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('edges', edges)

hsv = cv2.cvtColor(init_img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

kernel = np.ones((13, 13), np.uint8)
mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)

cv2.imshow('mask', mask_red)

cv2.waitKey(0)
cv2.destroyAllWindows()

