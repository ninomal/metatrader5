import pandas_ta as ta
from products.product import Products 
import pandas as pd
from functools import cache
import time
from datetime import datetime
from Ai.AiColect import AiColect

class ProductsServices:  
    def __init__(self, mt5, timeFrame, ASSET, HOURSSTART):
        self.mt5 = mt5
        self.Products = Products(self.mt5, timeFrame, ASSET, HOURSSTART)
        self.pd = pd
        self.futureNegative = 0
        self.futurePositive = 0
        self.positive = False
        self.negative = False
        self.aiColect = AiColect()

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
      
    def copyFromRates(self, mt5, asset, enumsFrame, rangeStart, rangeStop):
        copyRatesRange = self.Products.copyFromRates(mt5, asset, enumsFrame, 
                            rangeStart, rangeStop)   
        return copyRatesRange
          
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
    
    # calcv call method
    def calcVfunc(self):
        for i in range(1000):
            calc = self.convertToList(self.lastbar()) 
            self.calcV(calc)
            self.timeSleepNow()
        
    #Beta  calcV method
    def calcV(self, data):
        if self.futureNegative == 0:
            self.futurePositive = data +  ((data * 0.69)/100)
            self.futureNegative = (data - (data * 0.69)/100)
        elif data < self.futurePositive and self.positive:
            self.aiColect.colectID("Buy", self.futurePositive, data , "none",
                             data, "Calcv", "why") #Ai 
            self.futurePositive = 0
            self.positive = False
            return True
        elif data > self.futureNegative and self.negative: 
            self.aiColect.colectID("Sell", self.futurePositive, "none" , data , 
                            data,"Calcv", "why") #Ai 
            self.futureNegative = 0
            self.negative = False  
            return True      
        elif data > self.futurePositive:
            if self.positive == False:
                self.futurePositive = (data - (data * 0.48)/100)
                self.positive = True
                self.aiColect.colectID("Buy", self.futurePositive, data,
                            "none","none", "Calv","how") #Ai
        elif data < self.futureNegative:
            if self.negative == False:
                self.futureNegative = (data + (data* 0.48)/100)
                print(self.futureNegative)
                self.negative = True
                self.aiColect.colectID("Sell", self.futureNegative, "none",
                            data,"none", "Calv","how") #Ai
                
                           
   