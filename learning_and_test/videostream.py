# Importing necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#initialize camera and grab ref

cam = PiCamera()
cam.resolution = (640, 480)
cam.framerate = 32
rawCapt = PiRGBArray(cam, size=(640, 480))

time.sleep(1)

for frame in cam.capture_continuous(rawCapt, format="bgr", use_video_port=True):
	#grab numpy array
	image = frame.array
	
	#display frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
	#clear stream for next
	rawCapt.truncate(0)
	
	#break on q
	if key == ord("q"):
		break
