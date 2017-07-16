# packages
from picamera import PiCamera
from time import sleep
from picamera.array import PiRGBArray
import cv2
# camera setting
camera = PiCamera()
camera.resolution = (256, 256)
rawCapture = PiRGBArray(camera, size=(640, 480))
# wait time
camera.start_preview();
time.sleep(1)
# capture frames 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream 
	rawCapture.truncate(0)
	# break from loop, if q is pressed
	if key == ord("q"):
		break
