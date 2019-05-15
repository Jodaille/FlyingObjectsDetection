#!/usr/bin/env python
# import the necessary packages

import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname
#from colors_utils import removeGreen

img_dir='/home/jody/vlcsnap/'
background=cv2.imread(os.path.join(img_dir, 'vlcsnap-00241.png') )

## Read
img = background


#removeGreen(background)
cv2.imshow("background", background)
# add blur because of pixel artefacts 
#img = cv2.GaussianBlur(img, (5, 5),5)
# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# set lower and upper color limits
lower_val = (40, 100, 100)
lower_val = (36, 25, 25)
upper_val = (60,255,200)
upper_val = (71,255,255)
# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_val, upper_val)
# apply mask to original image
res = cv2.bitwise_and(img,img, mask= mask)

diff_img = img - res
#show imag
cv2.imshow("Result", res)
cv2.imshow("diff_img", diff_img)
cv2.imwrite(os.path.join(img_dir,"diff_img.jpg"), diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
