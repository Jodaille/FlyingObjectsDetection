#!/usr/bin/env python
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname
from colors_utils import removeGreen

img_dir='/home/jody/vlcsnap/'
background=cv2.imread(os.path.join(img_dir, 'vlcsnap-00239.png') )
removeGreen(background)
nbframe=0

vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.201/2")
#fps = vcap.get(cv2.CV_CAP_PROP_FPS)
print(cv2.__version__)
while(1):


    ret, frame = vcap.read()
    if not ret:
        break
    nbframe +=1

    if nbframe % 2 == 0:
        print(nbframe)

        removeGreen(frame)
        nextbackground=frame
        diff = cv2.absdiff(frame, background)
        mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        th = 25
        imask =  mask>th

        canvas = np.zeros_like(frame, np.uint8)
        canvas[imask] = frame[imask]
        
        nextbackground=background

        cv2.imshow('VIDEO', canvas)
        #cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
