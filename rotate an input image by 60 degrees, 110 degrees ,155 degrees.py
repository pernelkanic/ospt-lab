import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("C:/Users/admin/Downloads/opencv.png")
from scipy import ndimage
plt.imshow(ndimage.rotate(image, 60))
plt.imshow(ndimage.rotate(image, 110))
plt.imshow(ndimage.rotate(image, 150))