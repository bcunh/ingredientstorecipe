from ultralytics import YOLO
from roboflow import Roboflow
import os


#Dataset von Roboflow herunterladen
rf = Roboflow(api_key="")
project = rf.workspace("mymlproject-j4uiu").project("ingredients-2-nct08")
version = project.version(2)
dataset = version.download("yolov8-obb")
data_path = os.path.join(dataset.location, "data.yaml")

# YOLOv8n model laden
model = YOLO("yolov8n.pt")

# Trainieren
#Standard mit batchsize=16, Optimizer=AdamW
results = model.train(data=data_path, epochs=50, patience=30)

#Modell bewerten
model= YOLO('runs/detect/train11/weights/best.pt')

#metrics = model.val() #Bewertung auf denselben Daten, die beim Training verwendet wurden
#print(metrics)

metrics = model.val(
    data=data_path,
    split="test"               # auf testdaten bewerten
)

test_path=os.path.join(dataset.location, "test", "images")
# Batch-Testing -  visuell erkennung durchführen (zu finden unter runs/detect/predict)
results = model.predict(
    source=test_path,
    save=True,       # speichert Bilder mit Bounding Boxes
    conf=0.5,        # Mindest-Confidence
    batch=16
)