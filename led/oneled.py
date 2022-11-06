# pip install RPi.GPIO

import RPi.GPIO as GPIO
import time
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
x = 0
while x < 10:
	GPIO.output(LED_PIN, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(LED_PIN, GPIO.LOW)
	time.sleep(2)
	x = x + 1
GPIO.cleanup()
