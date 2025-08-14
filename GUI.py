import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk

import ingredientdetection

#path wird als globale variable definiert um sie später nutzen zu können
path = None

# Bild hochladen
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    global path
    path = tk.filedialog.askopenfilename(filetypes=fileTypes) #Zugriff auf das Bild

    # Bild ausgewählt
    if len(path):
        img = Image.open(path)
        img = img.resize((300, 300)) #Bildgröße fürs Fenster anpassen
        pic = ImageTk.PhotoImage(img) #umwandeln in Tkinter Bildobjekt

        #Bild in Fenster anzeigen
        label.config(image=pic)
        label.image = pic

    # falls kein Bild ausgewählt wurde
    else:
        print(" Please choose a file.")


 #globale Variable path nutzen, um Bild hier erneut aufzurufen
def generaterecipe(path):
    if path:
        antwort= ingredientdetection.start(path) #ingredient detection durchführen
        label.config(image="",text=antwort) #Antwort anzeigen lassen
        label.image = None
    else:
        print("Please choose a file.")

# Main method
if __name__ == "__main__":

    # tkinter object
    app = tk.Tk()

    # Fenster configs: titel, größe, button farbe
    app.title("Ingredients to Recipe")
    app.geometry("900x500")
    app.option_add("*Button*Background", "lightblue")

    #Platzhalter für Bild und Text setzen
    label = tk.Label(app)
    label.pack(pady=10)

    # upload button
    uploadButton = tk.Button(app, text="Generate Recipe", command=lambda: generaterecipe(path))
    uploadButton.pack(side=tk.BOTTOM, pady=10, padx=0)

    # generate button
    uploadButton = tk.Button(app, text="Upload Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=0, padx=0)

    app.mainloop() #Fenster anzeigen