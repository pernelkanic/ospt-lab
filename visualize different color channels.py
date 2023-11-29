import cv2
img=cv2.imread('C:/Users/admin/Downloads/opencv.png')
B, G, R = cv2. split (img)
print (B)
print(G)
print (R)