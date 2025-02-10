import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Path to input video
video_path = r'D:\smart_traffic\20250209_163940.mp4'
output_video_path = r'D:\smart_traffic\output_detected.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0  # Track processed frames

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection on the frame
    results = model(frame)

    # Convert results to a pandas dataframe
    df = results.pandas().xyxy[0]  # Bounding box coordinates

    vehicle_count = len(df)  # Count detected vehicles
    print(f"Frame {frame_count}: Vehicle count = {vehicle_count}")

    # Draw bounding boxes and labels
    for _, row in df.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = f"{results.names[int(row['class'])]} {row['confidence']:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display vehicle count
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Write processed frame to the output video
    out.write(frame)

    frame_count += 1  # Increment frame counter

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {output_video_path}")
