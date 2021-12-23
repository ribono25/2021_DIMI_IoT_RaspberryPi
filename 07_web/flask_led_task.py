# same with flask_led.py

from flask import Flask
import RPi.GPIO as GPIO

RLED_PIN = 22
BLED_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED_PIN, GPIO.OUT)
GPIO.setup(BLED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return ''' 
        <p>Hello, Flask!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF<br></a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_onoff(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(RLED_PIN, GPIO.HIGH)
            return '''
                <p>RED LED ON</p>
                <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(RLED_PIN, GPIO.LOW)
            return '''
                <p>RED LED OFF</p>
                <a href="/">Go Home</a>
            '''

    elif color == "blue":
        if op == "on":
            GPIO.output(BLED_PIN, GPIO.HIGH)
            return '''
                <p>BLUE LED ON</p>
                <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(BLED_PIN, GPIO.LOW)
            return '''
                <p>BLUE LED OFF</p>
                <a href="/">Go Home</a>
            '''


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()