import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
# Import the necessary patch for displaying images in Colab


# Load YOLOv8 model (pre-trained on COCO dataset)
model = YOLO("yolov8n.pt")

# Open traffic video
video_path = r"D:\smart_traffic\vids\traffic_video (2).mp4"  # Replace with your video file
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize vehicle count storage
vehicle_counts = []
frame_times = []

frame_count = 0

# Define vehicle class IDs (COCO dataset)
vehicle_classes = [2, 3, 5, 7]  # Car, Truck, Bus, Motorcycle

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Run YOLO detection
    results = model(frame)

    # Count vehicles in the frame
    vehicle_count = sum(1 for obj in results[0].boxes.data if int(obj[-1]) in vehicle_classes)
    vehicle_counts.append(vehicle_count)

    # Calculate time in seconds
    frame_times.append(frame_count / fps)

    # Annotate frame with detected objects
    annotated_frame = results[0].plot()

    # Show the annotated video using cv2_imshow instead of cv2.imshow
    cv2.imshow(annotated_frame)

    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to stop
        break

cap.release()
cv2.destroyAllWindows()

# Save vehicle count data as CSV
df = pd.DataFrame({"Time (s)": frame_times, "Vehicle Count": vehicle_counts})
df.to_csv("vehicle_counts.csv", index=False)

print("✅ Vehicle count data saved as 'vehicle_counts.csv'!")