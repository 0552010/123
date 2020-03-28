import cv2

img = cv2.imread('pig_gray.jpg',0)
ret, out = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('pig_threshold.jpg',out) 