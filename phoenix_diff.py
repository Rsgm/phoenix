#!/bin/python
import cv2
import os
import time

epsilon = 10000 # this may be a bit low
r = []
g = []
b = []

c_r = []
c_g = []
c_b = []

warn = 0

while (True):
    time.sleep(1)

    warn -= 1
    if (warn <= 0):
        try:
            os.remove("/home/ryan/warn")
        except OSError:
            print ""

    # replace the last histograms
    r = c_r
    g = c_g
    b = c_b

    img = cv2.imread("/home/ryan/0.png", 0)

    c_r = cv2.calcHist([img], [0], None, [256], [0, 256])
    # c_g = cv2.calcHist([img], [1], None, [256], [0,256])
    # c_b = cv2.calcHist([img], [2], None, [256], [0,256])

    if (r == []):
        continue

    diff_r = 0
    diff_g = 0
    diff_b = 0
    for i in range(256):
        diff_r += abs(c_r[i][0] - r[i][0])
        # diff_g += abs(c_g[i] - g[i])
        # diff_b += abs(c_b[i] - b[i])

    diff = diff_r  # + diff_g + diff_b
    if (diff > epsilon and diff != 56320):
        warn = 5 #30
        f = open("/home/ryan/warn", "w")
        f.write("warning")
        f.close()
        print "diff"

    print diff

