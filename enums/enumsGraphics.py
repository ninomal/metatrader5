from threading import Thread
class EnumsGraph():
    def __init__( self, ui):
        self.ui = ui
                  

    def selectUIgrap( self, nameGraph):
        match nameGraph:
            case  "lastgraph":
                return self.ui.lastGraph('true')
            case  "allgraph":
                return self.ui.allGraph()
            case  "graphintra":
                return self.ui.graphIntraDay()  
            case  "uibar":
                return self.ui.uiBar()
            case "allred":
                return self.ui.allRedBar()
            case "allredintra":
                return self.ui.sortedRedBarIntraday()
            case "pizza":
                self.ui.pizzaGraphForce()
                self.ui.closedPlt()
            case "ad":
                return self.ui.adGraph()
            case "eom":
                return self.ui.eomGraph()
            case _:
                return print("Name error")
            
