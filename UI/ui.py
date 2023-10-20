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
        print(preco)
        preco = preco.to_frame()
        return preco
        
    def construc(self):
        #fig, ax = plt.subplots()  # Create a figure containing a single axes.
        #ax.plot([115000, 120000, 125000, 130000], [115200, 120200, 127000, 124000])
        #ax.legend("color ex")
        #ax.yaxis.set_minor_locator()
        #ax.yaxis.set.set_major_formater() 
        #data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
        #names = list(data.keys())
        #values = list(data.values())
        #fig, axs = plt.subplots(1)
        #axs.bar(names, values)
        #fig.suptitle('Categorical Plotting') 
        #self.calcEma().plot()
        #self.calcAMV().plot()
        while self.total <= 20:
            plt.ion()
            self.dataframe = self.dataframe[:self.params]
            self.dataframe.plot(kind= 'bar') 
            
            plt.pause(2)
            plt.cla()
            plt.clf()    
            plt.ioff()
            self.total += 1
            self.params += self.params * 2