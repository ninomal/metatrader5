from AiColect import AiColect

class Ai():
    def __init__(self):
        pass
    
    def whyAsnew(self,nameOfMethod, value , getQuizZap):
        if (getQuizZap == "WHY"):
            print("Why method ", nameOfMethod, " reached the point: ", value )
    
    def howAsnew(self,nameOfMethod, value , getQuizZap):
        if (getQuizZap == "HOW"):
            print("When method ", nameOfMethod, " reaches the value: ", value )
    
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
        
   