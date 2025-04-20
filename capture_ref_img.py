import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cv2.imwrite("ref_img.png", frame)

cap.release()

print("Reference image saved as 'ref_img.png'")
