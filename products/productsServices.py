import pandas_ta as ta
from products.product import Products 
import pandas as pd
from functools import cache
import time
from datetime import datetime

class ProductsServices:  
    def __init__(self, mt5, timeFrame, ASSET, HOURSSTART):
        self.mt5 = mt5
        self.Products = Products(self.mt5, timeFrame, ASSET, HOURSSTART)
        self.pd = pd
       
    def toTimeFrame(self):
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
    
    def convertToList(self, x):
        return self.Products.convertToList(x)
                                        
    def addListDynamics(self, value):
        return self.Products.addListDynamics(value)
   
    def maxIndex(self, value, counts):
        return self.Products.maxIndex(value, counts)
        
    def lastIndex(self, value): 
        return self.Products.lastIndex(value)
    
    def dayGraph(self,  value):
        return self.Products.dayGraph(value)
        
    def dayForconvert(self):
        return self.Products.current_day()
        
    def timeSleepNow(self):
        return self.Products.timeSleepNow()

    #(mfi)volume force in buy and sell 
    def mfi(self):
        highNotConv = self.selectBar('high')
        high = pd.to_numeric(highNotConv, downcast='float')
        closeNotConv = self.selectBar('low')
        close = pd.to_numeric(closeNotConv, downcast='float') 
        mfiDataFrame = ta.mfi(high,closeNotConv,
                            self.selectBar('close'), self.selectBar('real_volume'))
        return mfiDataFrame
    
    def ad(self):
        adData = ta.ad(self.selectBar('high'), self.selectBar('low')
                       , self.selectBar('close'),  self.selectBar('real_volume'))
        return adData
    
    def eom(self):
        eomData = ta.eom(self.selectBar('high'), self.selectBar('low')
                       , self.selectBar('close'),  self.selectBar('real_volume') )
        return eomData
    
    def teste(self):
        help(ta.eom)
    
    #Beta  
    def calcV(self):
        calc = True
        before = []
        v = []
        futureNegative = []
        futurePositive = [] 
        while calc :
            before.append(float(self.selectBar('close')))
            for first in len(before):
                if first >= (first * 2):  
                    futurePositive.append(float(self.selectBar('close')))
                elif first <= (first * 2):
                    futureNegative.append(before)
            v = list(filter(lambda n : n < n * 0,8 , futurePositive))
            v = list(filter(lambda n : n > n * 0,8 , futureNegative))
            if len(v) > 1 :
                print(v)
                calc = False