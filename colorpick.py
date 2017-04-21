import numpy as np
import argparse
import cv2
import os, sys

#from globalspot import *
import globalspot

def contourFilter(imagefile):
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-q", "--query", required = True, help = "path to query image")
    # ap.add_argument("-o", "--write", required = True, help = "path to output file")
    # args = vars(ap.parse_args())
    
    # image = cv2.imread(args["query"])
    image = cv2.imread(imagefile)
    orig = image.copy()

    #
    cv2.imshow('orig', orig)
    

    hsv = cv2.cvtColor(orig, cv2.COLOR_BGR2HSV)
    
    #
    cv2.imshow('hsv', hsv)
    

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    #
    cv2.imshow('mask', mask)


    # yellow = np.uint8([[[0, 255, 255]]])
    # hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
    # print(hsv_yellow)
    
    res = cv2.bitwise_and(orig, orig, mask= mask)
    
    #
    cv2.imshow('res', res)


    im2, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours, key = cv2.contourArea, reverse = True[:10]
    
    # cv2.waitKey(0)

    return contours
            

def contourCount(contours):
    i = 0;
    
    for c in contours:
        i += 1
        
    return i


def computeContours(imagefile):
    a = contourFilter(imagefile)
    b = contourCount(a)
    print("Spots in this image: " + str(b))
    globalspot.spotcount += b 


# print(type(contourFilter()))
        

# print(contourCount(a))
 

# fd = os.open("spotcount.txt",os.O_RDWR|os.O_CREAT)
# ret = os.write(fd, str(i))
# os.close(fd)

