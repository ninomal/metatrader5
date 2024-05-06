

class Ai():
    def __init__(self, text, request):
        self.text = text
        self.resquest = request
        self.textSelect = self.textReadSelect()
    
    #def whyMethode(self,ValueX, valueY ,request ):
        #if(self.resquest == True and ):
         
            #print()
    
    def textReadList(self):
        strText = str(self.text)
        listText = strText.split(" ")
        return listText
        
    def textReadSelect(self):
        text = self.textReadList()
        textSplitSelec = list(filter
                (lambda textLam: textLam.upper() == "WHY" or textLam == "HOW", text))
        print(textSplitSelec)