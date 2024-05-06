import cv2
import numpy as np

init_img = cv2.imread('/Users/gustave/Downloads/IMG_9244.png')

x, y, w, h = 600, 1500, 1700, 1400
init_img = init_img[y:y+h, x:x+w]

blue, green, red = cv2.split(init_img)

mask = (red > 1.5 * green) & (red > 1.5 * blue)

mask = np.uint8(mask * 255)

result = cv2.bitwise_and(init_img, init_img, mask=mask)

gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)
_, edges = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('Red Dominant Areas', result)
cv2.imshow('edges', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

