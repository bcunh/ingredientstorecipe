import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk

import ingredientdetection

#path is defined as a global variable in order to use it later
path = None

# Upload Image
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    global path
    path = tk.filedialog.askopenfilename(filetypes=fileTypes) #Access to image

    # image selected
    if len(path):
        img = Image.open(path)
        img = img.resize((300, 300)) #adjust image to fit window size
        pic = ImageTk.PhotoImage(img) #convert to Tkinter image object

        #show image in window
        label.config(image=pic)
        label.image = pic

    # error message if no image was selected
    else:
        message="please select an image file"
        label.config(image="", text=message, anchor="center")
        print(message)


 #use global variable path to access image again
def generaterecipe(path):
    if path:
        label.config(image="", text="Loading...")  # show loading message
        label.image = None
        antwort= ingredientdetection.start(path) #execute ingredient detection
        label.config(image="",text=antwort) #show answer in window
        label.image = None
    else:
        message = "Error:no image file selected"
        label.config(image="", text=message, anchor="center")
        print(message)

# Main method
if __name__ == "__main__":

    # tkinter object
    app = tk.Tk()

    # window configs: title, size, button color
    app.title("Ingredients to Recipe")
    app.geometry("900x500")
    app.option_add("*Button*Background", "lightblue")

    #set placeholder for image and text
    label = tk.Label(app)
    label.pack(expand=True, fill="both") #Label zentrieren

    # upload button
    uploadButton = tk.Button(app, text="Generate Recipe", command=lambda: generaterecipe(path))
    uploadButton.pack(side=tk.BOTTOM, pady=10, padx=0)

    # generate button
    uploadButton = tk.Button(app, text="Upload Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=0, padx=0)

    app.mainloop() #show window