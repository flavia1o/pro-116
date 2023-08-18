import cv2


img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Terra", (285, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Marte", (370, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
cv2.putText(img, "Mercurio", (119, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "venus", (190, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
cv2.putText(img, "Jupiter", (450, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
cv2.putText(img, "Saturno", (675, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
cv2.putText(img, "Uranos", (950, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
cv2.putText(img, "Netuno", (1100, 145), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

cv2.imshow("resultado", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.destroyAllWindows()