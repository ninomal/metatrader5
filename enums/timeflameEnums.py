TIMEFRAME_M1 = str# 1 minute
TIMEFRAME_M2 = str# 2 minutes
TIMEFRAME_M3 = str#3 minutes
TIMEFRAME_M4 = str#4 minutes
TIMEFRAME_M5 = str #5 minutes
TIMEFRAME_M6 = str #6 minutes
TIMEFRAME_M10 = str #10 minutes
TIMEFRAME_M12 = str #12 minutes
TIMEFRAME_M15 = str  #15 minutes
TIMEFRAME_M20 = str #20 minutes
TIMEFRAME_M30 = str #30 minutes
TIMEFRAME_H1 = str #1 hour
TIMEFRAME_H2 = str #2 hours
TIMEFRAME_H3 = str #3 hours
TIMEFRAME_H4 = str #4 hours
TIMEFRAME_H6 = str #6 hours
TIMEFRAME_H8 = str #8 hours
TIMEFRAME_H12 = str #12 hours
TIMEFRAME_D1 = str #1 day
TIMEFRAME_W1 = str #1 week
TIMEFRAME_MN1 = str #1 month

class TimeFrame:
    def __init__(self, time):
        self.time = time
        
    
    def timeframe(self):
        if self.time == 1:
            return TIMEFRAME_M1 
        elif self.time == 2:
            return TIMEFRAME_M2 
        elif self.time == 3:
            return TIMEFRAME_M3 
        elif self.time == 4:
            return TIMEFRAME_M4 
        elif self.time == 5:
            return TIMEFRAME_M5 
        elif self.time == 6:
            return TIMEFRAME_M6 
        elif self.time == 10:
            return TIMEFRAME_M10 
        elif self.time == 12:
            return TIMEFRAME_M12 
        elif self.time == 15:
            return TIMEFRAME_M15 
        elif self.time == 20:
            return TIMEFRAME_M20 
        elif self.time == 30:
            return TIMEFRAME_M30 
        elif self.time == 60:
            return TIMEFRAME_H1 
        elif self.time == "2h":
            return TIMEFRAME_H2 
        elif self.time == "3h":
            return TIMEFRAME_H3 
        elif self.time == "4h":
            return TIMEFRAME_H4 
        elif self.time == "6h":
            return TIMEFRAME_H6 
        elif self.time == "8h":
            return TIMEFRAME_H8 
        elif self.time == "12h":
            return TIMEFRAME_H12 
        elif self.time == "1d":
            return TIMEFRAME_D1 
        elif self.time == "2d":
            return TIMEFRAME_W1 
        elif self.time == "3d":
            return TIMEFRAME_MN1 