
#Services
class Service():
    def __init__(self, mt5, SYMBOL):
        self.mt5 = mt5
        self.SYMBOL = SYMBOL
    
    def symbol(self):
        symbol_info_tick_dict = self.mt5.symbol_info_tick(self.SYMBOL)
        
    def buy():
        pass
    
    def sell():
        pass