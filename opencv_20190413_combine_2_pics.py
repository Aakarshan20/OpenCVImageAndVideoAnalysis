import cv2
import numpy as np

#引入兩張圖
img1 = cv2.imread('3D-matplotlib.png')
img2 = cv2.imread('mainlogo.png')

#想把logo放在左上角 所以用背景圖建立了一個roi
rows, cols, _ = img2.shape
roi = img1[0:rows, 0:cols]

#設定浮水印
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#反正就是轉換
#小於220 轉為0(黑)
#反之 轉為255(白) 
ret, mask = cv2.threshold(img2gray,220,255, cv2.THRESH_BINARY_INV)
#cv2.imshow('mask', mask)#整張變黑白且黑白反轉

#再一次黑白反轉
mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask', mask_inv)


#背景
img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv)

#前景
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

#黏一黏
dst = cv2.add(img1_bg, img2_fg)

#黏完還給img1
img1[0:rows, 0:cols ] = dst


cv2.imshow('res',  img1)
cv2.imshow('mask_inv',  mask_inv)
cv2.imshow('img1_bg',  img1_bg)
cv2.imshow('img2_fg',  img2_fg)
cv2.imshow('dst',  dst)

cv2.waitKey(0)
cv2.destroyAllWIndows()

