# packages
from picamera import PiCamera
from time import sleep
from picamera.array import PiRGBArray
import CV2
# camera setting
camera = PiCamera()
camera.resolution = (256, 256)
rawCapture = PiRGBArray(camera, size=(256, 256))
# wait time
camera.start_preview()
sleep(1)
# capture image
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
camera.stop_preview()
# save and display image
cv2.imwrite('image.jpg',image)
cv2.imshow("Image", image)
cv2.waitKey(0)
