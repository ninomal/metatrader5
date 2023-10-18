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
        fig, ax = plt.subplots()  # Create a figure containing a single axes.
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
        ax.set_title("aaa")
        ax.legend("color ex")
        ax.yaxis.set_minor_locator()
        plt.show()