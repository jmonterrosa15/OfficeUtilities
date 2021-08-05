#This is the final version
#This script moves the cursor of your screen in the top left corner and clicks every 60 seconds

import pyautogui
import time
import sys
from datetime import datetime
import random
import os

pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = int(input('Enter the number of minutes: '))
    print('Hit Control + C to cancel!')
else:
    numMin = int(sys.argv[1])

x = 0
while(x < numMin):
    time.sleep(60)
    pos_x = random.randint(0,120)
    pos_y = random.randint(0,64)
    pyautogui.moveTo(pos_x,pos_y)
    pyautogui.click()
    print('Movement made at {}'.format(datetime.now().time()))
    x += 1

print('End of script')
os.system("pause")
