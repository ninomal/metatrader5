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
ASSET = "WINJ24" #Change name of ASSETS HERE exemple :"WDOc1"
SECONDS = 2 # seconds that the graphs will be shown here 
PHONENUMBER = "you watssap number"
HOURSSTART = '9:00:00' # IF you wish market start hours exemple '9:00:00'


os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info()   
    products = Products(mt5, SELECTTIME, ASSET, HOURSSTART)
    productsService = ProductsServices(mt5, SELECTTIME, ASSET, HOURSSTART)
    services = Service(mt5, SELECTTIME, ASSET)
    ui = UI(mt5, SELECTTIME, ASSET, SECONDS, HOURSSTART)
    screenShot = Screenshot(products)
    apiConect = Apiconect(mt5, SELECTTIME, ASSET, PHONENUMBER, ui, HOURSSTART)
    adbConect = Adbconect(PHONENUMBER)
    apiService = ApiServices(mt5, SELECTTIME, ASSET,SECONDS,PHONENUMBER, HOURSSTART)
    print()
    print(products.date_of_Day())
    #print(productsService.dayForconvert())
    #print(products.lastBar())
    #ui.lastGraph('true')
    #ui.allGraph()
    #ui.graphIntraDay()  
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
    #screenShot.printScreen()
    #adbConect.adbConect()
    #apiService.callScreenShoot()
    #apiConect.sendImage()
    #ui.calcV()
    #productsService.calcVfunc()
    ui.mt5Graf() 
    #apiService.calcvScreen()
    #time.sleep(10.0)
    #products.clearAllimage()
    
    



    
if __name__ == "__main__":
    main()