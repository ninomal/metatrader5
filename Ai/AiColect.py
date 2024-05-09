#this class colect the date in dict mode


class AiColect():
    def __init__(self) -> None:
        self.aiDict = {}
        
    def colectID(self, action, value, valueBuy, valueSell,priceNow, method, operationMethod):
        valueStr = str(value)
        self.aiDict[action + " in " + valueStr] = [valueBuy, valueSell,priceNow, method, operationMethod]
        return self.aiDict
    
            
         

        