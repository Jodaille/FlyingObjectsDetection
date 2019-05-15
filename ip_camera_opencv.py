#!/usr/bin/env python
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname


nbframe=0

vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.201/2")
#fps = vcap.get(cv2.CV_CAP_PROP_FPS)
print(cv2.__version__)
while(1):


    ret, frame = vcap.read()
    if not ret:
        break
    nbframe +=1

    if nbframe % 20 == 0:
        print(nbframe)
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
