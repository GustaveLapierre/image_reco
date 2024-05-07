import cv2
import numpy as np

from circle_detection import find_circle_border

init_img = cv2.imread('/Users/gustave/Downloads/IMG_9244.png')

x, y, w, h = 600, 1500, 1700, 1400
init_img = init_img[y:y+h, x:x+w]

blue, green, red = cv2.split(init_img)

mask = (red > 1.5 * green) & (red > 1.5 * blue)

mask = np.uint8(mask * 255)

red_circle = cv2.bitwise_and(init_img, init_img, mask=mask)

red_image = np.zeros((h, w, 3), dtype=np.uint8)
red_image[:] = [0, 0, 50]

black_image = np.zeros((h, w, 3), dtype=np.uint8)
black_image[:] = [0, 0, 0]

fully_red_image = np.zeros((h, w, 3), dtype=np.uint8)
fully_red_image[:] = [0, 0, 200]

enhanced_red = np.where(red_circle > red_image, fully_red_image, black_image)

center_x, center_y, radius = find_circle_border(enhanced_red)
image = cv2.circle(enhanced_red, (center_x, center_y), radius, (0, 255, 0))
image2 = cv2.circle(init_img, (center_x, center_y), radius, (0, 255, 0))


gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)
_, edges = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Red Dominant Areas', enhanced_red)
cv2.imshow('original', image2)
cv2.imshow('line', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

