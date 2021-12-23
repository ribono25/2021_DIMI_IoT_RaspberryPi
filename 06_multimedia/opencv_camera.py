import cv2

cap = cv2.VideoCapture('output.avi') # open camera device

if not cap.isOpened():
    print('Camera open failed')
    exit()

# film a photo
# ret, frame = cap.read() # tuple data (parentheses skip)
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg', frame)

# shift + line you want to delete -> ctrl + slash

# film a video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13:
        break

# release user resource
cap.release()
cv2.destroyAllWindows()