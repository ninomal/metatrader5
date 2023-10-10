ITENS = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"10" ,"12 ","15" ,"20" ,"30 ","60" ,"2h" ,"3h" ,"4h" ,"6h" ,"8h" ,"12h" ,"1d" ,"2d" ,"3d"]
class TimeflameException:
    def __init__(self, value) :
        self.value = value
    
    
    def timeflameCheck(self):
        itens = ITENS
        for i in itens:
            if self.value == i:
                 False
                 break      
        return print(f"VALUE of {self.value} not acept")
    
    

                
        