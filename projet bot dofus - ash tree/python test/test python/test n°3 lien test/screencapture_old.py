from ctypes.wintypes import HWND
import imghdr
from pickle import NONE
from time import time
import cv2 as cv
import numpy as np
import os
import pyautogui
import win32gui, win32ui, win32con

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def screen_capture():
    w = 1920 
    h = 1080 
    
    #hwnd = win32gui.FindWindow(None, windowname)
    #hwnd=win32gui.FindWindow(NONE, windowname)

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

    signedIntsArray=dataBitMap.GetBitsmapBits(True)
    img=np.fromstring(signedIntsArray,dtype='uint8')
    img_shape=(h,w,4)
# Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    #"delete" alpha (baisse de frp)
    img=img[...,:3]

    img=np.ascontiguousarray(img)

    return img

loop_time=time()
while(True):
    screenshot=screen_capture()
    screenshot=np.array(screenshot)
    #change color from rgb to gbi
    screenshot=screenshot[:,:,::-1].copy()

    cv.imshow('Bot Vision', screenshot)

    print('Fps{}'.format(1/(time()-loop_time)))
    loop_time=time()
    
    #a to end 'bot vision'(=all the program)
    if cv.waitKey(1)==ord('a'):
        cv.destroyAllWindows()
        break


screen_capture()
print('Done')