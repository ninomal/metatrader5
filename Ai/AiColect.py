#this class colect the date in dict mode

class AiColect():
    def __init__(self) -> None:
        self.aiDict = {}
    
    # return list whit sting price and method  
    def colectID(self, action, valueMethod, valueBuy, valueSell,priceNow, method):
        valueMethodStr = str(valueMethod)
        valueBuyStr = str(valueBuy)
        valueSellStr = str(valueSell)
        priceNowStr = str(priceNow)
        self.aiDict[action + " in " + valueMethodStr] = [valueBuyStr
                                        , valueSellStr,priceNowStr, method]
        return self.aiDict
    
            
         

        