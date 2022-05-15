from pickle import NONE
import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture

# show the folder path to the code to prevent error with downloading and changing folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
# x=name of character to help find the client to wincap(windowcapture)
x = input("Entrer le nom du personnage:")
time.sleep(2)
wincap = WindowCapture(x+' - Dofus 2.63.8.10')

while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # show fps/sec (dont work with time.sleep[l.15])
    #print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()

    # press 'a' to close the 'bot vision'
    if cv.waitKey(1) == ord('a'):
        cv.destroyAllWindows()
        break

print('Done.')
