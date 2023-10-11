
#Services
class Service():
    def __init__(self, mt5):
        self.mt5 = mt5
        TIMEFRAME = self.mt5.TIMEFRAME_M1
    
    def symbol(self):
        symbol_info_tick_dict = self.mt5.symbol_info_tick(self.SYMBOL)
        return symbol_info_tick_dict
    
    ATIVO = "WINV23" #name of market
    VOLUME = 1.0 #volume observe compatibility volume error change for 1.0 Demo verion
    ONDAS = 20
    MAGIC = 10
    ONDAS_BOLINGER = 20
    STANDER_DEVIATIONS = 2
    TL_SD = 2
    SL_SD = 2
    deviation = 0

    def buy(self):
        preco = self.mt5.symbol_info_tick(self.ATIVO).ask
        pontos = self.mt5.symbol_info(self.ATIVO).point
        print(preco)
        request = ({
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": self.ATIVO,
            "volume": 1.0,
            "type": self.mt5.ORDER_TYPE_BUY,
            "price": preco,
            "deviation":self. deviation,
            "sl": preco - 50 * pontos,
            "tp":preco + 50 * pontos,
            "magic": 12345,
            "comment": "python script buy",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_RETURN
        })
        self.mt5.order_send(request)
        result = self.mt5.order_send(request)
        print("aaaa")
        print(result)


    def sell(self):
        preco = self.mt5.symbol_info_tick(self.ATIVO).bid
        pontos = self.mt5.symbol_info(self.ATIVO).point
        request = ({
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": self.ATIVO,
            "volume": self.VOLUME,
            "type": self.mt5.ORDER_TYPE_SELL,
            "price": preco,
            "deviation": self.deviation,
            "sl": preco + 50 * pontos,
            "tp":preco - 50 * pontos,
            "magic": 12345,
            "comment": "python script sell",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_RETURN
        })
        self.mt5.order_send(request)
        result = self.mt5.order_send(request)
        print(result)

    
    def lastick(self):
        #test
        lasttick= self.mt5.symbol()
        print(lasttick)
        # display tick field values in the form of a list
        print(f"Show symbol_info_tick({lasttick})._asdict():")
        symbol_info_tick_dict = lasttick._asdict()
        for prop in symbol_info_tick_dict:
            print("  {}={}".format(prop, symbol_info_tick_dict[prop]))
              
    
    #def __repr__(self) -> str:
       # if(buy != 0):
           # return f"Buy {self.symbol} market {self.SYMBOL}"
       # elif(sell != 0):
           # return f"Sell {self.symbol} market {self.SYMBOL}"