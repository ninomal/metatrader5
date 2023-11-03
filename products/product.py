# implments volume in matplot basead in mt5 
import pandas as pd
import time
from datetime import datetime
from functools import cache

ATIVO = "WINZ23" #name of market
POS = 0  #position bar
COUNT = 0 #position count 

class Products:
    def __init__(self, mt5, timeframe):
        self.mt5 = mt5
        self.TIMEFRAME = timeframe
        self.COUNT = COUNT
        self.SYMBOL = ATIVO
        self.POS = POS
        self.daTime = self.dateTime()        
        self.dados = self.colectDate()
        
    def convertDateHour(self, df):
        df['time'] = pd.to_datetime(df['time'], unit ='s')
        return df

    @cache
    def colectDate(self, count = 0):
        date =self.mt5.copy_rates_from_pos(self.SYMBOL,self.TIMEFRAME, self.POS, count)
        dateDf = pd.DataFrame(date)
        dateConvDf = self.convertDateHour(dateDf)
        #dateConvDf.set_index('time', inplace=True) 
        return dateConvDf 
    
    def tOtimeFrame(self):
        df = pd.DataFrame(self.colectDate())
        df['time'] = df['time']
        print(df['time'])
        return df
    @cache           
    def dateTime(self):
        named_tuple = time.localtime() 
        timeframe = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        return timeframe
    @cache
    def lastBar(self):
        lastBarDF = self.dados
        lastBarDFa = lastBarDF.iloc[-1]
        return lastBarDFa
        
    def selectBar(self, name):
        bars = self.colectDate()
        select = bars[name]
        selectConv = self.to_numerics(select)
        return selectConv     
   
    def to_numerics(self, series):
        seriesConv = pd.to_numeric(series, downcast='float')
        return seriesConv
        
    
