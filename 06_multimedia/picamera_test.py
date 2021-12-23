import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()

    time.sleep(3)

    while True :
        print('photo:1 video:2 exit:9 > ')
        a = input()

        now_str=time.strftime("%Y%m%d_%H%M%S")

        if a == 1:
            print('photo filming')
            camera.capture('%s/photo_%s.jpg' % (path, now_str))
        elif a == 2:
            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            print('press enter to stop recording..')
            print('video filming')
            input()
            camera.stop_recording()
        elif a == 9:
            break
        else :
            print('incorrect command')
    
finally:
    camera.stop_preview()