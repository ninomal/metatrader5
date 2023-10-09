
import MetaTrader5 as mt5
class LoguinMt5():
    def __init__(self,name, password, server, time,portable) :
       self.name = name
       self.password = password
       self.server = server
       self.time = time
       self.portable = portable
       
    
    def logar(self):       
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
            
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
                print("initialize() failed, error code =",mt5.last_error())
                quit()
            
        # display data on MetaTrader 5 version
        print(mt5.version())
        # connect to the trade account without specifying a password and a server
        account= self.name
        authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
        if authorized:
            print("connected to account #{}".format(account))
        else:
             print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
            
        # now connect to another trading account specifying the password
        account=self.name
        authorized=mt5.login(account, password = self.password)
        if authorized:
            # display trading account data 'as is'
            print(mt5.account_info())
            # display trading account data in the form of a list
            print("Show account_info()._asdict():")
            account_info_dict = mt5.account_info()._asdict()
            for prop in account_info_dict:
                    print("  {}={}".format(prop, account_info_dict[prop]))
            else:
                print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
            
            # shut down connection to the MetaTrader 5 terminal
            mt5.shutdown()
    
    @classmethod
    def deslogar():
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed")
            quit()
        
        # display data on connection status, server name and trading account
        print(mt5.terminal_info())
        # display data on MetaTrader 5 version
        print(mt5.version())
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        