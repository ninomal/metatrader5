#this class colect the date in dict mode


class AiColect():
    def __init__(self) -> None:
        self.aiDict = {}
        self.methodName = {}
        
    def colectID(self, action, value, valueBuy, valueSell):
        valueStr = str(value)
        self.aiDict[action + " in " + valueStr] = valueBuy
        return self.aiDict
    
    def colectMethod(self, method, hit):
        hitStr = str(hit)
        self.methodName[method] = hitStr
        return self.methodName
            
         

        