#!/bin/python2
import cv2
import time
import os

cap = cv2.VideoCapture(0)
cap.set(3, 320)  # width
cap.set(4, 216)  # height
cap.set(5, 1)  # frame rate

n = 0
dt = .1
save_interval = 2

while (True):
    time.sleep(dt)
    n += dt

    if (n >= 2):
        n = 0

        try:
            os.remove("/home/ryan/9.png")
        except OSError:
            print ""  # ignroe

        for i in reversed(range(9)):
            try:
                os.rename("/home/ryan/{0}.png".format(i), "/home/ryan/{0}.png".format(i + 1))
            except OSError:
                print ""  # ignroe

    ret, frame = cap.read()
    cv2.imwrite("/home/ryan/0.png", frame)

cap.release()
