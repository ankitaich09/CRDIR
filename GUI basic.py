#CRDIR
#Author - Ankit Aich


#Update 28th May - Basic window with combobox for choosing all files and a button to show them in a window
#Update 3rd June - The combobox now has only nef files using a standard cleaning technique, there is also another combobox which lets the user choose a commonly used format (jpeg, png, or tiff) and another button to save it to a new folder, another button added to view histogram of selected image



from tkinter import *
from tkinter.ttk import *
import os
import rawpy
import matplotlib.pyplot as plt


def show(name):

    imgName = imagePath + name
    img = rawpy.imread(imgName)
    rgb = img.postprocess()
    plt.imshow(rgb)


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def hist(name):
    imgName = imagePath + name
    img = rawpy.imread(imgName)
    rgb = img.postprocess()
    gray = rgb2gray(rgb)
    plt.hist(gray)#.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')


def histogramView():
    nm = comboExample.get()
    hist(nm)


def callbackFunc():
    nm = comboExample.get()
    show(nm)


def callbackConv():
    name = comboExample.get()
    imgName = imagePath + name
    img = rawpy.imread(imgName)
    rgb = img.postprocess()
    n = str(name)
    first, ext = n.split('.')
    exten = '.' + comboChoices.get()
    convert(rgb, first, exten)


def convert(image, name, extension):
    newName = name+extension
    path = newPath + newName
    plt.imsave(path, image)


def clear(listofThings):
    newList = []
    for each_item in listofThings:
        if(not('nef' in each_item)):
            pass
        else:
            newList.append(each_item)
    return newList


imagePath = "/Users/ankit/Documents/CRDIR Expedition 31 Single Camera/"
#path to read images
listofThings = os.listdir(imagePath)
listofImages = clear(listofThings)
newPath = "/Users/ankit/Documents/CRDIR Expedition 31 Single Camera/Converted Images/"
#path to store converted images
app = Tk()
app.geometry('1000x1000')
app.title('Choose an image')
labelTop = Label(app,text="Choose a picture")
labelTop.grid(column=0, row=0)
comboExample = Combobox(app, values=listofImages)
comboExample.grid(column=0, row=3)
comboExample.current(1)
#list of nef files
comboChoices = Combobox(app, values=['jpeg', 'png', 'tiff'])
comboChoices.grid(column=5, row=3)
comboChoices.current(1)
#list of image converting formats
b = Button(app, text="show", command=callbackFunc)
b.grid(column=0, row=5)
#button to show image
b1 = Button(app, text="convert", command=callbackConv)
b1.grid(column=5, row=5)
#button to convert image
b2 = Button(app, text="plot Histogram", command=histogramView)
b2.grid(column=3, row=10)
#button to plot histogram
app.mainloop()