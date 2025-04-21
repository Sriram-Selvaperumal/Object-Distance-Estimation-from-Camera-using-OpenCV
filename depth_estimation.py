import cv2
import numpy as np

def find_focal_length(known_distance, known_width, width_in_rf_image):
    return (width_in_rf_image * known_distance) / known_width

def distance_finder(focal_length, known_width, width_in_frame):
    return (known_width * focal_length) / width_in_frame

KNOWN_DISTANCE = 30.0  
KNOWN_WIDTH = 5.0      

ref_image = cv2.imread("ref_img.png")
hsv_ref = cv2.cvtColor(ref_image, cv2.COLOR_BGR2HSV)

lower_bound = np.array([LH, LS, LV])
upper_bound = np.array([UH, US, UV])
mask = cv2.inRange(hsv_ref, lower_bound, upper_bound)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ref_object_width = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        ref_object_width = w
        break

if ref_object_width == 0:
    print("No reference object found!")
    exit()

focal_length = find_focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_object_width)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)

            distance = distance_finder(focal_length, KNOWN_WIDTH, w)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(frame, "Object Name", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.putText(frame, f"Distance: {round(distance, 2)} cm", (x, y + h + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Distance Measurement", frame)

    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
