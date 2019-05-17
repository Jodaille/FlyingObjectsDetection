#!/usr/bin/env python
# threshold_trackbar.py
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname
from colors_utils import removeGreen

img_dir='/home/jody/opencvpython/bg_comparison/'

background=cv2.imread(os.path.join(img_dir, 'background.png') )
image=cv2.imread(os.path.join(img_dir, "vlcsnap-00026.png"))

#grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#graybg  = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
def nothing(x):
  pass

cv2.namedWindow('Options')
cv2.createTrackbar('threshold','Options',0,255,nothing)
cv2.setTrackbarPos('threshold', 'Options', 40) # default threshold value

while(1):

    threshold = cv2.getTrackbarPos('threshold','Options')

    diff = cv2.absdiff(image, background)
    #mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    #threshold = 40
    imask =  diff>threshold

    canvas = np.zeros_like(image, np.uint8)
    canvas[imask] = image[imask]

    cv2.imshow('VIDEO', canvas)

    print("threshold = %d" % (threshold))
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

output = "background_comparison_%s.png" % threshold
print("output file:%s" % output)
cv2.imwrite(output, canvas)

cv2.destroyAllWindows()
