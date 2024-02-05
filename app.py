import time
import MetaTrader5 as mt5
from services import service
import os
from products import product 
from products import productsServices
from ui.ui import UI
from enums import enumsTime
from products import Screenshot
from products.Adb import Adbconect
import threading

SELECTTIME = "1" #select time here, string type exp '2' or '3' 
ASSET = "WING24" #Change name of ASSETS HERE exemple :"WDOc1"
SECONDS = 2 # seconds that the graphs will be shown here 
PHONENUMBER = "you watssap number"

os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info()                   
    
    products = product.Products(mt5, SELECTTIME, ASSET)
    productsService = productsServices.ProductsServices(mt5, SELECTTIME, ASSET)
    services = service.Service(mt5, SELECTTIME, ASSET)
    ui = UI(mt5, SELECTTIME, ASSET, SECONDS)
    screenShot = Screenshot.Screenshot(products)
    #adbConect = Adbconect(PHONENUMBER, products, ui)
    print()
    print(products.date_of_Day())
    #print(productsService.dayForconvert())
    #print(products.lastBar())
    ui.lastGraph('true')
    #ui.allGraph()
    #ui.graphIntraDay()  
    #ui.uiBar()
    #ui.allRedBar()
    #ui.sortedRedBarIntraday()
    #productsService.mfi()
    print()
    #services.sell()
    #services.buy()
    #ui.PizzaGraphForce()
    #productsService.teste()
    #ui.adGraph()
    #ui.eomGraph()
    #ui.eomGraphNow()
    #ui.adGraphNow()
    #screenShot.printScreen()
    #adbConect.adbConect()
    products.listOfImg()
    print("esse")
    print(products.hoursImgName[0])
    
th1 = threading.Thread(target=main)
print(3)
mt5.initialize()
products = product.Products(mt5, SELECTTIME, ASSET)
screenShot = Screenshot.Screenshot(products.hoursImgName())
th2 = threading.Thread(target=screenShot.printScreen)

th1.start()
th2.start()
    
    
    
#if __name__ == "__main__":
    #main()