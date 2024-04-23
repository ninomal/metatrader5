class Timeframe():
    def __init__(self, mt5, timeframe):
        self.time = timeframe
        self.mt5 = mt5
      
    def timeSelect(self): 
        match self.time:
            case "1":
                return self.mt5.TIMEFRAME_M1   #Standard
            case'2':
                return self.mt5.TIMEFRAME_M2
            case '3':
                return self.mt5.TIMEFRAME_M3 
            case '4':
                return self.mt5.TIMEFRAME_M4 
            case '5':
                return self.mt5.TIMEFRAME_M5 
            case '6':
                return self.mt5.TIMEFRAME_M6 
            case '10':
                return self.mt5.TIMEFRAME_M10 
            case '12':
                return self.mt5.TIMEFRAME_M12 
            case '15':
                return self.mt5.TIMEFRAME_M15 
            case '20':
                return self.mt5.TIMEFRAME_M20 
            case '30':
                return self.mt5.TIMEFRAME_M30
            case '1h':
                return self.mt5.TIMEFRAME_H1 
            case "2h":
                return self.mt5.TIMEFRAME_H2 
            case "1d":
                return self.mt5.TIMEFRAME_D1 
            case "2d":
                return self.mt5.TIMEFRAME_D2
            case  "1w":
                return self.mt5.TIMEFRAME_W1 
            case "1mon":
                return self.mt5.TIMEFRAME_MN1 
            case _:
                return print("Error time")
            
            