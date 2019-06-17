#Update 11Th June, because I figured out to do better stuff with lesser code

import rawpy
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import time
import fullimageshow as fis


def openAndSavePic():
    rgb = callOpener()
    plt.imshow(rgb)


def scale():
    w = window.winfo_screenheight()
    h = window.winfo_screenwidth()
    rgb = callOpener()
    fis.imshow(rgb, h, w)


def rgb2gray(rgbIm):
    r, g, b = rgbIm[:, :, 0], rgbIm[:, :, 1], rgbIm[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def hist():
    rgb = callOpener()
    gray = rgb2gray(rgb)
    tstart = time.time()
    plt.hist(gray, histtype= 'step')
    tend = time.time()
    taken = (tend-tstart)/60
    messagebox.showinfo("Timer", message=taken)


def callOpener():
    imageName = filedialog.askopenfilename()
    fname, exten = str(imageName).split('.')
    if not (exten == "nef"):
        messagebox.showerror("Wrong Extension", "Please choose a nef rawfile")
    img = rawpy.imread(imageName)
    rgbImage = img.postprocess()
    return rgbImage




window = Tk()
window.geometry('300x300')
window.title('CRDIR')
openButton = Button(window, text='Choose a pic', command=openAndSavePic)
openButton.grid(column=2, row=2)
histogramButton = Button(window, text='Plot a histogram', command=hist)
histogramButton.grid(column=2, row=4)
scaleButton = Button(window, text='scale an image to fullscreen', command=scale)
scaleButton.grid(column=2, row=6)
window.mainloop()

