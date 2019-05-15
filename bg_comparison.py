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

img_dir='/home/jody/opencvpython/bg_comparison/'


filelist=os.listdir(img_dir)

background=cv2.imread(os.path.join(img_dir, 'background.png') )
removeGreen(background)

for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".png")) or fichier == 'background.png':
        print(fichier)
        filelist.remove(fichier)
    else:
        image=cv2.imread(os.path.join(img_dir, fichier))
        removeGreen(image)
        #np subtraction and mean

        diff = cv2.absdiff(image, background)
        mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        th = 40
        imask =  mask>th

        canvas = np.zeros_like(image, np.uint8)
        canvas[imask] = image[imask]

        cv2.imshow('VIDEO', canvas)
        cv2.waitKey()

print(filelist)
