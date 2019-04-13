import numpy as np
import cv2


img = cv2.imread('G20.jpg', cv2.IMREAD_COLOR)

#img[55,55] = [255,255,255]#x=55, y=55

#px = img[55,55]

#print(img[55,55])
#region of image
img[100:150, 100:150] = [255,255,255]#100-150, 100-150 的地方填上白色

watch_face = img[37:111, 107:194]#複製37-111, 107-194的圖片

img[0:74, 0:87] = watch_face#貼到0-74, 0-87的地方


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
