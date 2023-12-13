import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

try:
    while True:
        GPIO.output(2, 1)  # turn ON LED
        time.sleep(1)  # wait 1 second
        GPIO.output(2, 0)  # turn OFF LED
        time.sleep(1)  # wait 1 second
except KeyboardInterrupt:
    GPIO.cleanup()
