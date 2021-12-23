import RPi.GPIO as GPIO
import time

BUZZER_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [392,392,440,440,392,392,330,392,392,330,330,294,392,392,440,440,392,392,330,392,330,294,330,262]

try:
    for i in range(0, len(melody)):
        pwm.ChangeFrequency(melody[i])
        time.sleep( 0.5)
        if i == 6 or i == 18: time.sleep(0.5)
        if i == 11 or i == 23: time.sleep(1)
        
finally:
    pwm.stop()
    GPIO.cleanup()