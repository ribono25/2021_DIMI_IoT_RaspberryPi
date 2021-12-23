import cv2

cap = cv2.VideoCapture(0) # open camera device

if not cap.isOpened():
    print('Camera open failed')
    exit()

# film a video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 50, 100)

    cv2.imshow('frame', frame)
    cv2.imshow('frame_gray', gray)
    cv2.imshow('frame_edge', edge)

    if cv2.waitKey(10) == 13:
        break

# release user resource
cap.release()
cv2.destroyAllWindows()