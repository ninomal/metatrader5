import pyautogui
from enums.enumsGraphics import enumsGraph
import time

class Screenshot():
    def __init__(self, imgName) :
        self.imgName = imgName
    
    def printScreen(self):
        time.sleep(10.0)
        im1 = pyautogui.screenshot()
        im1.save(self.imgName)
    
      
    