#imports

import pyautogui
import random
import time
import numpy as np

#random variables

x = np.random.randint(100,500)
y = np.random.randint(100,500)
z = np.random.randint(100,500)
b = np.random.randint(100,500)
num_seconds = 3
#script

while True:
    pyautogui.moveTo(x,y)
    time.sleep(5)
    pyautogui.dragTo(z,b,duration=num_seconds)
