

class Ai():
    def __init__(self):
        self.actionValue = 0
    
    def questionAsnwer(self, valueDict):
        if valueDict["question"].upper() == "WHY": 
            self.whyAsnew(valueDict)
        elif valueDict["question"].upper() == "HOW": 
            self.howAsnew(valueDict)
        else:
            return print("Error")
    
    def whyAsnew(self, valueDict ): 
        if valueDict['valueBuy'] == "none":
            self.actionValue = valueDict['valueSell']
        else:
            self.actionValue = valueDict['valueBuy']
        return print("Why method",valueDict['method'], 
            "reached the point:", valueDict['valueMethod'],
            "and", valueDict['action'] ,"in price:", self.actionValue )
    
    def howAsnew(self, valueDict ): 
        if valueDict['valueBuy'] == "none":
            self.actionValue = valueDict['valueSell']
        else:
            self.actionValue = valueDict['valueBuy']
        return print("When method", valueDict['method'], 
            "not reaches the value:",self.actionValue,
            "you are not going to", valueDict['action'])
    
    def zapTextReadList(self, text ):
        strText = str(text)
        listText = strText.split(" ")
        self.textReadSelect(listText)
        
    def textReadSelect(self, text):
        text = self.zapTextReadList(text)
        textSplitSelec = list(filter
                (lambda textLam: textLam.upper() == "WHY" or textLam == "HOW", text))
        print(textSplitSelec[0])
        return textSplitSelec[0]
        
    def getText(self, text):
        self.zapTextReadList(text)
        
   