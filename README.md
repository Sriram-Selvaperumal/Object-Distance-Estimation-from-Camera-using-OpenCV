# 📏 Object Distance Estimation using OpenCV

Estimate the **real-time distance** of an object from your webcam using computer vision techniques. This project uses color detection and basic geometry to determine how far an object is from the camera.

---

## ✨ Features

- Real-time object detection using color (HSV filtering).
- Calculates and displays the distance of the object from the camera.
- Green bounding box with **object name** and **distance**.
- Adjustable HSV threshold for different colored objects.
- Beginner-friendly code structure.

---

Steps involved:
- Capture a reference image at a known distance.
- Detect the object using its color (HSV range).
- Calculate focal length from reference image.
- Estimate distance from current frame using object width.

---

## 📁 Project Files

| File Name             | Description                                       |
|----------------------|---------------------------------------------------|
| `capture_ref_img.py` | Captures a reference image of the object.         |
| `hsv_calculator.py`  | Helps you find HSV range of the object to detect. |
| `depth_estimation.py`| Main script to calculate and show object distance.|
| `ref_img.png`        | Reference image captured by user.                 |


---

## ⚙️ Requirements

Install dependencies using pip:

```bash
pip install opencv-python numpy

