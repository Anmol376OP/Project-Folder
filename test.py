import cv2

from scipy import ndimage
img = cv2.imread("output.png")
img_copy = 255-img
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# Finding contours for the thresholded image
opening1 = cv2.morphologyEx(img_copy, cv2.MORPH_OPEN, kernel, iterations=1)
opening2 = cv2.morphologyEx(img_copy, cv2.MORPH_OPEN, kernel, iterations=5)

# opening2=255-opening2
opening1 = 255-opening1

labeled, nr_objects = ndimage.label(opening2)
print("Number of head is - " + str(nr_objects))

cv2.imshow("img", opening2)

cv2.waitKey(0)
cv2.destroyAllWindows()
# print(img)
