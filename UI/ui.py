import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from products.productsServices import ProductsServices
from functools import cache
from datetime import datetime
import time

class UI(ProductsServices):
    def __init__(self, mt5):
        super().__init__(mt5)
        self.dataframe = self.priceVol()
        self.time = self.dataTime()
        self.pvol = self.dataPvol() 
        self.POSITION = range(0, 50)
        self.conts = 1
               
    def dataTime(self):
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        time = self.convertToList(dfindex['time'])
        return time
    
    def dataPvol(self):
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        pvol = self.convertToList(dfvalues['PVOL'])
        return pvol
          
    #on Dynamic ui  
    def uiBar(self, pvol, time):          
        plt.cla()
        plt.clf()              
        self.showGraphBar(self.POSITION, pvol, time)
        plt.pause(2)        
               
    def redBar(self, x, sort):
        maxLen = len(sort)
        reList = []
        for number in x:
            if number != sort[maxLen -1]:
                reList.append(0)
            else:
                reList.append(number)
        return reList
       
    def showGraphBar(self, position , pvol, time): 
        plt.bar(position, pvol, width= 0.4) 
        self.redBarGraph(pvol, position)   
        plt.xticks(position, time, rotation = 90)
        plt.title('Volume graph')      
            
    def redBarGraph(self, pvol, position):
        pvolSorted = sorted(pvol)
        redbar = self.redBar(pvol, pvolSorted) 
        plt.bar(position, redbar, color = 'red', width = 0.4)
        plt.yticks(pvol)
    
    @cache
    def lastGraph(self, switch):
        if switch == 'true':
            plt.subplots(layout='constrained', figsize = (50 , 6)) 
            plt.ion() 
            pvols = self.lastIndex(self.pvol)
            times = self.lastIndex(self.time)
            plt.cla()
            plt.clf()
            self.uiBar(pvols, times)
            plt.ioff()   
            plt.show()
        else:
            pvols = self.lastIndex(self.pvol)
            times = self.lastIndex(self.time)
            plt.cla()
            plt.clf()
            self.uiBar(pvols, times)
        
    @cache   
    def dynamicsGraph(self):
        plt.ion()
        plt.subplots(layout='constrained', figsize = (50 , 6)) 
        pvols = self.addListDynamics(self.pvol)
        times = self.addListDynamics(self.time) 
        self.uiBar(pvols, times)
        plt.ioff()   
        plt.show()
    
    #fix data input
    @cache 
    def allGraph(self):
        plt.subplots(layout='constrained', figsize = (50 , 6))
        maxindex = (len(self.pvol) /50) 
        plt.ion() 
        if maxindex < 1:
           pvols = self.addListDynamics(self.pvol)
           times = self.addListDynamics(self.time)
           self.uiBar(pvols, times)
        else:
            while self.conts < maxindex:
                pvols = self.maxIndex(self.pvol, self.conts)
                times = self.maxIndex(self.time, self.conts)
                self.uiBar(pvols, times)
                self.conts +=1
            self.lastGraph('off')
        plt.ioff()   
        plt.show()
    
    @cache    
    def graphIntraDay(self):
        plt.subplots(layout='constrained', figsize = (50 , 6))
        maxindex = (((len(self.pvol))-self.dayForconvert()) /50) - 2
        print(maxindex)
        plt.ion() 
        if maxindex < 1:
            pvols = self.dayGraph(self.pvol)
            times = self.dayGraph(self.time)
            self.uiBar(pvols, times)
        else:
            while self.conts < maxindex:
                pvols = self.maxIndex(self.pvol, self.conts)
                times = self.maxIndex(self.time, self.conts)
                self.uiBar(pvols, times)
                self.conts +=1
                print(self.conts)
            self.lastGraph('off')
        plt.ioff()   
        plt.show()
         
    def minutesInGraph(self):
        dateTime = datetime.now()
        while self.conts != 60:
            timeSecond = 60.0 - dateTime.second 
            self.lastGraph('true')
            time.sleep(timeSecond)
            self.conts += 1
            
            
        
        
        
        
            