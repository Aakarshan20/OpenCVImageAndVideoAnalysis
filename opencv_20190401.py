import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread('Africa.jpg', cv2.IMREAD_COLOR)

#畫線
#line(畫布, 起始點, 結束點, (B,G,R), 線寬(負值代表填滿 負多少都一樣)) (255,255,255)=白色
cv2.line(img, (0,0), (150,150), (255, 0, 255), 15)

#畫矩型
#rectangle(畫布, 左上點, 右下點, (B,G,R), 線寬(負值代表填滿 負多少都一樣))
cv2.rectangle(img, (15,25), (200,150), (0,255,255), 5)

#畫圓
#circle(畫布, 中心, 直徑, (B,G,R), 線寬(負值代表填滿 負多少都一樣))
cv2.circle(img, (150,150), 80, (0,0,255), -3)


#畫多邊型
#點的列表 使用np.array包裝
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

#pts = pts.reshape((1-,1,2))#變型
#True 代表最後一點要連上第一個點
cv2.polylines(img, [pts], True, (0,255,0),2)


font = cv2.FONT_HERSHEY_SIMPLEX
#中文有亂碼
#cv2.putText(img, 'OpenCV Tuts!中文', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1.4, (200,255,255), 2, cv2.LINE_AA)





cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
