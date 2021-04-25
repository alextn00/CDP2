import cv2
from numpy import percentile
import numpy as np

img = cv2.imread('background.jpg', cv2.IMREAD_GRAYSCALE)
lower = percentile(img, 5)
upper = percentile(img, 100)
cv2.normalize(img, img, -lower, 800+upper, cv2.NORM_MINMAX)
# cv2.normalize(img, img, -lower, 100+upper, cv2.NORM_MINMAX)
cv2.imwrite('output.jpg', img)
sub_dst = cv2.subtract(img, 100)
cv2.imwrite('back2.jpg', sub_dst)