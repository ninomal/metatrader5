#this class colect the date in dict mode

class AiColect():
    def __init__(self) -> None:
        self.aiDict = {}
    
    # return string dict with values method  
    def colectID(self, action, valueMethod, valueBuy, valueSell,priceNow, method, question):
        valueMethodStr = str(valueMethod)
        valueBuyStr = str(valueBuy)
        valueSellStr = str(valueSell)
        priceNowStr = str(priceNow)
        self.aiDict = { "action": action, "valueMethod": valueMethodStr, "valueBuy": valueBuyStr
            ,"valueSell": valueSellStr,"priceNow" :priceNowStr, "method": method, "question" :question}
        return self.aiDict
    
            
         

        