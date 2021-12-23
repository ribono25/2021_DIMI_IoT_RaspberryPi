import spidev # SPI
import RPi.GPIO as GPIO # GPIO
from flask import Flask, render_template # Web Flask
import picamera # PiCamera
import cv2 # opencv
import numpy as np
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

#----------------------------------GPIO---------------------------------
LED_PIN = 18 # 추후 기입
PIR_PIN = 4 # 추후 기입

GPIO.setmode(GPIO.BCM) # GPIO 초기 설정
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)
print("PIR Ready...")
#----------------------------------GPIO---------------------------------

#----------------------------------FLASK--------------------------------
app = Flask(__name__)
species = "None"

@app.route("/")
def hello():
    return render_template("admin.html")

@app.route("/manage")
def manage(): 
    return species # RENEWAL 버튼 클릭 시 return → 종 전달
#----------------------------------FLASK--------------------------------

#----------------------------------PICAMERA-----------------------------
path = '/home/pi/src6/08_project2'

camera = picamera.PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
time.sleep(3)

print("PiCamera Ready...")
#----------------------------------PICAMERA-----------------------------

#----------------------------------CV2DNN-------------------------------
# model, config, classFile 설정
model = './dnn/bvlc_googlenet.caffemodel'
config = './dnn/deploy.prototxt'
classFile = './dnn/classification_classes_ILSVRC2012.txt'

classNames = None
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load a pre-trained neural network
net = cv2.dnn.readNet(model, config)
#----------------------------------CV2DNN-------------------------------

#----------------------------------MAIN---------------------------------
try:
    if __name__ == "__main__":
        app.run(host="0.0.0.0")
    
    while True:
        reading = analog_read(0) # 0번 채널에서 읽어온 SPI 데이터 (수치는 0~1024)

        if reading < 1023: # 조도센서 값이 일정 값 이하일 때 True → 늦은 오후일 때 True / 추후 기입
            pir_val = GPIO.input(PIR_PIN) # PIR 센서 값 read

            if pir_val == GPIO.HIGH: # PIR 센서에 움직임이 감지될 때 True
                camera.capture('%s/animal.jpg' % path) # 사진 촬영

                img = cv2.imread('animal.jpg') # 이미지 파일 읽기

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

                species = classNames[classId] # species 변수에 종 이름 기입

                GPIO.output(LED_PIN, 1) # LED ON → 홈페이지에서 버튼 클릭을 하도록 알림
                cv2.waitKey(0) # 키보드 입력 대기
            time.sleep(0.1)

        GPIO.output(LED_PIN, 0)
        time.sleep(0.01)

finally: #spi, gpio 후처리
    spi.close()
    GPIO.cleanup()
    camera.stop_preview()
#----------------------------------MAIN---------------------------------

