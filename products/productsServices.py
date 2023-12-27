import pandas_ta as ta
from products.product import Products 
import pandas as pd
from functools import cache
import time
from datetime import datetime

class ProductsServices:
       
    def __init__(self, mt5):
        self.mt5 = mt5
        self.Products = Products(self.mt5)
        self.pd = pd
       
    def  toTimeFrame(self):
        return self.Products.tOtimeFrame()
              
    #name for dateframes func    
    def selectBar(self, valor):
        bar = self.Products.selectBar(valor)
        return bar
    
    #mid price   
    def calcAMV(self):
        media = ta.midprice(self.selectBar('open'), self.selectBar('close'), 20, 0 , 0 )
        return media
        
    #Exponential Moving Average    
    def calcEma(self):
        mov = ta.ema(self.selectBar('close'), length=10)
        return mov
          
    #fixing  
    def vwap(self):
        vol = ta.vwap(self.selectBar('high'), self.selectBar('low'), 
              self.selectBar('close'), self.selectBar('real_volume'), anchor= 'W') 
        return vol
    
    #Accumulation/Distribution Index
    def adv(self):
        adVol = ta.ad(self.selectBar('high'), self.selectBar('low'), 
              self.selectBar('close'), self.selectBar('real_volume'),
              self.selectBar('open'), talib=False )
        return adVol
    
    #Price volume
    @cache
    def priceVol(self):
        pricevol = ta.pvol(self.selectBar('close'), self.selectBar('real_volume')) 
        pricevolConv = pd.DataFrame(pricevol)
        return pricevolConv
    
    #last bar in market
    def lastbar(self):
        bar = self.Products.lastBar()
        return bar
    
    #convert dataframe in list eficient 
    def convertToList(self, x):
        lens = 0
        xlist = []
        while len(x) != lens:
            xlist.append( x.loc[lens])
            lens +=1 
        return xlist
             
    # for start day in graph                              
    def addListDynamics(self, value):
        dynamycList = [] 
        for new in range(50):
            if  new  < (len(value) -1):
                dynamycList.append(value[new])
            else:
                dynamycList.append(0)
        return dynamycList

    # def max range not allow counts = '0'      
    def maxIndex(self, value, counts):
        index = 50
        maxindex = index * counts 
        base = maxindex - 50
        values = value[base: maxindex]
        return values
        
    def lastIndex(self, value): 
        maxindex = len(value)
        base = maxindex - 50
        values = value[base: maxindex]
        return values
    
    #day graph
    def dayGraph(self,  value):
        day = self.Products.current_day()  
        index = 50
        maxindex = index + day
        values = value[day: maxindex]
        return values
        
    def dayForconvert(self):
        return self.Products.current_day()
        
    def timeSleepNow(self):
        dateTime = datetime.now()
        timeSecond = 60.0 - dateTime.second 
        time.sleep(timeSecond)

    def sortedDic(self, pvolsValue):
        pvolsSorted = sorted(pvolsValue, reverse=True)
        timeDic = self.convertToDic(self.pvol, self.dataTime())
        timeSorted = list(map(lambda n : timeDic[n] , pvolsSorted))
        return timeSorted
   