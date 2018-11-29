import cv2
import numpy as np


camera = cv2.VideoCapture(0)
# 初始化平均影像

firstframe = None

while True:
    ret, frame = camera.read()    
    
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstframe is None:
        firstframe = gray
        continue
    frameDelta = cv2.absdiff(firstframe, gray)
    # 篩選出變動程度大於門檻值的區域
    # cv2.threshold (src, thresh, maxval, type)  type get 0~4 
    thresh = cv2.threshold(frameDelta, 10, 255, 1)[1]
    thresh = cv2.dilate(thresh, None, iterations = 2)
    cntImg, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        # 忽略太小的區域
        if cv2.contourArea(c) < 25:
            continue
            
        # 偵測到物體，可以自己加上處理的程式碼在這裡...

        # 計算等高線的外框範圍
        (x, y, w, h) = cv2.boundingRect(c)
        if x is not 0 and y is not 0 and w is not 640 and h is not 480:
#             print(x, y, w, h)
#  setup area
            if 0 <= x <= 160 and y < 200:
#                 print('A',x)
                printItem('A')
            elif 160 <= x <= 320 and y < 200:
#                 print('B',x)
                printItem('B')
            elif 320 <= x <= 480 and y < 200:
#                 print('C',x)
                printItem('C')
            else:
#                 print('D',x)
                printItem('D')
#         175 64 22 14
#         175 64 24 14
#         201 85 11 8
        # 613 114 8 9
        # 627 80 13 40
        # 613 114 8 9

        # 畫出外框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
   
    # 畫出等高線（除錯用）
#     cv2.drawContours(frame, cnts, -1, (0, 255, 255), 2)
    # 計算等高線的外框範圍
    x, y, w, h = cv2.boundingRect(thresh)
    # 畫出外框
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("Thresh", thresh)
#     cv2.imshow("frame2", frameDelta)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
        
tempX = "s"

def printItem(item):
    global tempX
    if tempX != item:
        tempX = item
        print(tempX)
        if tempX =='A':
        #    click(1600,300)
             print('A')
        if tempX =='B':
        #    click(300,300)
          print('B')
        if tempX =='C':
        #    click(800,800)
          print('C')
