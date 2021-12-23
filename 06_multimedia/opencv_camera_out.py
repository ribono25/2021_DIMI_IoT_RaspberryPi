import cv2

cap = cv2.VideoCapture(0) # open camera device

if not cap.isOpened():
    print('Camera open failed')
    exit()

# comment process key -> ctrl + slash

fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D', 'I', 'V', 'X') is permitted 
# fourcc : four character code
# DIVX(avi), MP4V(mp4), X264(h264)

# make VideoWriter object to save video
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))
#('name', fourcc, fps, frame size)

# film a video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)
    
    if cv2.waitKey(10) == 13:
        break

# release user resource
cap.release()
out.release()
cv2.destroyAllWindows()