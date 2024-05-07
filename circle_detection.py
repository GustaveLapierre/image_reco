import cv2
import numpy as np


def find_circle_border(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(gray_blurred,
                               cv2.HOUGH_GRADIENT, 1.5, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            return (i[0], i[1], i[2])  # (center_x, center_y, radius)
    return None