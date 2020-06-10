import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX
lower_green = np.array([35, 110, 106])  
upper_green = np.array([77, 255, 255])  
lower_red = np.array([0, 127, 128])  
upper_red = np.array([10, 255, 255])  
#https://www.tfzx.net/article/6838812.html
cap = cv2.VideoCapture('1.mp4') 
#cap = cv2.VideoCapture(0)
if (cap.isOpened()):  
    flag = 1
else:
    flag = 0
num = 0
if (flag):
    while (True):
        ret, frame = cap.read()  
       
        if ret == False:  
            break
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_green = cv2.inRange(hsv_img, lower_green, upper_green)  
        mask_red = cv2.inRange(hsv_img, lower_red, upper_red) 
        mask_green = cv2.medianBlur(mask_green, 7)  
        mask_red = cv2.medianBlur(mask_red, 7)  
        mask = cv2.bitwise_or(mask_green, mask_red)
        mask_green, contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        mask_red, contours2, hierarchy2 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        #for cnt in contours:
            #(x, y, w, h) = cv2.boundingRect(cnt)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            #cv2.putText(frame, "Green", (x, y - 5), font, 0.7, (0, 255, 0), 2)

        for cnt2 in contours2:
            (x2, y2, w2, h2) = cv2.boundingRect(cnt2)
            cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 255), 2)
            cv2.putText(frame, "red", (x2, y2 - 5), font, 0.7, (0, 0, 255), 2)
        num = num + 1
        cv2.imshow("dection", frame)
        cv2.imwrite("imgs/%d.jpg"%num, frame)
        if cv2.waitKey(20) & 0xFF == 27:
            break
cv2.waitKey(0)
cv2.destroyAllWindows()