import cv2
img = cv2.imread('assets/img1.jpg', -1)
img = cv2.resize(img, (0,0), fx = 0.2, fy = 0.2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
