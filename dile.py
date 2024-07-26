import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Mercury", (100, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Venus", (200, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Earth", (300, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Mars", (400, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Jupiter", (550, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Saturn", (750, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Uranus", (950, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Neptune", (1100, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow("output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_system_with_names.jpg", img)
