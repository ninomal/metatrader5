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
            #fig, ax = plt.subplots( )  # Create a figure containing a single axes.
            #ax.scatter(self.priceVol().index, self.priceVol().values) 
            
            #ax.plot([115000, 120000, 125000, 130000], [115200, 120200, 127000, 124000])
            #ax.legend("color ex")
            #ax.yaxis.set_minor_locator()
            #ax.yaxis.set.set_major_formater() 
            #data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
            #names = list(data.keys())
            #names = list(self.dataframe.keys())
            #values = list(self.dataframe.values())       
            #values = list(data.values())
            #valoriloc = self.priceVol().iloc[0]
            #df = self.dataframe.iloc[[0, 10]]
            #values = df['PVOL']
            #print(values)    
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        print(dfindex)
        x = self.convertToList(dfindex['time'], dfvalues['PVOL'])
        x = x[:10]
        print('aaaa') 
        print('cccc')
        plt.figure()
        #plt.bar(x,  x)
            #precos.plot(kind='bar')
        fig, axs = plt.subplots(figsize=(10, 5), layout='constrained')
        axs.bar(x, x)
            #fig.suptitle('Categorical Plotting') 
            #self.calcEma().plot()
            #self.calcAMV().plot()
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