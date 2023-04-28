# THis script will take the picture with the pic and send it or store. 
import time
from picamera import PiCamera
from time import sleep

camera = PiCamera()
timestr = time.strftime("%Y%m%d-%H%M%S")
camera.capture(f'images/img{timestr}.jpg')

