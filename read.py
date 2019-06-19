import rawpy as rp
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def savefile(array, name):
    fname = '/Users/ankit/Documents/CRDIR Expedition 31 Single Camera/Bayer/'+'BayerFilter for' + name + '.csv'
    np.savetxt(fname, array, delimiter=',')


def imtoBayerFile(path, options=1):
    # 1 - show red Img
    # 2 - show blue Img
    # 3 - show green Img
    # 4 - save bayer Filter into a csv file
    filename = path[path.rfind('/')+1:]
    name,ext = filename.split('.')
    rawImg = rp.imread(path)
    rgbImg = rawImg.postprocess()
    pilImg = Image.fromarray(rgbImg)
    redImg = pilImg.getchannel('R')
    greenImg = pilImg.getchannel('G')
    blueImg = pilImg.getchannel('B')
    redArray = np.array(redImg)
    greenArray = np.array(greenImg)
    blueArray = np.array(blueImg)
    bayerFilter = rawImg.raw_image
    if options == 1:
        plt.imshow(redArray)
    elif options == 2:
        plt.imshow(greenArray)
    elif options == 3:
        plt.imshow(blueArray)
    elif options == 4:
        savefile(bayerFilter, name)
    else:
        print('Not a valid option')

