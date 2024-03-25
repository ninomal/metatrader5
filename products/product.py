# implments volume in matplot basead in mt5 
import pandas as pd
import time
from datetime import datetime
from functools import cache
from enums import enumsTime
import os

POS = 0  #position bar
COUNT = 0 #position count 

class Products:
    def __init__(self, mt5, timeFramesStr, ASSET, HOURSSTART):
        self.mt5 = mt5
        self.timeFramesStr = timeFramesStr
        self.TIMEFRAME = self.enumsTimeProducts()
        self.COUNT = COUNT
        self.SYMBOL = ASSET
        self.POS = POS
        self.daTime = self.dateTime()        
        self.dados = self.colectDate()
        self.HOURSSTART = HOURSSTART
        self.listOfImage = []
        self.imageCount = 0
        
    def enumsTimeProducts(self):
        enumsTimeIns = enumsTime.Timeframe(self.mt5, self.timeFramesStr)
        enumsTimeProduct = enumsTimeIns.timeSelect()
        return enumsTimeProduct
        
    def convertDateHour(self, df):
        df['time'] = pd.to_datetime(df['time'], unit ='s')
        return df

    def colectDate(self, count = 0):
        date =self.mt5.copy_rates_from_pos(self.SYMBOL,self.TIMEFRAME, self.POS, count)
        dateDf = pd.DataFrame(date)
        dateConvDf = self.convertDateHour(dateDf)
        #dateConvDf.set_index('time', inplace=True) 
        return dateConvDf 
    
    def tOtimeFrame(self):
        df = pd.DataFrame(self.colectDate())
        df['time'] = df['time']
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
        #selectConv = self.to_numerics(select)
        return select    
   
    def to_numerics(self, series):
        seriesConv = pd.to_numeric(series, downcast='float')
        return seriesConv
           
    def date_of_Day(self):
        named_tuple = time.localtime()
        timeDay = time.strftime("%Y-%m-%d", named_tuple)
        return timeDay
           
    def current_day(self):
        if self.HOURSSTART != '':
            day = self.date_of_Day()
            times = self.selectBar('time')
            day_raw = times.where(times== (day+ " " + self.HOURSSTART)).dropna()
            day_nowList = day_raw.axes
            day_now = day_nowList[0][0]
            day_now_conv = day_now.item()
            print(day_now_conv)
            return day_now_conv
    
    #time seconds calculator
    @cache
    def timeSleepNow(self):
        dateTime = datetime.now()
        timeSecond = 60.0 - dateTime.second 
        time.sleep(timeSecond)
        
    def dayGraph(self,  value):
        day = self.current_day()  
        index = 50
        maxindex = index + day
        values = value[day: maxindex]
        return values
    
    #slice max index grafics
    def lastIndex(self, value): 
        maxindex = len(value)
        base = maxindex - 50
        values = value[base: maxindex]
        return values
       
    # def max range not allow counts = '0'   
    def maxIndex(self, value, counts):
        index = 50
        maxindex = index * counts 
        base = maxindex - 50
        values = value[base: maxindex]
        return values
       
    # for start day in graph                              
    def addListDynamics(self, value):
        dynamycList = [] 
        for new in range(50):
            if  new  < (len(value) -1):
                dynamycList.append(value[new])
            else:
                dynamycList.append(0)
        return dynamycList
    
    #convert dataframe in list eficient 
    def convertToList(self, x):
        lens = 0
        xlist = []
        while len(x) != lens:
            xlist.append( x.loc[lens])
            lens +=1 
        return xlist
    
    def defineSleep(self, value):
        time.sleep(value)
     
    # define name of screenShoot to send watssap path   
    def hoursImgName(self):
        time = self.dateTime()
        newTime = ""
        for times in time:
            if times[0] == "/" or times[0] == "," or times[0] == ":":
                newTime += " "
            elif times[0]== " " :
                newTime+=""
            else:
                newTime += times[0]
        newTime += ".png"
        self.listOfImage.append(newTime)
        return newTime
     
    def colectDataMpf(self, count = 0):
        date =self.mt5.copy_rates_from_pos(self.SYMBOL,self.TIMEFRAME, self.POS, count)
        dateDf = pd.DataFrame(date)
        dateDfslice = dateDf.iloc[950: 1000]
        ateConvDf = self.convertDateHour(dateDfslice)
        dataConv = pd.DataFrame(ateConvDf)
        dataConv = dataConv.set_index('time')
        dataConv.shape
        dataConv.head(3)
        dataConv.tail(3)
        return dataConv
    
    #for delete img afeter sending
    def deleteImg(self, path):
        os.remove(path)
        
    def copyFromDate(self, asset, enumsFrame, dateStart, dateStop):
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        if not self.mt5.initialize():
            print("initialize() failed, error code =",self.mt5.last_error())
            quit() 
        rates = self.mt5.copy_rates_from_pos(f"{asset}", enumsFrame, dateStart, dateStop)
        print("Display obtained data 'as is'")
        for rate in rates:
            print(rate)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        print("\nDisplay dataframe with data")
        print(rates_frame) 
        return rates_frame
        