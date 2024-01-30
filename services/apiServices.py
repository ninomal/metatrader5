from products import Apiconect
from products import Screenshot
#from products.Adb import 
from ui.ui import UI
from service import Service
from enums.enumsGraphics import enumsGraph
from products.Apiconect import Apiconect
from products.product import Products

class ApiServices():  
    def __init__(self, mt5, selecTime, ASSET, SECONDS, valueStr) :
        self.mt5 = mt5
        self.selecTime = selecTime
        self.ASSET = ASSET
        self.SECONDS = SECONDS
        self.valueStr = valueStr
        self.product = Products(self.mt5, self.SECONDS, self.ASSET)
        self.ui = UI(self.mt5, self.selecTime, self.ASSET, self.SECONDS)
        self.services = Service(self.mt5, self.selecTime, self.ASSET)
        self.enumsGraph = enumsGraph(self.ui)
        self.apiConect = Apiconect(self.product, self.ui)
        
    def selectGraph(self):
        valueStr = self.apiConect.readTxt()
        self.enumsGraph.selectUIgrap(valueStr)
        
    def actions(self):
        valueStr = self.apiConect.readTxt()
        if valueStr == "buy":
            self.services.buy()
        elif valueStr == "sell":
            self.services.sell()
        else:
            print("Action error")
            
    
    