import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


img2 = np.zeros((450, 450, 3), np.uint8)

img2[:] = (0, 0, 255)
# 文字
text = '招財\n進寶'

# 指定 TTF 字體檔
fontPath = "./msjh.ttf"

# 載入字體
font = ImageFont.truetype(fontPath, 192)

# 將 NumPy 陣列轉為 PIL 影像
imgPil = Image.fromarray(img2)

# 在圖片上加入文字
draw = ImageDraw.Draw(imgPil)
draw.text((30, 30),  text, font = font, fill = (0, 0, 0))

# 將 PIL 影像轉回 NumPy 陣列
img = np.array(imgPil)




cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
