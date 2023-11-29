import matplotlib.pyplot as pIt
import cv2
image = cv2.imread("C:/Users/admin/Downloads/opencv.png")
font = cv2.FONT_HERSHEY_SIMPLEX
org = (10, 50)
fontScale = 1.5
color = (0,0,0)
thickness = 2
image = cv2.putText (image, 'OPENCV', org, font, fontScale, color, thickness, cv2.LINE_AA)
plt.imshow(image) 