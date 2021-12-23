import cv2

# read image file
img = cv2.imread('fox.jpg')
img2 = cv2.resize(img, (600, 400))

cv2.imshow('fox_org', img)
cv2.imshow('fox', img2)

# wait keyboard input (millisecond)
# if first value is 0, it waits until keyboard receives input
cv2.waitKey(0)

# close all windows
cv2.destroyAllWindows()