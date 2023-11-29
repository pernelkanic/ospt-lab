import cv2
img = cv2.imread('C:/Users/Tcs/Downloads/leo.jpg')
h,w,c = img.shape
print('width',w)
print ('height', h)
print('channel',c)