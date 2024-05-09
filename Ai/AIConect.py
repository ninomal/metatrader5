
class AiConect():
    def __init__(self, ai ,aiColect, apiConect) :
        self.ai = ai
        self.aiColect = aiColect
        self.apiConect = apiConect
        
    def getText(self):
        text = self.apiConect.readTxt()
        self.ai.getText(text)
    
    def setText(self, *args):
        text = args
        self.apiConect.conectAiTxt(text)
    
        
        
    
    
        
    
    
        
        
    