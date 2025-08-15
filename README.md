# Ingredients to Recipe 

here you'll find:
- project description (welcome)
- Instructions for setup, execution and further training 
- project structure 
- additional information

## Welcome 
This project allows users to upload a photo of ingredients they want to use and generate a recipe from them.  
Everyone has probably faced the question: "What should I eat today? I feel like X, but what can I make with it?" With this project, you can easily get an answer.  

It provides variety for your meals and another benefit of this feature is that it helps reduce food waste by generating recipes for leftover ingredients.  

:exclamation: Currently, the model recognizes the following ingredients:  
Bell pepper, butter, carrot, cauliflower, cheese, chicken, chili, egg, garlic, ham, meat, milk, mushrooms, olives, onion, pasta, peas, potato, rice, tomato, zucchini  

The project is based on object detection using the YOLOv8 model from Ultralytics, which identifies the ingredients in the photo, and a local LLM from Ollama, which generates the recipe.

## Instructions 

### 1. Setup 
1.1. Install Ollama [here](https://ollama.com/), run the .exe, and add it to your PATH to be able to run `ollama run llama2` in the command line.  
```
ollama run llama2
```

1.2. Clone this repository, create a virtual environment and install the requirements using:  
```
pip install -r requirements.txt
```
1.3. This repository uses tkinter for the GUI. On Windows and macOS it is already included in python. On Linux it may be required to install it separately. <br>
- Ubuntu/Debian
````
sudo apt install python3-tk
````

- Fedora

````
sudo dnf install python3-tkinter
````

- Arch Linux
````
sudo pacman -S tk
````

### 2. Execution

- Run GUI.py,
- Select a photo ("Upload Image") - Use the example photo or take your own photo,
- Generate the recipe ("Generate Recipe").

The recipe generation may take a moment.

### 3. To Extend Model Training

The data has been prepared in Roboflow and can be found [here](https://universe.roboflow.com/mymlproject-j4uiu/ingredients-2-nct08/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true).
To use the download code, a personal Roboflow account is required to obtain an API key.

## Project Structure

**GUI.py**: starts the workflow, guiding the user through a GUI <br>
**ingredientdetection.py**: performs ingredient detection and passes the data to the local LLM <br>
**localLLM**: sends the prompt to the LLM and generates the response <br>
**trainmodel.py**: previously used to train the model; NOT NEEDED FOR NORMAL EXECUTION <br>
<br>
**runs**: contains all training runs for documentation purposes: <br>

- runs/detect/train2 - training with ~3000 images and 5 epochs

- runs/detect/train3 - training with ~3100 images (slightly expanded with data closer to the use case) and 5 epochs

- runs/detect/train4 - training with ~5500 images (augmented) and 10 epochs

- runs/detect/train10 - training with ~5500 images and 22 epochs (stopped early)

- runs/detect/train11 - training with ~5500 images and 50 epochs (using GPU in Google Colab)
<br><br>

- runs/detect/val val2 - metrics generated from train10

- runs/detect/val3 - metrics based on test data from train10

- runs/detect/val4 - metrics based on test data from train11

- runs/detect/predict - detection on test data with bounding boxes using the model from train10

- runs/detect/predict2 - detection on test data with bounding boxes using the model from train11

<br>

**beispiel_.jpg**: example photo <br>
**.gitignore**: files to be ignored by Git <br>
**requirements.txt**: required packages <br>
**README.md**: documentation <br>

## Additional Notes

The dataset still needs to be expanded with more use-case relevant examples.

## License