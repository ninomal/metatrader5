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
        time = time[:10]
        pvol = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'y')
        pvol = pvol[:10]
        print('aaaa') 
        print(time)
        print('cccc')
        print(pvol)
        position = range(len(pvol))
        fig, ax = plt.subplots(layout='constrained')# Create a figure containing a single axes. 
        plt.bar(position, pvol )
        ax.set_yticklabels(pvol)
        plt.xticks(position, time)
        plt.title('Volume graph')
        #self.reOrder(pvol.items())    
        #ax.set_yticks()
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
            self.dataframes = self.dataframe
            plt.cla()
            plt.clf()
            plt.bar(self.priceVol().index, self.dataframes.values)
            plt.pause(5)
            self.total += 1
            #self.params += self.params  
        plt.ioff()   
        plt.show()
        '''
    '''      
    def reOrder(self, x):
        lens = 0
        y = 0  
        while lens != len(x):
            if y < x :
                y[lens] = x
                print(y)
            lens += 1
        return y'''