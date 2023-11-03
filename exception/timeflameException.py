ITENS = ["1m" ,"2m" ,"3m" ,"4m" ,"5m" ,"6m" ,"10m" ,"12m","15m",
         "20m", "30m", "1h","2h" ,"3h" ,"4h" ,"6h" ,"8h" ,"12h" ,"1d" ,"1w" ,"1mon"]
class TimeflameException:
    def __init__(self, value) :
        self.value = value
       
    def timeflameCheck(self):
        for i in ITENS:
            if self.value == i:
                return i         
        return print(f"VALUE of {self.value} not acept in TIME FRAME")
    
    

                
        