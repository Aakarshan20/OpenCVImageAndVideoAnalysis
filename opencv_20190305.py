import cv2
import numpy as np
##import matplotlib as plt
import matplotlib.pyplot as plt

img = cv2.imread('pingWei.jpg', cv2.IMREAD_GRAYSCALE)

##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([200,50],[200,60], 'c', linewidth=5)
plt.show()
