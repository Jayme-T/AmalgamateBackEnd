#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]
def relay():
   for i in pinList:
       GPIO.setup(i, GPIO.OUT)
       GPIO.output(i, GPIO.HIGH)

   # time to sleep between operations in the main loop

   SleepTimeL = 2

   # main loop
