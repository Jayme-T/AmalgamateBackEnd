#!/usr/bin/python
import RPi.GPIO as GPIO
import time


# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'
def turn(): 
   GPIO.setmode(GPIO.BCM)

   for i in pinList: 
       GPIO.setup(i, GPIO.OUT) 
       GPIO.output(i, GPIO.HIGH)

   # time to sleep between operations in the main loop

   SleepTimeL = 3

   # main loop

   try:
     GPIO.output(2, GPIO.LOW)
     time.sleep(SleepTimeL);  

     GPIO.cleanup()

   # End program cleanly with keyboard
   except KeyboardInterrupt:

     # Reset GPIO settings
     GPIO.cleanup()



