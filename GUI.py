#Update 11Th June, because I figured out to do better stuff with lesser code

import rawpy
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


def openAndSavePic():
    imageName = filedialog.askopenfilename()
    _, exten = str(imageName).split('.')
    if not(exten == "nef"):
        messagebox.showerror("Wrong Extension", "Please choose a nef rawfile")
    img = rawpy.imread(imageName)
    rgbImage = img.postprocess()
    plt.imshow(rgbImage)


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def hist():
    imageName = filedialog.askopenfilename()
    img = rawpy.imread(imageName)
    _, exten = str(imageName).split('.')
    if not (exten == "nef"):
        messagebox.showerror("Wrong Extension", "Please choose a nef rawfile")
    rgbImage = img.postprocess()
    gray = rgb2gray(rgbImage)
    plt.hist(gray)


window = Tk()
window.geometry('300x300')
window.title('CRDIR')
openButton = Button(window, text='Choose a pic', command=openAndSavePic)
openButton.grid(column=2, row=2)
histogramButton = Button(window, text='Plot a histogram', command=hist)
histogramButton.grid(column=2, row=4)
window.mainloop()
