import cv2 as cv
import numpy as np
import os
import pyautogui

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while(True):
    screenshot=pyautogui.screenshot()
    screenshot=np.array(screenshot)

    cv.imshow('Computer Vision', screenshot)

    if cv.waitKey(1)==ord('a'):
        cv.destroyAllWindows()
        break

print('Done')
