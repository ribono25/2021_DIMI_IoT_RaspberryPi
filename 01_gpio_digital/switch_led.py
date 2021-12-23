    import RPi.GPIO as GPIO

    RED_LPIN = 26
    RED_SPIN = 24
    YEL_LPIN = 13
    YEL_SPIN = 17
    GRE_LPIN = 5
    GRE_SPIN = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_LPIN, GPIO.OUT)
    GPIO.setup(YEL_LPIN, GPIO.OUT)
    GPIO.setup(GRE_LPIN, GPIO.OUT)
    GPIO.setup(RED_SPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(YEL_SPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(GRE_SPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    try:
        while True:
            val_red = GPIO.input(RED_SPIN) #누르지 않았을 때는 0, 눌렀을 떄는 1
            val_yel = GPIO.input(YEL_SPIN)
            val_gre = GPIO.input(GRE_SPIN)

            
            GPIO.output(RED_LPIN, val_red) #GPIO.HIGH = 1
            GPIO.output(YEL_LPIN, val_yel)
            GPIO.output(GRE_LPIN, val_gre)

    finally:
        GPIO.cleanup()
        print("cleanup and exit")