#!/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

led_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.5)

try:
    while True:
            pass

except KeyboardInterrupt:
        GPIO.cleanup()
