import cv2
import numpy as np
# import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import dlib
# Loading image
image = cv2.imread('sample11.jpg')

kernel = np.ones((50, 50), np.uint8)


closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

rt, thresholded_image = cv2.threshold(closed_image, 30, 255, cv2.THRESH_BINARY)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rt2, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

black_mask_thresholded = cv2.cvtColor(thresholded_image, cv2.COLOR_BGR2GRAY)
rt3, black_mask_thresholded = cv2.threshold(
    black_mask_thresholded, 20, 255, cv2.THRESH_BINARY)


mask = np.logical_and(image == 0, black_mask_thresholded == 0)
# print(mask)
image[mask] = 255

cv2.imwrite("output.png", image)
cv2.imshow("Image: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
