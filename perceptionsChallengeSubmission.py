##imports
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

input = cv2.imread('/content/red.png')
##splitting image in half
height, width, _ = input.shape
leftHalf = input[:, :width//2].copy()
rightHalf = input[:, width//2:].copy()
##function to find cones, find centroids and draw lines
def findConeDraw(image):
    hsvCS = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowerR = np.array([0, 100, 100])
    upperR = np.array([10, 255, 255])
    mask = cv2.inRange(hsvCS, lowerR, upperR)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    height, width, _ = image.shape
    upperFourth = height // 4
    centroids = []
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                if cY > upperFourth:
                    centroids.append((cX, cY))
                    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    for i in range(len(centroids) - 1):
        cv2.line(image, centroids[i], centroids[i + 1], (0, 255, 0), 2)

##using the function on each half of the picture and merging
findConeDraw(leftHalf)
findConeDraw(rightHalf)
merged = np.hstack((leftHalf, rightHalf))

cv2_imshow(merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
