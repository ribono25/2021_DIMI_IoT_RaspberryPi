from flask import Flask, render_template
import RPi.GPIO as GPIO

RLED_PIN = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(RLED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(RLED_PIN, GPIO.LOW)
        return "LED OFF"
    else:
        return "Error"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()