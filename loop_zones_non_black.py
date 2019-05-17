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

background=cv2.imread(os.path.join(img_dir, 'background.png') )
filename="vlcsnap-00030.png"
image=cv2.imread(os.path.join(img_dir, filename))

bgheight, bgwidth, bgchannels = background.shape

def nothing(x):
  pass

cv2.namedWindow('Options')
cv2.createTrackbar('threshold','Options',0,255,nothing)
cv2.setTrackbarPos('threshold', 'Options', 40) # default threshold value

cv2.createTrackbar('width','Options',1,255,nothing)
cv2.setTrackbarPos('width', 'Options', 54)
cv2.createTrackbar('height','Options',1,255,nothing)
cv2.setTrackbarPos('height', 'Options', 48)
cv2.createTrackbar('nonzero','Options',1,3000,nothing)
cv2.setTrackbarPos('nonzero', 'Options', 1500)

while(1):

    nbzone = 0
    threshold  = cv2.getTrackbarPos('threshold','Options')
    zonewidth  = cv2.getTrackbarPos('width','Options')
    zoneheight = cv2.getTrackbarPos('height','Options')
    nonzerothresold = cv2.getTrackbarPos('nonzero','Options')

    height, width, channels = image.shape
    croped_by_width = width / zonewidth
    croped_by_height = height / zoneheight
    ypos = 0
    xpos = 0

    diff = cv2.absdiff(image, background)

    #mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    #threshold = 40
    imask =  diff>threshold

    canvas = np.zeros_like(image, np.uint8)
    canvas[imask] = image[imask]

    for y in xrange(croped_by_height): 
        for x in xrange(croped_by_width):
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

    #print("threshold = %d" % (threshold))
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

output = "background_comparison_%s.png" % threshold
print("output file:%s" % output)
cv2.imwrite(output, canvas)

cv2.destroyAllWindows()



