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
        maxindex = (((len(self.pvol))-self.dayForconvert()) /50) - 1
        totalFrame = (len(self.pvol) /50) 
        firstFifty = 0
        index = self.dayForconvert()
        indexPlus = index + 50
        plt.ion() 
        if (len(self.pvol) - index) <50:
            while firstFifty != 50:
                pvolsNull = self.pvol[index:indexPlus]
                print(len(pvolsNull))
                pvolsNotConv = self.addListDynamics(pvolsNull)
                pvolsSorted = sorted(pvolsNotConv, reverse=True)
                timeDic = self.convertToDic(self.pvol, self.dataTime())
                pvolsSortedFilter = list(filter(lambda n : n != 0 , pvolsSorted))
                timeSorted = list(map(lambda n : timeDic[n] , pvolsSortedFilter))
                dateTime = datetime.now()
                minuts = 50 - dateTime.minute 
                for i in range(minuts):
                    print(i)
                    timeSorted.append(0)
                self.uiBar(pvolsSorted, timeSorted)
                self.timeSleepNow()
                index = self.dayForconvert()
                indexPlus = index + 50
                firstFifty += 1
        elif maxindex < totalFrame :
            while self.conts != 20:
                indexPlus = index +50
                pvolsNotConv = self.pvol[index:indexPlus]
                pvolsSorted = sorted(pvolsNotConv, reverse=True)
                timeDic = self.convertToDic(self.pvol, self.dataTime())
                timeSorted = list(map(lambda n : timeDic[n] , pvolsSorted))
                self.uiBar(pvolsSorted, timeSorted)
                self.conts +=1
                self.timeSleepNow()
        else:
            print("data error")
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
    
    #graph dynamic with redBar
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
    #calc minuts in real time    
    def minutesInGraph(self):
        dateTime = datetime.now()
        while self.conts != 60:
            timeSecond = 60.0 - dateTime.second 
            self.lastGraph('true')
            time.sleep(timeSecond)
            self.conts += 1
     
    #colect data im mfi dict convert in list       
    def PizzaGraphData(self):
        mfiData = self.mfi()
        dataFrame = mfiData.to_frame()
        data = dataFrame.to_dict()
        labels = "Buy", "Sell"
        colors = ["#0000ff","#FF0000"]
        valueBuy =[]
        valueSell = [] 
        size = []
        for i in range(len(dataFrame)):
            if data["MFI_14"][i] > 50.01:
                valueBuy.append(data["MFI_14"][i])
            elif data["MFI_14"][i] <= 50.00:
                valueSell.append(data["MFI_14"][i])
            else :
                pass
        sell = (sum(valueSell))/1000
        buy = (sum(valueBuy))/1000
        size.append(buy)
        size.append(sell)
        plt.cla()
        plt.clf()
        self.PizzaGraphUI( size, labels, colors)
        valueBuy.clear()
        valueSell.clear()
        size.clear()
    
    #set Pizza graph colors and params  
    def PizzaGraphUI(self, date, labels, colors):
        plt.pie(date, labels = labels, autopct = "%1.1f%%", 
                shadow = True, startangle= 90, colors = colors)
        plt.suptitle("Pizza volume graph")
        plt.axis('on')
        
    def PizzaGraphForce(self):
        maxindex = ((len(self.pvol)) /50)
        plt.subplot()
        plt.ion() 
        while self.conts < maxindex:
            dateTime = datetime.now()
            timeSecond = 60.0 - dateTime.second
            self.PizzaGraphData() 
            plt.pause(timeSecond)
            self.conts += 1
        plt.ioff()   
        plt.show()
        
    def adGraphData(self):
        plt.subplots(layout='constrained', figsize = (50 , 6))
        ad = self.ad()
        maxindex = (((len(self.pvol))-self.dayForconvert()) /50) - 1
        totalFrame = (len(self.pvol) /50) 
        firstFifty = 0
        index = self.dayForconvert()
        indexPlus = index + 50
        adList = []
        plt.ion() 
        if (len(self.pvol) - index) <50:
            plt.ion()
            while firstFifty != 50:
                adSlice = ad[index:indexPlus]
                pvolTime = self.pvol[index:indexPlus]
                print(len(adSlice))
                for x in adSlice:
                        adList.append(x)    
                timeDic = self.convertToDic(pvolTime, self.dataTime())
                timeList= list(map(lambda n : timeDic[n] , timeDic))
                dateTime = datetime.now()
                minuts = 50 - dateTime.minute 
                x = len(adSlice)
                for x in range(minuts-1):
                    print(x)
                    timeList.append(0)
                    adList.append(0)
                self.adGraph(adList, timeList)
                index = self.dayForconvert()
                indexPlus = index + 50
                firstFifty += 1
        elif maxindex < totalFrame :
            while self.conts != 20:
                timeDic = self.convertToDic(self.pvol, self.dataTime())
                timeList = list(map(lambda n : timeDic[n] , timeDic))
                timeIndex = timeList[index:indexPlus]
                adIndex = ad[index:indexPlus]
                self.adGraph(adIndex, timeIndex)
                self.conts +=1
                index = self.dayForconvert()
                indexPlus = index + 50
        else:
            print("data error")
        plt.ioff()   
        plt.show()
           
    def adGraph(self, data, time):
        plt.clf()
        plt.cla()
        plt.scatter(self.POSITION,data)
        plt.xticks(self.POSITION, time, rotation = 90)    
        plt.plot(self.POSITION, data)
        plt.yticks(data)
        plt.title('AD graph') 
        plt.pause(3)
        
            