import RPi.GPIO as GPIO
import time

def PIN_ON(pin, tnum):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(tnum)
    GPIO.output(pin, GPIO.LOW)

LED_PIN = 4
YEL_PIN = 18
GRE_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(YEL_PIN, GPIO.OUT)
GPIO.setup(GRE_PIN, GPIO.OUT)

for i in range(100):
    PIN_ON(LED_PIN, 0.1)
    PIN_ON(YEL_PIN, 0.1)
    PIN_ON(GRE_PIN, 0.1)
    PIN_ON(YEL_PIN, 0.1)

GPIO.cleanup()