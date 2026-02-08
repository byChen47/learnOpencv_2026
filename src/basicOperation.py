import cv2

img = cv2.imread('image.png',1)
positionx = img[100,90]
print(positionx)

# 只获取蓝色blue的通道
px_blue = img[100,90,0]
print(px_blue)

# img[100,90] = [255,255,255]
# print(img[100,90])

print(img.shape)
height,weight,channels = img.shape

print(img.dtype)
print(img.size)

face = img[100:500,50:300]
cv2.imshow('face',face)
cv2.waitKey(0)