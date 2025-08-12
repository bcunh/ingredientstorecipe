from ultralytics import YOLO


# Load a YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model on the dataset for 10 epochs
results = model.train(data="dataset/data.yaml", epochs=10)

