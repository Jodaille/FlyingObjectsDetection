#!/usr/bin/env python
# Crop a zone in image  
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname

# example:
# ./cromp_image_zone.py -i /home/jody/opencvpython/bg_comparison/background.png --xpos 830 --ypos 20 --width 200 --height 650

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to the input image")
parser.add_argument('--width', nargs='?', const=110, type=int, default=110,
	help="Width zone")
parser.add_argument('--height', nargs='?', const=110, type=int, default=110,
        help="height zone")
parser.add_argument('--xpos', nargs='?', const=0, type=int, default=0,
        help="x pos")
parser.add_argument('--ypos', nargs='?', const=0, type=int, default=0,
        help="y pos")

args = vars(parser.parse_args())
print(args);

# open image and get infos
image = cv2.imread(args["image"])
height, width, channels = image.shape

print(image.shape)

h=args["height"]
w=args["width"]

croped_by_width = width / w
croped_by_height = height / h
ypos = 0
xpos = 0

crop = image[args["ypos"]:args["ypos"]+h, args["xpos"]:args["xpos"]+w]

cv2.imshow('Image CROP', crop)
cv2.imshow('Image source', image)
cv2.waitKey()
