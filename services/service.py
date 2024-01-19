from enums import enumsTime
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
    def __init__(self, mt5, timeFramesStr):
        self.mt5 = mt5
        self.timeFramesStr = timeFramesStr
        self.TIMEFRAME = self.enumsTimeProducts()
        self.buyOrders = 0
        self.sellOrders = 0
        
    def enumsTimeProducts(self):
        enumsTimeIns = enumsTime.Timeframe(self.mt5, self.timeFramesStr)
        enumsTimeProduct = enumsTimeIns.timeSelect()
        return enumsTimeProduct  
    
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
        self.sellOrders += -1
        self.mt5.rates_total()
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
        
    def orders(self):   
        orders= self.buyOrders + self.sellOrders
        if orders!= 0:
            print("Total orders=",orders)
        else:
            print("Orders not found")
            
        