import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPActiveBuzzer_PIN = 19

GPIO.setup(GPActiveBuzzer_PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(GPActiveBuzzer_PIN, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(GPActiveBuzzer_PIN, GPIO.LOW)
    time.sleep(2)