import time
import MetaTrader5 as mt5
from services.service import Service
import os
from products.product import Products
from products.productsServices import ProductsServices
from ui.ui import UI
from enums.enumsTime import Timeframe
from products.Screenshot import Screenshot
from products.Adb import Adbconect
import threading
from products.Apiconect import Apiconect
from services.apiServices import ApiServices

SELECTTIME = "1" #select time here, string type exp '2' or '3'
ASSET = "WING24" #Change name of ASSETS HERE exemple :"WDOc1"
SECONDS = 2 # seconds that the graphs will be shown here 
PHONENUMBER = "you watssap number"


os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info()     
    products = Products(mt5, SELECTTIME, ASSET)
    productsService = ProductsServices(mt5, SELECTTIME, ASSET)
    services = Service(mt5, SELECTTIME, ASSET)
    ui = UI(mt5, SELECTTIME, ASSET, SECONDS)
    screenShot = Screenshot(products)
    apiConect = Apiconect(mt5, SELECTTIME, ASSET, "214550", ui)
    adbConect = Adbconect(PHONENUMBER)
    apiService = ApiServices(mt5, SELECTTIME, ASSET,SECONDS,PHONENUMBER)
    print()
    print(products.date_of_Day())
    #print(productsService.dayForconvert())
    #print(products.lastBar())
    #ui.lastGraph('true')
    #ui.allGraph()
    #ui.graphIntraDay()  
    #ui.uiBar()
    #ui.allRedBar()
    #ui.sortedRedBarIntraday()
    #productsService.mfi()
    print()
    #services.sell()
    #services.buy()
    #ui.pizzaGraphForce()
    #productsService.teste()
    #ui.adGraph()
    #ui.eomGraph()
    #ui.eomGraphNow()
    #ui.adGraphNow()
    #screenShot.printScreen()
    adbConect.adbConect()
    print(products.hoursImgName())
    apiService.callScreenShoot()
    time.sleep(10.0)
    apiConect.sendImage()
    
    
'''
th1 = threading.Thread(target=main)
mt5.initialize()
products = product.Products(mt5, SELECTTIME, ASSET)
screenShot = Screenshot.Screenshot(products.hoursImgName())
th2 = threading.Thread(target=screenShot.printScreen)

th1.start()
th2.start()
    
    '''
    
if __name__ == "__main__":
    main()