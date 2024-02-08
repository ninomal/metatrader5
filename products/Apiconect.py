from products.Adb import Adbconect
from products.product import Products
from enums.enumsGraphics import EnumsGraph

class Apiconect():
    def __init__(self, mt5, timeframe, asset, phonenumber, ui, HOURSSTART) :
        self.product = Products(mt5, timeframe, asset, HOURSSTART)
        self.adb = Adbconect(phonenumber)
        self.enumsGraph = EnumsGraph(ui)
              
    def readTxt(self):
        return self.adb.readMsgOfChat()
    
    #send image in watssap web
    def sendImage(self):
        self.adb.sendImagens(self.product.hoursImgName())
        
    #read text in watsapp web and transfer for UI graphics
    def selecGraph(self):
        self.enumsGraph.selectUIgrap(self.readTxt())
        
        
    
        
        
        
        
    
    
        
    
    