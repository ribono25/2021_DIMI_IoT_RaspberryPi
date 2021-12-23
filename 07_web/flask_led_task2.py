from flask import Flask, render_template
import RPi.GPIO as GPIO

RLED_PIN = 13
BLED_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED_PIN, GPIO.OUT)
GPIO.setup(BLED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led_task.html")

@app.route("/led/<color>/<op>")
def led_onoff(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(RLED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif op == "off":
            GPIO.output(RLED_PIN, GPIO.LOW)
            return "RED LED OFF"

    elif color == "blue":
        if op == "on":
            GPIO.output(BLED_PIN, GPIO.HIGH)
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(BLED_PIN, GPIO.LOW)
            return "BLUE LED OFF"
    else:
        return "Error"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()