import spidev
from flask import Flask, render_template
import cv2
import numpy as np
import picamera
import RPi.GPIO as GPIO
import time

#----------------------------------SPI----------------------------------
# SPI 인스턴스 생성 
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) # bus: 0, dev: 0(CE0, CE1 둘 중 하나가 0임)

# SPI 최대 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 읽어온 아날로그값을 디지털로 변환하여 리턴하는 함수
def analog_read(channel):
    #[byte_1, byte_2, byte_3]
    #byte_1 : 1
    #byte_2 : channel(0) + 8 = 0000 1000(2진수) << 4 - > 1000 0000
    #byte_3 : 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out
#----------------------------------SPI----------------------------------

#----------------------------------CV2----------------------------------
# model, config, classFile 설정
model = './dnn/bvlc_googlenet.caffemodel'
config = './dnn/deploy.prototxt'
classFile = './dnn/classification_classes_ILSVRC2012.txt'

classNames = None
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load a pre-trained neural network
net = cv2.dnn.readNet(model, config)
#----------------------------------CV2----------------------------------

#----------------------------------PICAMERA-----------------------------
path = '/home/pi/src6/08_project2'

# picamera 사용 준비
camera = picamera.PiCamera()

camera.resolution = (640, 480)
camera.start_preview()

# 카메라 대기
time.sleep(3)
print("Camera Ready")

camera.rotation = 180
#----------------------------------PICAMERA-----------------------------

#----------------------------------SERVO--------------------------------
SERVO_PIN1 = 22
SERVO_PIN2 = 27

# 서보모터(2개) 사용 준비
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN1, GPIO.OUT)
GPIO.setup(SERVO_PIN2, GPIO.OUT)

# 주파수 : 50Hz
pwm1 = GPIO.PWM(SERVO_PIN1, 50)
pwm1.start(10) # 시작 상태 : 열림
pwm2 = GPIO.PWM(SERVO_PIN2, 50)
pwm2.start(6) # 시작 상태 : 열림
#----------------------------------SERVO--------------------------------

#----------------------------------PIEZO--------------------------------
BUZZER_PIN = 15

GPIO.setup(BUZZER_PIN, GPIO.OUT)

# piezo buzzer 사용 준비
pwm = GPIO.PWM(BUZZER_PIN, 1)
#----------------------------------PIEZO--------------------------------

#----------------------------------FLASK--------------------------------
app = Flask(__name__)
species = "None"

# adminv2.html 파일 연동
@app.route("/")
def main():
    return render_template("adminv2.html")

# 15초마다 반복
@app.route("/manage") 
def manage(): 
    try:
        reading = analog_read(0)

        if reading < 300: # 조도센서 값이 일정 값 이하일 때 True

            # 사진 촬영
            camera.capture('%s/photo.jpg' % path)

            img = cv2.imread('photo.jpg')

            # blob 이미지 생성
            blob = cv2.dnn.blobFromImage(img, scalefactor=1, size=(224, 224), mean=(104, 117, 123))

            # blob 이미지를 네트워크 입력으로 설정
            net.setInput(blob)

            # 네트워크 실행 (순방향)
            detections = net.forward()

            # 가장 높은 값을 가진 클래스 얻기
            out = detections.flatten()
            classId = np.argmax(out)
            confidence = out[classId]

            # species 변수에 종 이름, 확률 기입
            species = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)

            # species 변수 반환
            return species
            

        else: # 일정 값 초과 시 오전으로 간주하고 False
            return "Not afternoon"
    except Exception as e:
        print(e)

# 웹에서 open barricade 버튼 클릭 시
@app.route("/open") 
def open():
    try:
        pwm1.ChangeDutyCycle(10) # 서보모터 2개를 open형태로
        pwm2.ChangeDutyCycle(6)
    except Exception as e:
        print(e)

# 웹에서 close barricade 버튼 클릭 시
@app.route("/close")
def close():
    try:
        pwm.start(10) # 피에조 부저 사용 준비
        
        pwm1.ChangeDutyCycle(6) # 서보모터 2개를 close형태로
        pwm2.ChangeDutyCycle(11)

        # 5초간 피에조 부저 울림
        pwm.ChangeFrequency(392)
        time.sleep(5) 

        pwm.stop()
    except Exception as e:
        print(e)

# 웹 호스트
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        # 사용한 개체들 정리
        spi.close()
        cv2.destroyAllWindows()
        camera.stop_preview()
        pwm1.stop()
        pwm2.stop()
        GPIO.cleanup()
#----------------------------------FLASK--------------------------------