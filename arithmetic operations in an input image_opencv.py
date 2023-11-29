import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('C:/Users/admin/Downloads/opencv.png')
img2=cv2.imread('C:/Users/admin/Downloads/jupyter.png')
add=img1 + img2
plt.imshow(add)
sub = img1 - img2
plt.imshow(sub)
mul = img1*img2
plt.imshow(mul)
div - img1 / img2
plt.imshow(div)
