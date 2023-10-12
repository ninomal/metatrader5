
#Services
class Service():
    def __init__(self, mt5):
        self.mt5 = mt5
        self.TIMEFRAME = self.mt5.TIMEFRAME_M1
        #self.timeframe = timeframe implement
        self.buyOrders = 0
        self.sellOrders = 0
        
    def symbol(self):
        symbol_info_tick_dict = self.mt5.symbol_info_tick(self.SYMBOL)
        return symbol_info_tick_dict
    
    ATIVO = "WINV23" #name of market
    VOLUME = 1.0 #volume observe compatibility volume error change for 1.0 Demo version
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
        self.buyOrders += 1
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
        self.sellOrders += 1
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
              
    
    def __repr__(self) -> str:    
        if(self.buyOrders != 0):
            return f"Buy {self.symbol}, {self.buyOrders} Ticks in market {self.SYMBOL}"
        elif(self.sellOrders != 0):
            return f"Sell {self.symbol} , {self.sellOrders} TIicks in market {self.SYMBOL}"