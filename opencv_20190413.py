import cv2
import numpy as np

img1 = cv2.imread('3D-matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
#img2 = cv2.imread('image.jpg')#不同尺寸不能相加

#add = img1+img2 顏色跑掉

#add = cv2.add(img1, img2)#相加後 超過255的會視為255

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)#加入權重 避免overflow

#cv2.imshow('add', add)

cv2.imshow('add',  weighted)
cv2.waitKey(0)
cv2.destroyAllWIndows()

