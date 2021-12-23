# servo_moter.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

#주파수
GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5) #0도

try:
    while True:
        val = input('1: 0도, 2: -90도, 3: +90도, 9: Exit >')
        if val == '1': 
            pwm.ChangeDutyCycle(7.5)
        elif val == '2':        
            pwm.ChangeDutyCycle(5)
        elif val == '3':
            pwm.ChangeDutyCycle(10) 
        elif val == '9':
            break
finally:    
    pwm.stop()
    GPIO.cleanup()