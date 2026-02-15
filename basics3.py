import cv2

image1= cv2.imread('OpenCV/supermanman.webp')
cv2.imshow('batman', image1)
cv2.waitKey(0)
print(image1)

image2= cv2.imread('OpenCV/superwoman2.webp')
cv2.imshow('batman', image2)
cv2.waitKey(0)
print(image2)

image3= cv2.resize(image2, (270, 338))
addition= cv2.addWeighted(image1, 0.5, image3, 0.5, 0)
cv2.imshow('added', addition)
cv2.waitKey(0)