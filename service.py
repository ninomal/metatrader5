
#Services
class Service():
    def __init__(self, mt5, SYMBOL):
        self.mt5 = mt5
        self.SYMBOL = SYMBOL
    
    def symbol(self):
        symbol_info_tick_dict = self.mt5.symbol_info_tick(self.SYMBOL)
        return symbol_info_tick_dict
    
        
    def buy():
        pass
    
    
    def sell():
        pass
    
    def __repr__(self) -> str:
        if(buy != 0):
            return f"Buy {self.symbol} market {self.SYMBOL}"
        elif(sell != 0):
            return f"Sell {self.symbol} market {self.SYMBOL}"