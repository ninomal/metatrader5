import pandas_ta as ta
from products.product import Products 
import pandas as pd

class ProductsServices:
       
    def __init__(self, mt5):
        self.mt5 = mt5
        self.Products = Products(self.mt5)
        
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
        #df['media'] = df['PVOL'].rolling(2).mean()
        #print(df.iloc[1])
        print(pricevolConv.index)
        return pricevolConv
    
    def lastbar(self):
        bar = self.Products.lastBar()
        return bar
    
    def maxLength(self, x):
        maxlen = 10
        if maxlen < x.lenght:
            maxlen = maxlen * 2
        return maxlen
    
    def convertToList(self, x , y):
        lens = 0
        while x.lenght != lens:
            x[lens] = x.iloc[lens]
            y[lens] = y.iloc[lens]
            lens +=1
        return x, y
        
            