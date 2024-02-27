from products.Adb import Adbconect
from products.product import Products
from enums.enumsGraphics import EnumsGraph

class Apiconect():
    def __init__(self, mt5, timeframe, asset, phonenumber, ui, HOURSSTART) :
        self.product = Products(mt5, timeframe, asset, HOURSSTART)
        self.adb = Adbconect(phonenumber)
        self.enumsGraph = EnumsGraph(ui)
        self.ui = ui
              
    def readTxt(self):
        self.adb.readMsgOfChat()
    
    #send image in watssap web
    def sendImage(self):
        img = self.product.hoursImgName()
        self.adb.sendImagens(img) 
        self.ui.closedPlt()
        self.product.deleteImg(img) 
        
    #read text in watsapp web and transfer for UI graphics
    def selecGraph(self):
        self.enumsGraph.selectUIgrap(self.readTxt())
        
    def apiConectZap(self):
        self.adb.adbConect()
        
    
    
        
    
        
        
        
        
    
    
        
    
    