import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

class ServicesMql():
    def __init__(self):
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
    
    def getSymbols(self, size):
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()  
        # get all symbols
        symbols=mt5.symbols_get()
        print('Symbols: ', len(symbols))
        count=0
        # display the first five ones
        for s in symbols:
            count+=1
            print("{}. {}".format(count,s.name))
            if count==size: 
                break
        print()
        '''
        # get symbols containing RU in their names
        ru_symbols=mt5.symbols_get("*RU*")
        print('len(*RU*): ', len(ru_symbols))
        for s in ru_symbols:
            print(s.name)
        print()'''
        
    def symbolsNotUsdEtc(self):
        # get symbols whose names do not contain USD, EUR, JPY and GBP
        group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
        print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
        for s in group_symbols:
            print(s.name,":",s)
            
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        
    def historyOrdersGet(self, year, month, day, asset, position_id):
        from_date= datetime(year , month, day)
        to_date= datetime.now()
        print(to_date)
        history_orders=mt5.history_orders_get(from_date, to_date, group= f"*{asset}*")
        if history_orders==None:
            print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
        elif len(history_orders)>0:
            print("history_orders_get({}, {}, group=\"*{}*\")={}".format(from_date,to_date,len(history_orders),asset))
        print()
        # display all historical orders by a position ticket
        position_history_orders= mt5.history_orders_get(position=position_id)
        if position_history_orders==None:
            print("No orders with position #{}".format(position_id))
            print("error code =", mt5.last_error())
        elif len(position_history_orders)>0:
            print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))
            # display all historical orders having a specified position ticket
            for position_order in position_history_orders:        
                print(position_order)
            print()
            # display these orders as a table using pandas.DataFrame
            df=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())
            df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)
            df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
            df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
            print(df)