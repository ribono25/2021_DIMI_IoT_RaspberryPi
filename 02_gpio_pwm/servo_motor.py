import RPi.GPIO as GPIO
import time

SERVO_PIN1 = 22
SERVO_PIN2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN1, GPIO.OUT)
GPIO.setup(SERVO_PIN2, GPIO.OUT)

#주파수 : 50Hz
pwm1 = GPIO.PWM(SERVO_PIN1, 50)
pwm1.start(10) #open
pwm2 = GPIO.PWM(SERVO_PIN2, 50)
pwm2.start(6) #open

try:
    while True:
        val = input('1: open 2: close 9: exit >')
        if val == '1':
            pwm1.ChangeDutyCycle(10)
            pwm2.ChangeDutyCycle(6)
        elif val == '2':
            pwm1.ChangeDutyCycle(6)
            pwm2.ChangeDutyCycle(11)
        else:
            break
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()