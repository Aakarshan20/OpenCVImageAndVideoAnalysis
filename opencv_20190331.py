import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pingWei.jpg', 0)

'''
cv2.imshow('標題', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [80,100], 'r', linewidth=5)
plt.show()

cv2.imwrite('pingWei4.jpg',img)
