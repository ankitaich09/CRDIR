#this program takes in a raw image
#changes it to an rgb image
#outputs three separate histograms (R, G and B) for three channels
#Outputs a fourth histogram for the grayscale image

import rawpy
import cv2
import matplotlib.pyplot as plt


def histogramMake(path, channel='R'):
    rawImage = rawpy.imread(path)
    rgbImg = rawImage.postprocess()
    redHist = cv2.calcHist(rgbImg, [1], None, [256], [0, 256])
    greenHist = cv2.calcHist(rgbImg, [2], None, [256], [0, 256])
    blueHist = cv2.calcHist(rgbImg, [3], None, [256], [0, 256])
    if channel == 'R':
        plt.plot(redHist)
        plt.title('Red Channel Histogram')
        plt.show()
    elif channel == 'G':
        plt.plot(greenHist)
        plt.title('Green Channel Histogram')
        plt.show()
    elif channel == 'B':
        plt.plot(blueHist)
        plt.title('Blue Channel Histogram')
        plt.show()
    else:
        print('Wrong option, choose between R, G, B')


