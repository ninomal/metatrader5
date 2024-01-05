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