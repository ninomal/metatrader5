import time
import MetaTrader5 as mt5
from services import service
import os
from products import product 
from products import productsServices
from UI.ui import UI
from exception.timeflameException import TimeflameException
from enums.timeflameEnums import TimeFrameEnums

SERVERDEMO = "SERVERDEMO" #"MetaQuotes-Demo"
SERVERREAL ="SERVERREAL" #"MetaQuotes-Real"
MOBILE = False # metatrader5 from mobile (True or False)

os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    #mt5.terminal_info()
    '''
    print('welcome')
    timeframeVariable = input(
            "for minutes press: " 
            '1m, 2m, 3m, 4m, 5m,6m ,10m ,12m ,15m ,20m ,30m ,60m'
            'for hours: 2h ,3h ,4h ,6h ,8h ,12h ,'
            'for days: 1d ,'
            'for week: 1w '
            'for month: 1mon :')                   
    timeframeStr = TimeflameException(timeframeVariable) 
    #instace objects
    teste = TimeFrameEnums(mt5 , timeframeVariable)
    testconv = teste.timeframe()
    '''
    services = service.Service(mt5)
    products = product.Products(mt5)
    productsService = productsServices.ProductsServices(mt5)
    print()
    
    print(products.date_of_Day())
    products.current_day()
    ui = UI(mt5)
    #ui.lastGraph()
    #ui.allGraph()
    #ui.graphIntraDay()
    
    #ui.uiBar()
    print()
    #services.sell()
    #services.buy()
    
if __name__ == "__main__":
    main()