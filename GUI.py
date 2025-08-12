# Importing libraries
import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk

import ingredientdetection

#path wird als globale variable definiert um sie später nutzen zu können
path = None

# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    global path
    path = tk.filedialog.askopenfilename(filetypes=fileTypes) #Zugriff auf das Bild

    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        # re-sizing the app window in order to fit picture
        # and buttom
        app.geometry("560x300")
        label.config(image=pic)
        label.image = pic

    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")



def generaterecipe(path):
    if path:
        antwort= ingredientdetection.start(path)
        label.config(image="",text=antwort)
        label.image = None
    else:
        print("No image uploaded yet!")

# Main method
if __name__ == "__main__":

    # defining tkinter object
    app = tk.Tk()

    # setting title and basic size to our App
    app.title("Ingredients to Recipe")
    app.geometry("560x270")

    # adding background color to our upload button
   # app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "lightblue")

    label = tk.Label(app)
    label.pack(pady=10)

    # defining our upload buttom
    uploadButton = tk.Button(app, text="Generate Recipe", command=lambda: generaterecipe(path))
    uploadButton.pack(side=tk.BOTTOM, pady=10, padx=0)

    # defining our upload buttom
    uploadButton = tk.Button(app, text="Upload Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=0, padx=0)

    app.mainloop() #show window