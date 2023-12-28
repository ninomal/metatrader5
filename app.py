import time
import MetaTrader5 as mt5
from services import service
import os
from products import product 
from products import productsServices
from ui.ui import UI

os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info() 
    services = service.Service(mt5)
    products = product.Products(mt5)
    productsService = productsServices.ProductsServices(mt5)
    print()
 
    print(products.date_of_Day())
    #print(productsService.dayForconvert())
    #print(products.lastBar())
    ui = UI(mt5)
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
    
if __name__ == "__main__":
    main()