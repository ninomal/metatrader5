
import pandas as pd

class Infos:
    def __init__(self, mt5) -> None:
        self.mt5 = mt5
        print("MetaTrader5 package author: ",self.mt5.__author__)
        print("MetaTrader5 package version: ",self.mt5.__version__)
        
    def infos(self):
        # establish connection to the MetaTrader 5 terminal
        if not self.mt5.initialize():
            print("initialize() failed, error code =",self.mt5.last_error())
            quit()
        
        # connect to the trade account specifying a password and a server
        authorized=self.mt5.login()
        if authorized:
            account_info=self.mt5.account_info()
            if account_info!=None:
                # display trading account data 'as is'
                print(account_info)
                # display trading account data in the form of a dictionary
                print("Show account_info()._asdict():")
                account_info_dict = self.mt5.account_info()._asdict()
                for prop in account_info_dict:
                    print("  {}={}".format(prop, account_info_dict[prop]))
                print()
                # convert the dictionary into DataFrame and print
                df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
                print("account_info() as dataframe:")
                print(df)
        else:
            print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",self.mt5.last_error())
        
        # shut down connection to the MetaTrader 5 terminal
        self.mt5.shutdown()
 