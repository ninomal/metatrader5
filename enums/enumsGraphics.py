class enumsGraph():

    def __init__( self, ui):
        self.ui = ui
                  
    def selectUIgrap( self, nameGraph):
        if nameGraph == "lastgraph":
            return self.ui.lastGraph('true')
        elif nameGraph == "allgraph":
            return self.ui.allGraph()
        elif nameGraph == "graphintra":
            return self.ui.graphIntraDay()  
        elif nameGraph == "uibar":
            return self.ui.uiBar()
        elif nameGraph == "allred":
            return self.ui.allRedBar()
        elif nameGraph == "allredintra":
            return self.ui.sortedRedBarIntraday()
        elif nameGraph == "pizza":
            return self.ui.pizzaGraphForce()
        elif nameGraph == "ad":
            return self.ui.adGraph()
        elif nameGraph == "eom":
            return self.ui.eomGraph()
        elif nameGraph == "eomnow":
            return self.ui.eomGraphNow()
        elif nameGraph == "adnow":  
            return self.ui.adGraphNow()
        else:
            return print("Name error")