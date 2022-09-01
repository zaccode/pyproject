import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1) #it capture the full screen automatically by pass 0 and 1

dim = (width,height)

f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("")
