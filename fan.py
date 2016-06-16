#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


if len(sys.argv) > 1:
        if sys.argv[1] == "start":
                GPIO.output(18, GPIO.HIGH)
        elif sys.argv[1] == "stop":
                GPIO.output(18, GPIO.LOW)
else:
        while True:
                if float(getCPUtemperature()) > 40:
                        GPIO.output(18, GPIO.HIGH)
                else:
                        GPIO.output(18, GPIO.LOW)
