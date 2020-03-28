import cv2

image = cv2.imread('pig.jpg')
image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('pig_gray.jpg',image_g)