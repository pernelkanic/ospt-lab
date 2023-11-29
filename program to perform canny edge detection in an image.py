import numpy as пр
import cv2 as cv
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/admin/Downloads/opencv.png')
edges = cv.Canny (img, 100, 200)
plt. subplot (121),plt.imshow(img, cmap = 'gray')
plt. title('Original Image'), plt.xticks ([]), plt.yticks([])
plt. subplot (122),plt. imshow(edges, cmap = 'gray')
plt. title('Edge Image'), plt.xticks ([]), plt.yticks ([])
plt.show()
