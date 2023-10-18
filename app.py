import time
import MetaTrader5 as mt5
from services import service
import os
from products import product 
from products import productsServices
from UI.ui import UI


SERVERDEMO = "SERVERDEMO" #"MetaQuotes-Demo"
SERVERREAL ="SERVERREAL" #"MetaQuotes-Real"
MOBILE = False # metatrader5 from mobile (True or False)

os.system('cls')
def main():    
    #Start
    mt5.initialize() 
    mt5.terminal_info()
    services = service.Service(mt5)
    products = product.Products(mt5)
    productsService = productsServices.ProductsServices(mt5)
    ui = UI(mt5)
    ui.teste()
    ui.construc()
    #productsService.calcAMV()
    #productsService.calcEma()
    #productsService.adv()
    #productsService.priceVol()
    
    
    #print(mt5.terminal_info())
    #print(products.lastBar())
    #print('a')
    #products.selectBar('close')
    
    # get struct_time
    #named_tuple = time.localtime() 
    #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    #loguin = input("Digit your loguin user: ") 
    #password = input("Digit your password user: ") 
    
    #timeFlameVariable = input('for minutes press 1 , 2 , 3 ,4 , 5 ,6 ,10 ,12 ,15 ,20 ,30 ,60 ,'
                     # 'for hours "2h" ,"3h" ,"4h" ,"6h" ,"8h" ,"12h" ,'
                      #'for days "1d" ,"2d" ,"3d"')  
    print()
    #services.sell()
    #services.buy()
    '''orders= services.buyOrders + services.sellOrders
    if orders!= 0:
        print("Total orders=",orders)
    else:
        print("Orders not found")
        
    #get timeflame execption
    #timeflameEx = timeflameException.TimeflameException(timeFlameVariable)
    #timeflameEx.timeflameCheck()
     
        '''
if __name__ == "__main__":
    main()