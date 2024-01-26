import pyautogui
from enums.enumsGraphics import enumsGraph

class Screenshot():
    def __init__(self, product) :
        self.timeHours = product.dateTime()
        self.enumsGraph = enumsGraph()
        self.product = product
    
    def printScreen(self):
        im1 = pyautogui.screenshot()
        im1.save(self.hours())
             
    def hours(self):
        time = self.timeHours
        newTime = ""
        for times in time:
            if times[0] == "/" or times[0] == "," or times[0] == ":":
                newTime += " "
            elif times[0]== " " :
                newTime+=""
            else:
                newTime += times[0]
        newTime += ".png"
        return newTime
    
    def imageSelect(self, value):
        image = self.enumsGraph(value)
        self.product.defineSleep(2.0)
        self.printScreen()
        