

class LoguinMt5():
    def __init__(self,name, password, server ,portable, mt5) :
       self.mt5 = mt5
       self.name = name
       self.password = password
       self.server = server
       self.portable = portable
       
    
    def logar(self):     
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",self.mt5.__author__)
        print("MetaTrader5 package version: ",self.mt5.__version__)
            
        # establish connection to the MetaTrader 5 terminal
        if not self.mt5.initialize():
                print("initialize() failed, error code =",self.mt5.last_error())
                quit()
            
        # display data on MetaTrader 5 version
        print(self.mt5.version())
        # connect to the trade account without specifying a password and a server
        account= self.name
        authorized=self.mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
        if authorized:
            print("connected to account #{}".format(account))
        else:
             print("failed to connect at account #{}, error code: {}".format(account, self.mt5.last_error()))
            
        # now connect to another trading account specifying the password
        account=self.name
        authorized=self.mt5.login(account, password = self.password)
        if authorized:
            # display trading account data 'as is'
            print(self.mt5.account_info())
            # display trading account data in the form of a list
            print("Show account_info()._asdict():")
            account_info_dict = self.mt5.account_info()._asdict()
            for prop in account_info_dict:
                    print("  {}={}".format(prop, account_info_dict[prop]))
            else:
                print("failed to connect at account #{}, error code: {}".format(account, self.mt5.last_error()))
            
            # shut down connection to the MetaTrader 5 terminal
            self.mt5.shutdown()
    
    
    def deslogar(self):
        # establish connection to the MetaTrader 5 terminal
        if not self.mt5.initialize():
            print("initialize() failed")
            quit()
        
        # display data on connection status, server name and trading account
        print(self.mt5.terminal_info())
        # display data on MetaTrader 5 version
        print(self.mt5.version())
        
        # shut down connection to the MetaTrader 5 terminal
        self.mt5.shutdown()
        