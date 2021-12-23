import cv2

# read image file
img = cv2.imread('fox.jpg')
img2 = cv2.resize(img, (600, 400))

# change color
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# open image file
cv2.imshow('fox', img2)
cv2.imshow('fox_gray', gray)

# wait keyboard input (millisecond)
# if first value is 0, it waits until keyboard receives input
cv2.waitKey(0)

# save as a file
cv2.imwrite('fox_gray.jpg', gray);

# close all windows
cv2.destroyAllWindows()