class Timeframe():
    def __init__(self, mt5, timeframe):
        self.time = timeframe
        self.mt5 = mt5
      
    def timeSelect(self): 
        if self.time == '2':
            return self.mt5.TIMEFRAME_M2
        elif self.time == '3':
            return self.mt5.TIMEFRAME_M3 
        elif self.time == '4':
            return self.mt5.TIMEFRAME_M4 
        elif self.time == '5':
            return self.mt5.TIMEFRAME_M5 
        elif self.time == '6':
            return self.mt5.TIMEFRAME_M6 
        elif self.time == '10':
            return self.mt5.TIMEFRAME_M10 
        elif self.time == '12':
            return self.mt5.TIMEFRAME_M12 
        elif self.time == '15':
            return self.mt5.TIMEFRAME_M15 
        elif self.time == '20':
            return self.mt5.TIMEFRAME_M20 
        elif self.time == '30':
            return self.mt5.TIMEFRAME_M30
        elif self.time == '1h':
            return self.mt5.TIMEFRAME_H1 
        elif self.time == "2h":
            return self.mt5.TIMEFRAME_H2 
        elif self.time == "1d":
            return self.mt5.TIMEFRAME_D1 
        elif self.time == "2d":
            return self.mt5.TIMEFRAME_D2
        elif self.time == "1w":
            return self.mt5.TIMEFRAME_W1 
        elif self.time == "1mon":
            return self.mt5.TIMEFRAME_MN1 
        else:
            return self.mt5.TIMEFRAME_M1   #Standard
        