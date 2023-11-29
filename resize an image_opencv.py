import cv2
img=cv2.imread('C:/Users/Tcs/Downloads/ak.jpg')
cv2.imshow('Org',img)
res=cv2.resize(img, (600, 450))
cv2.imshow('Resized', res)
cv2.waitkey(0)
cv2.destroyAllwindows()
