import cv2
import numpy as np
from ultralytics import YOLO

# -----------------------------
# CONFIGURATION
# -----------------------------
VIDEO_SOURCE =  0 #"traffic.mp4"   # use 0 for webcam
CONF_THRESHOLD = 0.4

# COCO vehicle class IDs
# car=2, motorcycle=3, bus=5, truck=7
VEHICLE_CLASSES = [2, 3, 5, 7]

# Traffic timing (seconds)
LOW_DENSITY_TIME = 10

MEDIUM_DENSITY_TIME = 20
HIGH_DENSITY_TIME = 30

# -----------------------------
# LOAD MODEL
# -----------------------------
model = YOLO("yolo11n.pt")

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def get_green_time(vehicle_count):
    """
    Decide green signal duration based on density
    """
    if vehicle_count < 5:
        return LOW_DENSITY_TIME
    elif vehicle_count < 10:
        return MEDIUM_DENSITY_TIME
    else:
        return HIGH_DENSITY_TIME


def draw_lane_lines(frame, width, height):
    """
    Draw lane division line
    """
    cv2.line(frame, (width // 2, 0), (width // 2, height), (255, 255, 255), 2)


# -----------------------------
# VIDEO CAPTURE
# -----------------------------
cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    print("❌ Error: Cannot open video source")
    exit()

print("✅ Traffic Density Control System Started")

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    # Lane counters
    lane_1_count = 0
    lane_2_count = 0

    # YOLO inference
    results = model(frame, conf=CONF_THRESHOLD, verbose=False)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls in VEHICLE_CLASSES:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = (x1 + x2) // 2

                # Assign lane based on center x
                if cx < width // 2:
                    lane_1_count += 1
                    color = (0, 255, 0)
                else:
                    lane_2_count += 1
                    color = (0, 0, 255)

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # Decide traffic signal
    if lane_1_count > lane_2_count:
        green_lane = "LANE 1"
        green_time = get_green_time(lane_1_count)
    else:
        green_lane = "LANE 2"
        green_time = get_green_time(lane_2_count)


    draw_lane_lines(frame, width, height)

    # Lane counts
    cv2.putText(frame, f"Lane 1 Vehicles: {lane_1_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.putText(frame, f"Lane 2 Vehicles: {lane_2_count}",
                (width // 2 + 20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


    cv2.putText(frame, f"GREEN: {green_lane}",
                (20, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3)

    cv2.putText(frame, f"Green Time: {green_time} sec",
                (20, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

 
    cv2.imshow("Smart Traffic Density Control (YOLO v11)", frame)

    # ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("🛑 System Stopped")
