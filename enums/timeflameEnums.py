#TIMEFRAME_M1 =str# 1 minute
#TIMEFRAME_M2 = str# 2 minutes
#TIMEFRAME_M3 = str# 3 minutes
#TIMEFRAME_M4 = str# 4 minutes
#TIMEFRAME_M5 = str# 5 minutes
#TIMEFRAME_M6 = str# 6 minutes
#TIMEFRAME_M10 =str# 10 minutes
#TIMEFRAME_M12 =str# 12 minutes
#TIMEFRAME_M15 =str# 15 minutes
#TIMEFRAME_M20 =str# 20 minutes
#TIMEFRAME_M30 =str# 30 minutes
#TIMEFRAME_H1 =str#  1 hour
#TIMEFRAME_H2 =str#  2 hours
#TIMEFRAME_H3 =str#  3 hours
#TIMEFRAME_H4 =str#  4 hours
#TIMEFRAME_H6 =str#  6 hours
#TIMEFRAME_H8 =str#  8 hours
#TIMEFRAME_H12 =str# 12 hours
#TIMEFRAME_D1 =str#  1 day
#TIMEFRAME_W1 =str#  1 week
#TIMEFRAME_MN1 =str# 1 month

class TimeFrame:
    def __init__(self, time, mt5):
        self.time = time
        self.mt5 = mt5
        
    
    def timeframe(self):
        if self.time == 1:
            return self.mt5.TIMEFRAME_M1 
        elif self.time == 2:
            return self.mt5.TIMEFRAME_M2 
        elif self.time == 3:
            return self.mt5.TIMEFRAME_M3 
        elif self.time == 4:
            return self.mt5.TIMEFRAME_M4 
        elif self.time == 5:
            return self.mt5.TIMEFRAME_M5 
        elif self.time == 6:
            return self.mt5.TIMEFRAME_M6 
        elif self.time == 10:
            return self.mt5.TIMEFRAME_M10 
        elif self.time == 12:
            return self.mt5.TIMEFRAME_M12 
        elif self.time == 15:
            return self.mt5.TIMEFRAME_M15 
        elif self.time == 20:
            return self.mt5.TIMEFRAME_M20 
        elif self.time == 30:
            return self.mt5.TIMEFRAME_M30 
        elif self.time == 60:
            return self.mt5.TIMEFRAME_H1 
        elif self.time == "2h":
            return self.mt5.TIMEFRAME_H2 
        elif self.time == "3h":
            return self.mt5.TIMEFRAME_H3 
        elif self.time == "4h":
            return self.mt5.TIMEFRAME_H4 
        elif self.time == "6h":
            return self.mt5.TIMEFRAME_H6 
        elif self.time == "8h":
            return self.mt5.TIMEFRAME_H8 
        elif self.time == "12h":
            return self.mt5.TIMEFRAME_H12 
        elif self.time == "1d":
            return self.mt5.TIMEFRAME_D1 
        elif self.time == "2d":
            return self.mt5.TIMEFRAME_W1 
        elif self.time == "3d":
            return self.mt5.TIMEFRAME_MN1 