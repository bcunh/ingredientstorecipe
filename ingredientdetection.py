import cv2
from ultralytics import YOLO
#import matplotlib.pyplot as plt

import localLLM

def start(path):
 #load own trained model (trained in trainmodel.py, saved under runs)
 model= YOLO('runs/detect/train11/weights/best.pt')

 #load image for recognition
 image = cv2.imread(path)

 # scale image to 416x416 pixels
 image = cv2.resize(image, (416, 416))

 # make prediction
 prediction = model.predict(image)
 print(prediction)

#DEBUG: important for visualization of the detected ingredients
# result = prediction[0].plot()  # gibt ein NumPy-Bild zurück
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.title('Erkannte Zutaten')
# plt.show()

 #output class, that is in .cls in tensor format, then convert to integer list
 ingredientlist = prediction[0].boxes.cls.int().tolist()

 #mapping of integer liste to words (classnames), to use it in llm natural language prompt
 classnames = prediction[0].names
 convertclass = list({classnames[i] for i in ingredientlist})
 print('The ingredients are:', convertclass)

#adjust list for prompt (comma)
 ingredient_list=",".join(convertclass)
 prompt="Give me a recipe with the following ingredients:"+ingredient_list+"\n"
 antwort = localLLM.ollama_chat(prompt) #pass propmt to localLLM
 #print(antwort) #Answer on console
 return antwort #answer in window

#start workflow
