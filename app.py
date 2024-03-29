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
from services.servicesMql import ServicesMql

SELECTTIME = "1" #select time here, string type exp '2' or '3'
ASSET = "WINJ24" #Change name of ASSETS HERE exemple :"WDOc1"
SECONDS = 2 # seconds that the graphs will be shown here 
PHONENUMBER = "You watssap number"
HOURSSTART = '9:00:00' # IF you wish market start hours exemple '9:00:00'
#TOLLS constant
SIZESYMBOLS = 20 # size of the asset name output
DAY = 20 
MONTH = 3
YEAR = 2024
POSITIONID = 0 # name of asset id

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
    servicesMql = ServicesMql()
    print()
    print(products.date_of_Day())
    #apiConect.apiConectZap()
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
    #ui.mt5Graf() 
    #ui.mt5GrafInMpf()
    #apiService.calcvScreen()
    #apiService.graficsSelectApiUi()
    #ui.eomGraphNow()
    #ui.adGraphNow()
    #servicesMql.getSymbols(SIZESYMBOLS)
    #servicesMql.historyOrdersGet(YEAR, MONTH, DAY, ASSET, POSITIONID)
    #servicesMql.symbolInfo(ASSET) 
    productsService.copyFromRates(mt5, ASSET, mt5.TIMEFRAME_D1, 0, 300)
     



    
if __name__ == "__main__":
    main()