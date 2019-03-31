import cv2

img = cv2.imread('image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('123',gray_img)
cv2.imshow('456',img)
cv2.waitKey(0)
cv2.destoryAllWindows()
