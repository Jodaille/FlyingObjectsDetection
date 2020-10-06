#!/usr/bin/env python
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname
from crop_utils import cropZone

img_dir='/home/jody/opencvpython/bg_comparison/'
img_dir = '/home/jody/VespaVelutina/FrelonDetecteurImages/pieces_jointes_15_09_2020/'

background=cv2.imread(os.path.join(img_dir, 'capture_2.jpg') )
filename="capture_52_F.JPG"
image=cv2.imread(os.path.join(img_dir, filename))

bgheight, bgwidth, bgchannels = background.shape

def nothing(x):
  pass

# default found params
threshold = 40
width     = 54
height    = 48
nonzero   = 1500

# GUI adjustments
cv2.namedWindow('Options')
cv2.createTrackbar('threshold','Options',0,255,nothing)
cv2.setTrackbarPos('threshold','Options', threshold) # default threshold value
cv2.createTrackbar('width',  'Options',1,255,nothing)
cv2.setTrackbarPos('width',  'Options', width)
cv2.createTrackbar('height', 'Options',1,255,nothing)
cv2.setTrackbarPos('height', 'Options', height)
cv2.createTrackbar('nonzero','Options',1,3000,nothing)
cv2.setTrackbarPos('nonzero','Options', nonzero)

while(1):

    nbzone = 0 # detected zones counter
    threshold  = cv2.getTrackbarPos('threshold','Options')
    zonewidth  = cv2.getTrackbarPos('width','Options')
    zoneheight = cv2.getTrackbarPos('height','Options')
    nonzerothresold = cv2.getTrackbarPos('nonzero','Options')

    height, width, channels = image.shape # image size

    # how many zones in image
    croped_by_width = width // zonewidth
    croped_by_height = height // zoneheight

    ypos = 0
    xpos = 0

    diff = cv2.absdiff(image, background)

    #threshold = 40
    imask =  diff>threshold

    canvas = np.zeros_like(image, np.uint8)
    canvas[imask] = image[imask]

    # loop to crop images and draw zone(s) with "non zeros pixels"
    for y in range(croped_by_height):
        for x in range(croped_by_width):
                crop = cropZone(canvas,xpos, ypos, zoneheight, zonewidth)
                destImgName = "crop_%s_x%d_y%d_h%d_w%d.jpg" % (filename,xpos, ypos, zoneheight, zonewidth)

                nonzero = cv2.countNonZero(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY))
                if (nonzero > nonzerothresold):
                    nbzone+=1
                    torender=image.copy()
                    cv2.rectangle(canvas,(xpos,ypos),(xpos + zonewidth,ypos + zoneheight),(0,0,255),3)
                    cv2.rectangle(torender,(xpos,ypos),(xpos + zonewidth,ypos + zoneheight),(0,0,255),3)
                    cv2.imshow('crop', crop)
                    cv2.imshow('source', torender)
                    #cv2.imwrite(destImgName, image)
                    print("nbzone %s xpos %d ypos %d nonzero %d" % (nbzone, xpos, ypos, nonzero))
                if (nbzone == 0):
                    print("No Zone")
                xpos =  xpos + zonewidth
        ypos = ypos + zoneheight
        xpos = 0

    cv2.imshow("VIDEO %s %s" % (bgheight, bgwidth), canvas)

    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

output = "background_comparison_%s.png" % threshold
print("output file:%s" % output)
cv2.imwrite(output, canvas)

cv2.destroyAllWindows()



