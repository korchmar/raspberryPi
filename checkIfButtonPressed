import RPi.GPIO as GPIO
import time

button = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
while True:
    value = GPIO.input(button)
    if value:
        print("Pressed")
    else:
        print("Not Pressed")
    time.sleep(0.1)

GPIO.cleanup()
