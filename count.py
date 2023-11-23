import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

img = cv2.imread('output.png')  # open the image

# creating boxes around objects
box, label, count = cv.detect_common_objects(img)
output = draw_bbox(img, box, label, count)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.imshow(img1)
plt.show()

print("No of persons : " + str(len(label)))
