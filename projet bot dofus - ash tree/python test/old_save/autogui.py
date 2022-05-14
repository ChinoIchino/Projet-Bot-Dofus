from cv2 import threshold
import pyautogui
import time
import cv2 as cv
import numpy as np
import os

ash_wood = os.path.join(os.path.dirname(__file__), 'ash_tree.png')
assert os.path.exists(ash_wood)
map_raw = os.path.join(os.path.dirname(__file__), 'deux_arbre.png')
assert os.path.exists(map_raw)

wood_lvl1=cv.imread(ash_wood,cv.IMREAD_UNCHANGED)
map=cv.imread(map_raw,cv.IMREAD_UNCHANGED)

resultat=cv.matchTemplate(map,wood_lvl1,cv.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv.minMaxLoc(resultat)
print("best match: %s" % str(max_loc))
print("best confidence: %s" % max_val)

print(resultat)

threshold = 0.40
if max_val >=threshold:
    print('arbre trouver')

    map_width=map.shape[1]
    map_height=map.shape[0]

    top_left=(max_loc)
    bottom_right=(top_left[0]+map_width+top_left[1]+map_height)

    #cv.rectangle(map, top_left, bottom_right, 
    # (0,255,0), 2, cv.LINE_4)
    cv.imshow('Resultat', resultat)
    cv.waitKey()
    
    #make a file named 'resultat.jpg' in the folder
    #cv.imwrite('resultat.jpg',map)
else:
    print('arbre non trouver')






#pyautogui.FAILSAFE=True

#10sec avant lancement
#print("starting...", end="")
#for i in range(0,10):
#    print(".", end="")
#    time.sleep(1)
#print("Go")




#print("fin")