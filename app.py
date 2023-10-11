import login
import time
import timeflameEnums
import timeflameException
import MetaTrader5 as mt5

SERVERDEMO = "SERVERDEMO" #"MetaQuotes-Demo"
SERVERREAL ="SERVERREAL" #"MetaQuotes-Real"
MOBILE = False # metatrader5 from mobile (True or False)
SYMBOL = "WINV23" #name of market

def main(): 
    
    #Start
    # get struct_time
    #named_tuple = time.localtime() 
    #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    #loguin = input("Digit your loguin user: ") 
    #password = input("Digit your password user: ") 
    mt5.initialize() 
    mt5.terminal_info()
    
    #timeFlameVariable = input('for minutes press 1 , 2 , 3 ,4 , 5 ,6 ,10 ,12 ,15 ,20 ,30 ,60 ,'
                     # 'for hours "2h" ,"3h" ,"4h" ,"6h" ,"8h" ,"12h" ,'
                      #'for days "1d" ,"2d" ,"3d"')
    
    
    #get timeflame execption
    #timeflameEx = timeflameException.TimeflameException(timeFlameVariable)
    #timeflameEx.timeflameCheck()
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()