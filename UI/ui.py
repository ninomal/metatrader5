import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from products.productsServices import ProductsServices


class UI(ProductsServices):
    def __init__(self, mt5):
        super().__init__(mt5)
        self.dataframe = self.teste()
        self.conts = 4
        
    def teste(self):
        preco = self.priceVol()
        return preco
     
    def construc(self):
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        print(dfindex)
        time = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'x')
        pvol = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'y')
        #pvol = self.cutListHour(pvol)
        #time = self.cutListHour(time)
        print('aaaa') 
        print(time)
        print('cccc')
        print(pvol)
        position = range(0, 50)
        #on Dynamic ui
        plt.ion()   
        #plt.style.use('ggplot') 
        while self.conts <= 8:
            plt.cla()
            plt.clf()
            pvol = self.maxIndex(pvol, self.conts)
            time = self.maxIndex(time, self.conts)
            self.showGraphBar(position, pvol, time)
            self.conts +=1
            print("teste")
            print(self.conts)
            plt.pause(5)        
        plt.ioff()   
        plt.show()
           
    def redBar(self, x, sort):
        maxLen = len(sort)
        reList = []
        for number in x:
            if number != sort[maxLen -1]:
                reList.append(0)
            else:
                reList.append(number)
        print('ahaha')
        print(reList)
        return reList
    
    def showGraphBar(self, position, pvol, time): 
        plt.subplots(layout='constrained', figsize = (50 , 6))
        plt.bar(position, pvol, width= 0.4) 
        self.redBarGraph(pvol, position)   
        plt.xticks(position, time, rotation = 90)
        plt.title('Volume graph')      
           
    def redBarGraph(self, pvol, position):
        pvolSorted = sorted(pvol)
        redbar = self.redBar(pvol, pvolSorted) 
        plt.bar(position, redbar, color = 'red', width = 0.4)
        plt.yticks(pvol)
        #plt.yticklabels(pvolSorted)
        
   
        