
import matplotlib as plt
import pandas_ta as ta
from products.product import Products 
import pandas as pd

class ProductsServices:
       
    def __init__(self, mt5):
        self.mt5 = mt5
        self.Products = Products(self.mt5)
        
        
    def selectBar(self, valor):
        bar = self.Products.selectBar(valor)
        return bar
        
    def calcAMV(self):
        media = ta.midprice(self.selectBar('open'), self.selectBar('close'), 20, 0 , 0 )
        print(media)
        
        
    def calcEma(self):
        mov = ta.ema(self.selectBar('close'), length=10)
        print(mov)
        
     
    #fixing  
    def vwap(self):
        vol = ta.vwap(self.selectBar('high'), self.selectBar('low'), 
              self.selectBar('close'), self.selectBar('real_volume'), anchor= 'W')
        print("volume")
        print(vol)
    
    #Accumulation/Distribution Index
    def adv(self):
        adVol = ta.ad(self.selectBar('high'), self.selectBar('low'), 
              self.selectBar('close'), self.selectBar('real_volume'),
              self.selectBar('open'), talib=False )
        print(adVol)
        
    
