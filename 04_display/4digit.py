import RPi.GPIO as GPIO 
import time #for sleeping
from random import * #for random()

LED_PIN = 26 #led
SIC_PIN = 19 #switch
PIR_PIN = 21 #pir
GLED_PIN = 14 #led 2 (PIR 감지 시 켜짐)

SEGMENT_PINS = [13, 6, 5, 11, 9, 10, 22] #display 4-digits FND
DIGIT_PINS = [27, 17, 4, 2] 
DP = 3

GPIO.setmode(GPIO.BCM) # 초기 GPIO 설정
GPIO.setup(LED_PIN, GPIO.OUT) #led red gpio out
GPIO.setup(SIC_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #switch pull up down
GPIO.setup(PIR_PIN, GPIO.IN) # pir sensor gpio in
GPIO.setup(GLED_PIN, GPIO.OUT) # led green gpio out

time.sleep(5)
print('PROGRAM ready...')

n1 = 0 # 4-digits FND 표시 처음값 0000
n2 = 0
n3 = 0
n4 = 0

for segment in SEGMENT_PINS: #4 digits 초기 GPIO 설정
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PINS: #4 digits초기 GPIO 설정
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

#Common Cathod 일 경우 : LOW -> LED OFF, HIGH -> LED ON
data = [[1,1,1,1,1,1,0], # 0
        [0,1,1,0,0,0,0], # 1
        [1,1,0,1,1,0,1], # 2
        [1,1,1,1,0,0,1], # 3
        [0,1,1,0,0,1,1], # 4
        [1,0,1,1,0,1,1], # 5
        [1,0,1,1,1,1,1], # 6
        [1,1,1,0,0,0,0], # 7
        [1,1,1,1,1,1,1], # 8
        [1,1,1,0,0,1,1]] # 9

def display(digit, number): #자리수, 숫자
    for i in range(len(DIGIT_PINS)): #해당하는 자릿수 핀만 LOW 설정
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

    #숫자 출력
    for i in range(len(SEGMENT_PINS)): #0부터 6까지
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)

try:
    while True:
        val = GPIO.input(SIC_PIN) #switch value variable 눌렀을 때 1, 아니면 0
        PIRval = GPIO.input(PIR_PIN) #PIR value variable 감지할 때 1, 아니면 0
        GPIO.output(LED_PIN, val) #GPIO.HIGH = 1
        GPIO.output(GLED_PIN, PIRval) #GPIO.HIGH = 1
        if val == 1: #버튼을 누를 시 랜덤 값 저장 (n1, n2, n3, n4에)
            n1 = randrange(10)
            n2 = randrange(10) #0부터 9까지 랜덤 정수 저장
            n3 = randrange(10)
            n4 = randrange(10)

        display(1, n1) #4-digits fnd 디스플레이 출력 (랜덤 지정한 값들)
        display(2, n2)
        display(3, n3)
        display(4, n4)
finally:
        GPIO.cleanup()
        print("cleanup and exit")