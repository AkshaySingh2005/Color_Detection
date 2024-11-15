import numpy as np
import cv2

def get_limits(color):

    color = np.uint8([[color]]) 
    
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    hue = hsv_color[0][0][0]
    lower_limit = np.array([hue - 10, 100, 100]) 
    upper_limit = np.array([hue + 10, 255, 255])
    
    return lower_limit, upper_limit
