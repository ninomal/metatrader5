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


ASSET = "WING24" #Change name of ASSETS HERE exemple :"WDOc1"
SECONDS = 2 # seconds that the graphs will be shown here 
PHONENUMBER = "you watssap number"

os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info()                   
    selecTime = "1" #select time here, string type exp '2' or '3' 
    products = product.Products(mt5, selecTime, ASSET)
    productsService = productsServices.ProductsServices(mt5, selecTime, ASSET)
    services = service.Service(mt5, selecTime, ASSET)
    ui = UI(mt5, selecTime, ASSET, SECONDS)
    screenShot = Screenshot.Screenshot(products, ui)
    adbConect = Adbconect(PHONENUMBER, products, ui)
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
    
if __name__ == "__main__":
    main()