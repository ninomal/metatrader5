import pandas_ta as ta
from products.product import Products 
import pandas as pd

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
    def priceVol(self):
        pricevol = ta.pvol(self.selectBar('close'), self.selectBar('real_volume')) 
        pricevolConv = pd.DataFrame(pricevol)
        return pricevolConv
    
    #last bar in market
    def lastbar(self):
        bar = self.Products.lastBar()
        return bar
    
    #convert dataframe in list eficient 
    def convertToList(self, x, y, value = 'b'):
        lens = 0
        xlist = []
        ylist = []
        while len(x) != lens:
            xlist.append( x.loc[lens])
            ylist.append( y.loc[lens])
            lens +=1
        if value == 'x':
            return xlist
        elif value == 'y':
            return ylist
       
    def cutListHour(self, value, index = 1):
        if len(value) > 51:
            maxindex = self.maxIndex(value, index)
            return maxindex
        elif len(value) >= 50:
            value = value[:50]
            return value
        elif len(value) < 50:
            newList = self.addListDynamics(value)
            return newList
                                
    def addListDynamics(self, value = 0):
        dynamycList = [] 
        for new in range(50):
            if value == 0:
                dynamycList.append(value)
            else:
                dynamycList = self.newList(value)
        return dynamycList
    
    # transform new list '0''0' ind value 'value' '0'
    def newList(self, value, counts= 0):
        newlist = []
        newlist.append(value)
        maxLen = len(newlist)
        if counts == 0:
            while maxLen <= 50 :
                newlist.append(0)
                maxLen += 1
            counts +=1
        return newlist
    
    # def max range not allow counts = '0'         
    def maxIndex(self, value, counts):
        index = 50
        maxindex = index * counts 
        base = maxindex - 50
        values = value[base: maxindex]
        print('index')
        print(maxindex,  base)
        return values
        
     