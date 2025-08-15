# Ingredients to Recipe
## Welcome 
Dieses Projekt ermöglicht es dem Nutzer, ein Foto von zu nutzenden Lebensmittel hochzuladen und sich ein Rezept generieren zu lassen. 
Jeder stand bereits vor der Frage "Was soll ich heute essen? Ich hab Lust auf X, aber was kann ich damit machen?". Hier kann man ganz einfach per Knopfdruck entscheiden lassen.
Es bietet Abwechslung für die eigene Ernährung. Ein weiterer Mehrwert dieser Funktion liegt darin, Reste verwerten zu können, indem man sich dafür ein Rezept generieren lässt.

:exclamation: Aktuell erkennt das Modell folgende Zutaten: 
 Paprika, Butter, Karrotte, Blumenkohl, Käse, Hähnchen, Chilli, Ei, Knoblauch, Schinken/Wurstaufstrich, Fleisch, Milch, Pilze, Oliven, Zwiebel, Pasta, Erbsen, Kartoffel, Reis, Tomate, Zucchini

Das Projekt basiert auf der Objekterkennung mithilfe des YOLOv8 Modells von ultralytics, das die Zutaten auf dem Foto identifiziert
und einem lokalen LLM von Ollama, das anschließend das Rezept generiert.

## Nutzungsanleitung 
### 1.Vorbereitung 
1.1. Ollama [hier](https://ollama.com/) installieren .exe auführen und zu PATH hinzufügen, um in cmd "ollama run llama2" auszuführen

1.2. Repository klonen und Requirements mittels "pip install -r requirements.txt" herunterladen.

1.3. Beispielfoto nutzen oder eigenes Foto machen 
### 2. Ausführung
GUI.py ausführen,
Foto auswählen ("Upload Image"),
Rezept generieren ("Generate Recipe")

Die Generierung des Rezeptes dauert einen Moment. 


### 3. Zur Erweiterung des Modelltrainings: 
Die Daten wurden in Roboflow vorbereitet und sind unter ... zu finden. 
Um den Downloadcode nutzen zu können, ist ein eigener Account in Roboflow notwendig, um den API-Key zu entnehmen. 
## Projektstruktur

**GUI.py**: startet den workflow, der Nutzer wird durch eine GUI angeleitet <br>
**ingredientdetection.py**: führt Erkennung der Zutaten durch und leitet diese an das localLLM weiter <br>
**localLLM**: gibt prompt in LLM und generiert Antwort <br>
**trainmodel.py**: hier wurde zuvor das Modell trainiert; NICHT ZUR EIGENTLICHEN AUSFÜHRUNG NÖTIG <br>
<br>
**runs**: hier findet man alle Trainingsdurchläufe zu Dokumentationszwecken:  <br>
- runs/detect/train2 - Training mit ca.3000 Bildern und 5 Epochs
- runs/detect/train3 - Training mit ca.3100 Bildern (um wenige 100 erweitert, die näher am Anwendungsfall sind) und 5 Epochs
- runs/detect/train4 - Training mit ca.5500 Bildern (erweitert mit Augmentation) und 10 Epochs
- runs/detect/train10 - Training mit ca.5500 Bildern und 22 Epoch (abgebrochen)
- runs/detect/train11 - Training mit ca.5500 Bildern und 50 Epochs (über GPU in Google Collab)
<br><br>
- runs/detect/val val2 - zur Generierung der Metriken aus train10
- runs/detect/val3 - Metriken basierend auf Testdaten Modell aus train 10
- runs/detect/val4 - Metriken basierend auf Testdaten Modell aus train 11
- runs/detect/predict - Erkennung auf den Testdaten mit Boundingboxes mit Modell aus train 10 
- runs/detect/predict2 - Erkennung auf den Testdaten mit Boundingboxes mit Modell aus train 11
<br>
beispiel_.jpg: Beispielfoto <br>
.gitignore: enthält Dateien, die in Git zu ignorieren sind <br>
requirements.txt: enthält nötige packages <br>
README.md: Dokumentation <br>

## Weiteres 
Die Datengrundlage muss noch mit mehr Anwendungsnahen Beispielen erweitert werden.
## Lizenz 