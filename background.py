import numpy as np
import cv2

cap = cv2.VideoCapture('looking.mp4')
ret = True
frameCounter = 0
previousFrame = None
nextFrame = None
iterations = 0

backgroundImage = cv2.imread("minecraft.jpg")

while (ret):
    ret, frame = cap.read()

    if frameCounter % 2 == 1:
        nextFrame = frame
    
    if frameCounter % 2 == 0:
        frameCounter = 0
        previousFrame = frame

    frameCounter = frameCounter + 1
    iterations = iterations + 1

    if iterations > 2:
            diff = cv2.absdiff(previousFrame, nextFrame)
            mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 3
    isMask = mask > th
    nonMask = mask <= th

    result = np.zeros_like(nextFrame, np.uint8)
    resized = cv2.resize(backgroundImage, (result.shape[1], result.shape[0]), interpolation = cv2.INTER_AREA)
    result[isMask] = nextFrame[isMask]
    result[nonMask] = resized[nonMask]
    cv2.imwrite("output" + str(iterations) + ".jpg", result)