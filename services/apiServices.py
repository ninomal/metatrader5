from products.Apiconect import Apiconect
from products.Screenshot import Screenshot
from ui.ui import UI
from services.service import Service
from enums.enumsGraphics import EnumsGraph
from products.Apiconect import Apiconect
from products.product import Products
import threading
import time


class ApiServices():  
    def __init__(self, mt5, selecTime, ASSET, SECONDS, PHONENUMBER) :
        self.mt5 = mt5
        self.selecTime = selecTime
        self.ASSET = ASSET
        self.SECONDS = SECONDS
        self.phone = PHONENUMBER
        self.product = Products(self.mt5, self.SECONDS, self.ASSET)
        self.ui = UI(self.mt5, self.selecTime, self.ASSET, self.SECONDS)
        self.services = Service(self.mt5, self.selecTime, self.ASSET)
        self.enumsGraph = EnumsGraph(self.ui)
        self.apiConect = Apiconect(self.mt5,self.selecTime,self.ASSET,self.phone,self.ui)
        
    def selectGraph(self):
        valueStr = self.apiConect.readTxt()
        self.enumsGraph.selectUIgrap(valueStr)
        
    def actions(self):
        valueStr = self.apiConect.readTxt()
        if valueStr == "buy":
            self.services.buy()
        elif valueStr == "sell":
            self.services.sell()
        else:
            print("Action error")
            
    def callScreenShoot(self):
        apiConect = Apiconect(self.mt5, self.selecTime, self.ASSET, self.phone, self.ui)
        th1  = threading.Thread(target=apiConect.selecGraph)
        screenShot = Screenshot(self.product.hoursImgName())
        th2 = threading.Thread(target=screenShot.printScreen)
        time.sleep(1.0)
        th1.start()
        th2.start()
        
        
    