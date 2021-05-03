import cv2
import numpy as np

reading = cv2.VideoCapture('reading.mp4')
look = cv2.VideoCapture('looking.mp4')
camera = cv2.VideoCapture(0)

fps = reading.get(cv2.CAP_PROP_FPS)
delay = int(((1/int(fps)) * 1000)/5)

frame_counter = 0

i = 0

ret = True

def show(frame):
    if frame.any() != None:
        cv2.imshow('frame', frame)

while (ret):
    if i == 1:
        ret, frame = reading.read()
        frame_counter += 1

        if frame_counter == reading.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0
            reading.set(cv2.CAP_PROP_POS_FRAMES, 0)

        show(frame)
    
    if i == 0:
        ret, frame = look.read()
        frame_counter += 1

        if frame_counter == look.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0
            look.set(cv2.CAP_PROP_POS_FRAMES, 0)

        show(frame)

    if i == 2:
        ret, frame = camera.read()

        show(frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
    if cv2.waitKey(delay) & 0xFF == ord('f') and i == 0:
        i = 1
    if cv2.waitKey(delay) & 0xFF == ord('f') and i == 1:
        i = 0
    if cv2.waitKey(delay) & 0xFF == ord('o'):
        i = 2
    if cv2.waitKey(delay) & 0xFF == ord('o') and i == 2:
        i = 0

reading.release()