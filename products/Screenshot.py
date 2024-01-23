import pyautogui

class Screenshot():
    def __init__(self, product) :
        self.timeHours = product.dateTime()
    
    def printScreen(self):
        im1 = pyautogui.screenshot()
        im1.save(self.hours())
             
    def hours(self):
        time = self.timeHours
        newTime = ""
        for times in time:
            if times[0] == "/" or times[0] == "," or times[0] == ":":
                newTime += " "
            else:
                newTime += times[0]
        newTime += ".png"
        return newTime
    