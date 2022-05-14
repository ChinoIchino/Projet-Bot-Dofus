from pickle import NONE
from cv2 import threshold
import cv2 as cv
import numpy as np
import os

ash_wood = os.path.join(os.path.dirname(__file__), 'ash_tree.png')
assert os.path.exists(ash_wood)
map_raw = os.path.join(os.path.dirname(__file__), 'first_try.png')
assert os.path.exists(map_raw)

wood_lvl1=cv.imread(ash_wood,cv.IMREAD_UNCHANGED)
map=cv.imread(map_raw,cv.IMREAD_UNCHANGED)

def click_coord(ash_wood,map_raw,threshold=0.5,debug_mode=NONE):
    map=cv.imread(map_raw,cv.IMREAD_UNCHANGED)
    wood_lvl1=cv.imread(ash_wood,cv.IMREAD_UNCHANGED)
    
    wood_w=wood_lvl1.shape[1]
    wood_h=wood_lvl1.shape[0]

    methode=cv.TM_CCOEFF_NORMED
    resultat=cv.matchTemplate(map,wood_lvl1,methode)

    locations=np.where(resultat >= threshold)
    locations=list(zip(*locations[::-1]))

    rectangles=[]
    for loc in locations:
        rect=[int(loc[0]),int(loc[1]),wood_w,wood_h]
        rectangles.append(rect)
        rectangles.append(rect)

        rectangles,weight=cv.groupRectangles(rectangles,groupThreshold=1,eps=0.5)

        point=[]
        if len(rectangles):
            line_color=(0,255,0)
            line_type=cv.LINE_4
            marker_color=(255,0,0)
            marker_type=cv.MARKER_CROSS

            for (x,y,w,h) in rectangles:
                center_x=x+int(w/2)
                center_y=y+int(h/2)
                point.append((center_x,center_y))

                if debug_mode=='rectangles':
                    top_left=(x,y)
                    bottom_right=(x+w,y+h)
                    cv.rectangle(map,top_left,bottom_right,color=line_color,
                                lineType=line_type,thickness=2)
                elif debug_mode=='points':
                    cv.drawMarker(map,(center_x,center_y),
                                color=marker_color,markerType=marker_type,
                                markerSize=40,thickness=2)
            if debug_mode:
                cv.imshow('Matches',map)
                cv.waitKey()
        return points
    points=click_coord('ash_tree.png','deux_arbre.png',debug_mode='points')
    print(points)
    print('done')

click_coord(ash_wood,map_raw,threshold=0.5,debug_mode=NONE)