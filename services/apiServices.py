from products.Apiconect import Apiconect
from products.Screenshot import Screenshot
from ui.ui import UI
from services.service import Service
from enums.enumsGraphics import EnumsGraph
from products.Apiconect import Apiconect
from products.product import Products
from products.productsServices import ProductsServices
import threading
import time


class ApiServices():  
    def __init__(self, mt5, selecTime, ASSET, SECONDS, PHONENUMBER, HOURSSTART) :
        self.mt5 = mt5
        self.selecTime = selecTime
        self.ASSET = ASSET
        self.SECONDS = SECONDS
        self.phone = PHONENUMBER
        self.HOURSSTART = HOURSSTART
        self.product = Products(self.mt5, self.selecTime, self.ASSET, HOURSSTART)
        self.ui = UI(self.mt5, self.selecTime, self.ASSET, self.SECONDS, HOURSSTART)
        self.services = Service(self.mt5, self.selecTime, self.ASSET)
        self.enumsGraph = EnumsGraph(self.ui)
        self.apiConect = Apiconect(self.mt5,self.selecTime,self.ASSET,self.phone,self.ui,HOURSSTART)
        self.productService = ProductsServices(self.mt5, selecTime, ASSET, HOURSSTART)
        
    def selectGraph(self):
        valueStr = self.apiConect.readTxt()
        self.enumsGraph.selectUIgrap(valueStr)
        
    def actions(self):
        while valueStr != 'exit':
            valueStr = self.apiConect.readTxt()
            if valueStr == "buy":
                self.services.buy()
            elif valueStr == "sell":
                self.services.sell()
            elif valueStr == 'selecgraph':
                self.graficsSelectApiUi()
            elif valueStr == 'calcv':
                self.calcvScreen()
            else:
                pass
            
    def callScreenShoot(self):
        #apiConect = Apiconect(self.mt5, self.selecTime, self.ASSET, self.phone, self.ui, self.HOURSSTART)
        #th1  = threading.Thread(target=apiConect.selecGraph)
        screenShot = Screenshot(self.product.hoursImgName())
        th2 = threading.Thread(target=screenShot.printScreen)
        time.sleep(1.0)
        #th1.start()
        th2.start()
        time.sleep(15.0)
        th4 = threading.Thread(target=self.apiConect.sendImage)
        th4.start() 
         
    def calcvScreen(self):
        if self.productService.calcV():
            #th3 = threading.Thread(target= self.apiConect.apiConectZap)
            th1  = threading.Thread(target=self.ui.mt5Graf)
            screenShot = Screenshot(self.product.hoursImgName())
            th2 = threading.Thread(target=screenShot.printScreen)
            time.sleep(1.0)
            th1.start()
            th2.start()
            time.sleep(20)
            #th3.start()
            time.sleep(60.0)
            th4 = threading.Thread(target=self.apiConect.sendImage)
            th4.start()        
                      
    def graficsSelectApiUi(self): 
        #th3 = threading.Thread(target= self.apiConect.apiConectZap)
        th1  = threading.Thread(target=self.apiConect.selecGraph, daemon=True)
        screenShot = Screenshot(self.product.hoursImgName())
        th2 = threading.Thread(target=screenShot.printScreen)
        time.sleep(1.0)
        th1.start()
        th2.start()
        time.sleep(10)
        #th3.start()
        time.sleep(30.0)     
        th4 = threading.Thread(target=self.apiConect.sendImage)
        th4.start()        