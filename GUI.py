#Update 11Th June, because I figured out to do better stuff with lesser code

import rawpy
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import cv2
from PIL import ImageTk, Image
import numpy as np

listOfImages = []


def openAndSavePic():
    if not listOfImages:
        messagebox.showerror("image not found", "Please choose an image first before continuing")
    rgb = listOfImages[0]
    plt.imshow(rgb)


def scale():
    if not listOfImages:
        messagebox.showerror("image not found", "Please choose an image first before continuing")
    rgb = listOfImages[0]
    cv2.imshow('1:1', rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rgb2gray(rgbIm):
    r, g, b = rgbIm[:, :, 0], rgbIm[:, :, 1], rgbIm[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def callOpener():
    if not listOfImages:
        imageName = filedialog.askopenfilename()
        fname, exten = str(imageName).split('.')
        if not (exten == "nef"):
            messagebox.showerror("Wrong Extension", "Please choose a nef rawfile")
        img = rawpy.imread(imageName)
        rgbImage = img.postprocess()
        listOfImages.append(rgbImage)
        listOfImages.append(img)
        listOfImages.append(fname)
        displayImage = listOfImages[0]
        displayImage = Image.fromarray(displayImage)
        displayImage = displayImage.resize((400,400))
        displayImage = ImageTk.PhotoImage(displayImage)
        panel = Label(window, image=displayImage)
        panel.image = displayImage
        panel.grid(column=100, row=20)
        text = Label(window, text='Loaded Image')
        text.grid(column=100, row=18)
    else:
        messagebox.showinfo('Message', 'Still working on program restarts')

def hist():
    if not listOfImages:
        messagebox.showerror("image not found", "Please choose an image first before continuing")
    rgbImg = listOfImages[0]
    redHist = cv2.calcHist(rgbImg, [2], None, [256], [0, 256])
    greenHist = cv2.calcHist(rgbImg, [1], None, [256], [0, 256])
    blueHist = cv2.calcHist(rgbImg, [0], None, [256], [0, 256])
    plt.figure()
    plt.plot(redHist)
    plt.title('Red Channel Histogram')
    plt.show()
    plt.figure()
    plt.plot(greenHist)
    plt.title('Green Channel Histogram')
    plt.show()
    plt.figure()
    plt.plot(blueHist)
    plt.title('Blue Channel Histogram')
    plt.show()


def generateBayer():
    if not listOfImages:
        messagebox.showerror("image not found", "Please choose an image first before continuing")
    rawImage = listOfImages[1]
    BayerFilter = rawImage.raw_image
    name = listOfImages[2]
    name = str(name)
    name = name[name.rfind('/')+1:]
    fname = '/Users/ankit/Documents/CRDIR Expedition 31 Single Camera/Bayer/'+'BayerFilter for' + name + '.csv'
    np.savetxt(fname, BayerFilter, delimiter=',')
    bayerMessage = 'Bayer Filter matrix available in' + fname
    messagebox.showinfo('File information', bayerMessage)
    plt.imshow(BayerFilter)
    plt.title('Raw Bayer Filter Image')

window = Tk()
window.geometry('650x600')
window.title('CRDIR')
impath = '/Users/ankit/Documents/CRDIR Expedition 31 Single Camera/iss031e011460.nef'
text = Label(window, text='Welcome to CRDIR')
text.grid(column=10, row=0)
openButton = Button(window, text='Show Image', command=openAndSavePic)
openButton.grid(column=10, row=12)
histogramButton = Button(window, text='Plot a histogram', command=hist)
histogramButton.grid(column=10, row=14)
scaleButton = Button(window, text='scale an image to 1:1', command=scale)
scaleButton.grid(column=10, row=16)
bayerButton = Button(window, text='Generate Bayer Filter for matrix', command=generateBayer)
bayerButton.grid(column=10, row=18)
loadButton = Button(window, text='load an image', command=callOpener)
loadButton.grid(column=10, row=10)
window.mainloop()

