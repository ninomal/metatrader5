import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


from products.productsServices import ProductsServices


class UI(ProductsServices):
    def __init__(self, mt5):
        super().__init__(mt5)
        
        
    def teste(self):
        preco = self.priceVol()
        print(preco)
        
    def construc(self):
        #fig, ax = plt.subplots()  # Create a figure containing a single axes.
        #ax.plot([115000, 120000, 125000, 130000], [115200, 120200, 127000, 124000])  # Plot some data on the axes.
        #ax.set_title("aaa")
        #ax.legend("color ex")
        #ax.yaxis.set_minor_locator()
        #ax.yaxis.set.set_major_formater() 
        #data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
        #names = list(data.keys())
        #values = list(data.values())
        #fig, axs = plt.subplots(1)
        #axs.bar(names, values)
        #fig.suptitle('Categorical Plotting')
        
        df = self.priceVol()
        ax = df.plot(kind='bar', x='Length', y= 'PVOL')
        ax.scatter('Length', 'PVOL')
        
        plt.show()