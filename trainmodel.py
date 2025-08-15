from ultralytics import YOLO
from roboflow import Roboflow
import os


#download dataset from Roboflow
rf = Roboflow(api_key="") #get your own api-key via your roboflow account
project = rf.workspace("mymlproject-j4uiu").project("ingredients-2-nct08")
version = project.version(2)
dataset = version.download("yolov8-obb")
data_path = os.path.join(dataset.location, "data.yaml")

# load YOLOv8n model
model = YOLO("yolov8n.pt")

# actual training
#default with batchsize=16, Optimizer=AdamW
results = model.train(data=data_path, epochs=50, patience=30)

#evaluate model
model= YOLO('runs/detect/train12/weights/best.pt')

#metrics = model.val() #evaluation on the same data that was used for training
#print(metrics)

metrics = model.val(
    data=data_path,
    split="test"        #evaluation on test data
)

test_path=os.path.join(dataset.location, "test", "images")
# Batch-Testing -  perform visual recognition (to be found under runs/detect/predict)
results = model.predict(
    source=test_path,
    save=True,       # save images with Bounding Boxes
    conf=0.5,        # confidence above 50%
    batch=16
)