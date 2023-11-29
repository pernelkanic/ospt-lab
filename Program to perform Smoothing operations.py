import cv2
import matplotlib.pyplot as plt
img = cv2.imread("C:/Users/admin/Downloads/opencv.png")
plt.imshow(cv2.blur(img,(10,10)))
plt.imshow(cv2.GaussianBlur(img,(5,5),sigmaX=0))
plt.imshow(cv2.medianBlur(img,5))
plt.imshow(cv2.bilateralFilter(img, 15, 75, 75))