import login
import time

SERVERDEMO ="MetaQuotes-Demo"
SERVERREAL ="MetaQuotes-Real"
MOBILE = False # metatrader5 from mobile (True or False)
SYMBOL = "WINV23" #name of market

def main():
    
    # get struct_time
    named_tuple = time.localtime() 
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    
    loguin = input("Digit your loguin user: ") 
    password = input("Digit your password user: ")   
    
      
    mt5 = login.LoguinMt5(loguin ,password ,SERVERREAL,time_string ,MOBILE)
    
    print(mt5.server)
    mt5.logar()
    
    
    
    
if __name__ == "__main__":
    main()