#!/usr/bin/python3
# This is the code that drives the Fucker-Feeder-9001
# Author: Alec J. Davidson
# Version: 1.0
# Date Modified: 11/13/19
# Purpose: To feed cats every 12 hours

# import cv2
import RPi.GPIO as GPIO
from time import sleep
# from datetime import datetime


GPIO.setmode(GPIO.BOARD)

Motor1 = 16 # EN = pin 16
Motor2 = 18 # IN1 = pin 18
Motor3 = 12 # IN2 = pin 12

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

print ("FORWARD MOTION")
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)

sleep(15) # Turns auger for 15 seconds. Outputs around a cup of food per auger.

GPIO.cleanup()

