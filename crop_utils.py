#!/usr/bin/env python
import cv2
def cropZone(image,xpos, ypos, height, width):
    #print("cropZone xpos %d ypos %d height %d width %d" % (xpos, ypos, height, width))
    crop = image[ypos:ypos+height, xpos:xpos+width]
    return crop

