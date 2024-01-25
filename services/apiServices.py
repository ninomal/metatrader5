from products import Apiconect
from products import Screenshot
from products import Adb
from ui.ui import UI
from service import Service

class ApiServices():  
    def __init__(self, mt5, selecTime, ASSET, SECONDS, valueStr) :
        self.mt5 = mt5
        self.selecTime = selecTime
        self.ASSET = ASSET
        self.SECONDS = SECONDS
        self.valueStr = valueStr
        self.ui = UI(self.mt5, self.selecTime, self.ASSET, self.SECONDS)
        services = Service(self.mt5, self.selecTime, self.ASSET)
        
    def selectUIgrap(self, nameGraph):
        pass