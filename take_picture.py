# THis script will take the picture with the pic and send it or store. 
import time
from picamera import PiCamera
from time import sleep

picamera = PiCamera()
camera.start_preview()
camera.capture('/home/timecmdr/images/img{timestamp:%H-%M-%S-%f}.jpg')
