# implments volume in matplot basead in mt5 
import pandas as pd
import time
from datetime import datetime

ATIVO = "WINV23" #name of market
POS = 0  #position bar
COUNT = 0 #position count 

class Products:
    def __init__(self, mt5):
        self.mt5 = mt5
        self.TIMEFRAME = self.mt5.TIMEFRAME_M1
        self.COUNT = COUNT
        self.SYMBOL = ATIVO
        self.POS = POS
        self.daTime = self.dateTime()        
        self.dados = self.colectDate()
        
    
    def convertDateHour(self, df):
        df['time'] = pd.to_datetime(df['time'], unit ='s')
        return df
    
    def colectDate(self, count = 0):
        date =self.mt5.copy_rates_from_pos(self.SYMBOL,self.TIMEFRAME, self.POS, count)
        dateDf = pd.DataFrame(date)
        dateConvDf = self.convertDateHour(dateDf)
        return dateConvDf
                
    def dateTime(self):
        named_tuple = time.localtime() 
        timeframe = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        return timeframe

    def lastBar(self):
        lastBarDF = self.colectDate()
        lastBarDFa = lastBarDF.iloc[-1]
        return lastBarDFa
        
    def selectBar(self, name):
        bar = self.lastBar()
        select = bar[name]
        selectConv = self.to_numerics(select)
        print(selectConv)
        return selectConv     
        
    def to_numerics(self, series):
        seriesConv = pd.to_numeric(series, downcast='float')
        return seriesConv
        
        
