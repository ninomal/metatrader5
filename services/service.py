ATIVO = "WINV23" #name of market
VOLUME = 1.0 #volume observe compatibility volume error change for 1.0 Demo version
ONDAS = 20
MAGIC = 12345
ONDAS_BOLINGER = 20
STANDER_DEVIATIONS = 2
TL_SD = 2
SL_SD = 2
BUY_SELL_STOP = 50
DEVIATION = 0

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
    
    def buy(self):
        preco = self.mt5.symbol_info_tick(ATIVO).ask
        pontos = self.mt5.symbol_info(ATIVO).point
        print(preco)
        request = ({
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": ATIVO,
            "volume": VOLUME,
            "type": self.mt5.ORDER_TYPE_BUY,
            "price": preco,
            "deviation":DEVIATION,
            "sl": preco - BUY_SELL_STOP * pontos,
            "tp":preco + BUY_SELL_STOP * pontos,
            "magic": MAGIC,
            "comment": "python script buy",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_RETURN
        })
        self.mt5.order_send(request)
        result = self.mt5.order_send(request)
        self.buyOrders += 1
        print(result)

    def sell(self):
        preco = self.mt5.symbol_info_tick(ATIVO).bid
        pontos = self.mt5.symbol_info(ATIVO).point
        request = ({
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": ATIVO,
            "volume": VOLUME,
            "type": self.mt5.ORDER_TYPE_SELL,
            "price": preco,
            "deviation": DEVIATION,
            "sl": preco + BUY_SELL_STOP * pontos,
            "tp":preco - BUY_SELL_STOP * pontos,
            "magic": MAGIC,
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
            return f"Sell {self.symbol}, {self.sellOrders} Ticks in market {self.SYMBOL}"