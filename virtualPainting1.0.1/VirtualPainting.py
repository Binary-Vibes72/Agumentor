import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

print("Processing...")
###############################
brushThickness = 15
eraserThickness = 100
###############################

folderPath = "Header"
myList = os.listdir(folderPath)

# print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
# print(len(overlayList))
header = overlayList[0]
drawColor = (13, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

pTime = 0
cTime = 0

while True:
    # 1. import the Image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!= 0:
        # print(lmList)

        #Tip of index and middle finger
        x1,y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection mode - two fingers are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("selection mode")
            # Checking for the click
            if y1 < 125:
                #Color1
                if 30 < x1 < 95:
                    header = overlayList[0]
                    drawColor = (13, 0, 255)
                # Color2
                elif 125 < x1 < 190:
                    header = overlayList[1]
                    drawColor = (52, 112, 255)
                # Color3
                elif 220 < x1 < 285:
                    header = overlayList[2]
                    drawColor = (1, 253, 255)
                # Color4
                elif 315 < x1 < 380:
                    header = overlayList[3]
                    drawColor = (0, 255, 102)
                # Color5
                elif 410 < x1 < 475:
                    header = overlayList[4]
                    drawColor = (252, 101, 1)
                # Color6
                elif 505 < x1 < 570:
                    header = overlayList[5]
                    drawColor = (253, 10, 173)
                # Color7
                elif 600 < x1 < 665:
                    header = overlayList[6]
                    drawColor = (255, 255, 255)

                # Eraser
                if 1160 < x1 < 1250:
                    header = overlayList[7]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1,y1-25), (x2,y2+25), drawColor, cv2.FILLED)


        # # 5. if drawing mode - index finger is up
        if fingers[1] and fingers[2]==False:
            cv2.circle(img, (x1, y1), 10, drawColor, cv2.FILLED)
            print("Drawing mode")
            if xp==0 and yp==0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1
        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

    #Frame Rate Capturing & Showing
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (18, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # setting the header image
    img[0:125,0:1280] = header
    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("image", img)
    cv2.waitKey(2)