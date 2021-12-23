#HEAD
import RPi.GPIO as GPIO

LED_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#BODY
try:
    while True:
        val = input("1:on, 0:off, 9:exit > ")
        if val == '0':
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led off')
        elif val == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led on')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            break

finally:
    GPIO.cleanup()
    print('Cleanup and Exit')