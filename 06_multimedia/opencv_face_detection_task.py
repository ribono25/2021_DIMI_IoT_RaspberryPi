import cv2

cap = cv2.VideoCapture(0) # open camera device
face_cascade = cv2.CascadeClassifier('./XML/face.xml')

if not cap.isOpened():
    print('Camera open failed')
    exit()  

# film a video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13:
        break

# release user resource
cap.release()
cv2.destroyAllWindows()