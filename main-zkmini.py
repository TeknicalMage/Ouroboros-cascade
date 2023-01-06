import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

from mss import mss
from PIL import Image



# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Zero-K')


#Part of the code where we are looking for shit -----------w
# load the trained model
cascade_limestone = cv.CascadeClassifier('cascade.xml')
# load an empty Vision class
vision_limestone = Vision(None)

topvar = 735
leftvar = 1440
widthvar = 480
heightvar = 270


bounding_box = {'top': 735, 'left': 1440, 'width': 480, 'height': 270}
sct = mss()

#loop_time = time()

width = 960
height = 540

dim = (width, height)

while(True):

    sct_img = sct.grab(bounding_box)
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # do object detection 
    rectangles = cascade_limestone.detectMultiScale(screenshot)

    # draw the detection results onto the original image
    detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)

    

    # display the images
    #cv.imshow('Matches', detection_image)

    macro = cv.resize(np.array(sct_img), dim, interpolation = cv.INTER_AREA)

  


    
    cv.imshow('Matches', macro)
    
    cv.setWindowProperty('Matches', cv.WND_PROP_TOPMOST, 1)

    # debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(20)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
        print('pos')
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
        print('neg')
    elif key == ord('c'):
        print("get fucked")
        #mac = cv.resize(detection_image, rectangles, interpolation = cv.INTER_AREA)
        #cv.imshow("win2", mac)

print('Done.')
