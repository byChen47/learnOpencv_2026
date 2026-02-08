import cv2

img1 = cv2.imread('image.png',1)



cv2.namedWindow('image1',cv2.WINDOW_NORMAL)
cv2.imshow('image1',img1)


cv2.waitKey(0)