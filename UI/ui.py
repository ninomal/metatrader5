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
        plt.pause(20)        
               
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
    def allRedBar(self):
        plt.subplots(layout='constrained', figsize = (50 , 6))
        pvolSorted = self.sortedRedBar()
        pvolSliced = pvolSorted[:50]
        timeDic = self.convertToDic(self.pvol, self.dataTime())
        timeSorted = list(map(lambda n : timeDic[n] , pvolSliced))
        self.uiBar(pvolSliced, timeSorted)
    
    @cache   
    def sortedRedBar(self):
        pvols = self.pvol
        pvolSorted = sorted(pvols, reverse= True)
        return pvolSorted
      
    def convertToDic(self, pvols , times):
        sortedDic = self.convertToDictLam(pvols, times)
        return sortedDic
              
    def convertToDictLam(self, list, list2):
        res_dct = map(lambda i: (list[i], list2[i]), range(len(list))[::])
        return dict(res_dct)
    
    def sortedRedBarIntraday(self):
        plt.subplots(layout='constrained', figsize = (50 , 6))
        maxindex = (((len(self.pvol))-self.dayForconvert()) /50) - 3
        totalFrame = (len(self.pvol) /50) 
        index = self.dayForconvert()
        plt.ion() 
        if (len(self.pvol) - index) <1:
            print("autoes")
            pass
        elif maxindex < totalFrame :
            while self.conts > maxindex:
                teste = index +50
                pvolsNotConv = self.pvol[index:teste]
                print(len(pvolsNotConv))
                print(pvolsNotConv)
                pvolsSorted = sorted(pvolsNotConv, reverse=True)
                print(pvolsSorted)
                timeDic = self.convertToDic(self.pvol, self.dataTime())
                timeSorted = list(map(lambda n : timeDic[n] , pvolsSorted))
                print(pvolsSorted)
                print("bbbb")
                print(pvolsNotConv)
                self.uiBar(pvolsSorted, timeSorted)
                self.conts +=1
            self.lastGraph('off')
        else:
            while self.conts == 50:
                pass
        plt.ioff()   
        plt.show()
      
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
        maxindex = (((len(self.pvol))-self.dayForconvert()) /50) - 3
        totalFrame = (len(self.pvol) /50) 
        plt.ion() 
        if maxindex < 1:
            self.minutesInGraph()
        elif maxindex < totalFrame:
            while self.conts < maxindex:
                pvols = self.maxIndex(self.pvol, self.conts)
                times = self.maxIndex(self.time, self.conts)
                self.uiBar(pvols, times)
                self.conts +=1
            self.lastGraph('off')
        else:
            self.minutesInGraph()
        plt.ioff()   
        plt.show()
         
    def minutesInGraph(self):
        dateTime = datetime.now()
        while self.conts != 60:
            timeSecond = 60.0 - dateTime.second 
            self.lastGraph('true')
            time.sleep(timeSecond)
            self.conts += 1
            
    
            
        
        
        
        
            