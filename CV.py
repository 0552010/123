import cv2 
import numpy as np

image = cv2.imread("20200408_180348.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(blurred,30,15)
result = np.hstack([gray,canny])
x = cv2.Sobel(gray,cv2.CV_16S,1,0)
y = cv2.Sobel(gray,cv2.CV_16S,0,1)
X = cv2.convertScaleAbs(x)
Y = cv2.convertScaleAbs(y)
out = cv2.addWeighted(X,0.5,Y,0.5,0)
#result = np.hstack([gray,out])

cv2.imwrite("123.jpg",result)
#cv2.imshow(result)
#cv2.waitkey(0)
