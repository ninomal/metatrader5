import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from products.productsServices import ProductsServices


class UI(ProductsServices):
    def __init__(self, mt5):
        super().__init__(mt5)
        self.dataframe = self.teste()
        self.total = 0
        self.params = 10
        
    def teste(self):
        preco = self.priceVol()
        return preco
     
    def construc(self):
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        print(dfindex)
        time = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'x')
        pvol = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'y')
        pvol = self.cutListHour(pvol)
        time = self.cutListHour(time)
        print('aaaa') 
        print(time)
        print('cccc')
        print(pvol)
        position = range(len(pvol) ) 
        print(position)
        
        fig, ax = plt.subplots(layout='constrained', figsize = (50 , 6))# Create a figure containing a single axes. 
        group1 = ax.bar(position, pvol, width= 0.4) 
        pvolSorted = sorted(pvol)
        redbar = self.redBar(pvol, pvolSorted) 
        group2 = ax.bar(position, redbar, color = 'red', width = 0.4)
        ax.set_yticks(pvol)
        ax.set_yticklabels(pvolSorted)
        plt.xticks(position, time, rotation = 90)
        plt.title('Volume graph')      
           
        #ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
        #ax.yaxis.set_minor_locator()
        #ax.yaxis.set.set_major_formater() 
        #ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
        #arrowprops=dict(facecolor='black', shrink=0.05))
        #ax.set_ylim(-2, 2)
        #on Dynamic ui
        plt.show()
        '''
        plt.style.use('ggplot')
        plt.ion()
        while self.total <= 2:
            plt.cla()
            plt.clf()
            plt.bar(self.priceVol().index, self.dataframes.values)
            plt.pause(5)
            self.total += 1
            #self.params += self.params  
        plt.ioff()   
        plt.show()
        '''
    def convert(self, value):
        value = value[:50]
        return value
      
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
    
