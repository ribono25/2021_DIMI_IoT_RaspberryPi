from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 13

now = datetime.datetime.now()
display = drivers.Lcd()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        display.lcd_display_string(f"{temperature:.1f}C, {humidity:.1f}%", 2)
        time.sleep(0.1)
finally:
    print("cleaning up!")
    display.lcd_clear()