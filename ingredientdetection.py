import cv2
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt

import localLLM

def start(path):
 #eigenes trainiertes Modell (von trainmodel.py) laden
 model= YOLO('runs/detect/train4/weights/best.pt')

 #dein Bild laden
 image = cv2.imread(path)

 # Bild auf 416x416 Pixel skalieren
 image = cv2.resize(image, (416, 416))

 # Vorhersage machen
 prediction = model.predict(image)
 print(prediction)

#zur Visualisierung der erkannten zutaten
 result = prediction[0].plot()  # gibt ein NumPy-Bild zurück
 plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
 plt.axis('off')
 plt.title('Erkannte Zutaten')
 plt.show()

 #klasse ausgeben, die in cls im tensor format vorliegt,dann in integer liste konvertieren
 ingredientlist = prediction[0].boxes.cls.int().tolist()

 #danach integer liste auf Worte (klassennamen) mappen, um im llm verwenden zu können
 classnames = prediction[0].names
 convertclass = list({classnames[i] for i in ingredientlist})
 print('The ingredients are:', convertclass)

#liste für prompt anpassen
 ingredient_list=",".join(convertclass)
 prompt="Give me a recipe with the following ingredients:"+ingredient_list+"\n"
 antwort = localLLM.ollama_chat(prompt) #prompt in LLM geben
 print(antwort) #antwort auf konsole
 return antwort #antwort im fenster

#start generating workflow
