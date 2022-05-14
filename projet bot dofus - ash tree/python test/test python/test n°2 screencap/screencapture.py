from time import time
import cv2 as cv
import numpy as np
import os
import pyautogui
from PIL import ImageGrab
import win32gui, win32ui, win32con

os.chdir(os.path.dirname(os.path.abspath(__file__)))


loop_time=time()
while(True):
    screenshot=ImageGrab.grab()
    screenshot=np.array(screenshot)
    #change color from rgb to gbi
    screenshot=screenshot[:,:,::-1].copy()

    cv.imshow('Bot Vision', screenshot)

    #show frp/sec
    print('Fps{}'.format(1/(time()-loop_time)))
    loop_time=time()
    
    #a to end 'bot vision'(=all the program)
    if cv.waitKey(1)==ord('a'):
        cv.destroyAllWindows()
        break

print('Done')