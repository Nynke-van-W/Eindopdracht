import cv2
import numpy as np
import random

img = cv2.imread('bord.jpg')
cv2.imshow("img", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 10, 3, 0.1)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("hoeken", img)
# print(dst[0])
if cv2.waitKey(0) & 0xff == 27:
    cv2.destryAllWindows()
