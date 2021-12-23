import cv2

# read image file
img = cv2.imread('fox.jpg')
img2 = cv2.resize(img, (600, 400))

# imshow(Window name, Video data gonna print)
cv2.imshow('FOX', img)

# Edge line extract
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

# wait keyboard input (millisecond)
# if first value is 0, it waits until keyboard receives input
while True:
    if cv2.waitKey(0) == 13:
        break

# close all windows
cv2.destroyAllWindows()