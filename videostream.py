# Importing necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#initialize camera and grab ref

cam = PiCamera()
rawCapt = PiRGBArray(camera)

time.sleep(1)

#take image from camera
cam.capture(rawCapt, format="bgr")
image = rawCapt.array

#display img and wait for key
cv2.imshow("Image", image)
cv2.waitKey(0) 
