## metatrader5 Api

[![NPM](https://img.shields.io/badge/Lincence-MIT-red)](https://github.com/ninomal/metatrader5/blob/main/LICENSE1)
[![NPM](https://img.shields.io/badge/Lincence-MQL-green)](https://www.mql5.com/en/docs)

#This project

This project is based on dynamic graphs for mql5;Tools for buy and sell and average media in pandas_ta

#Functions

First of all

Login in mt5 terminal

change name of ASSETS in products >products.py ASSETS Constante

change minuts in products >products.py def __init__ bellow  self.TIMEFRAME = self.mt5.TIMEFRAME_M1 <- here 

runtime in ui graphs

ui> ui.py > uiBar > plt.pause(2 <-change here) 

change start of market in products >products.py def current_day(self): change time in  day_raw = times.where(times== (day+' 9:00:00 <-here')).dropna()

Volume in indice 50 in graph
red candle for highest volume 

ui.allGraph()
![allgraph](https://github.com/ninomal/metatrader5/assets/137447782/0c3ff3f8-b172-4997-9cdc-25d5ae97ae8b)
all day PVOL ,while no stop graph change in 5 seconds  

ui.lastGraph('true')
![lasstgraph](https://github.com/ninomal/metatrader5/assets/137447782/5ec7ade7-2981-406e-83a4-ba3c1221a764)
last graph of day

ui.graphIntraDay()
![intraday](https://github.com/ninomal/metatrader5/assets/137447782/11bcaa9c-9f4e-4c19-8a39-c4cb3c0620ab)
current graph of day

ui.allRedBar()
![telallred](https://github.com/ninomal/metatrader5/assets/137447782/a98103e2-fd7c-4f44-bf4d-020a7c87bae2)
watch all highest sorted volume in 1000 candles 

ui.sortedRedBarIntraday()
![sortedintra](https://github.com/ninomal/metatrader5/assets/137447782/d58a8633-aa55-405d-bbf9-547980c4e8a8)
watch all highest sorted volume dynamic in day

ui.PizzaGraphForce()
![image](https://github.com/ninomal/metatrader5/assets/137447782/14543e90-d5fd-4501-a71c-a0c5a8362a47)
watch sum of volum force in pizza graph dynamic

#TECHNOLOGIES

[![NPM](https://img.shields.io/badge/PHYTON-blue)](https://www.python.org/)
[![NPM](https://img.shields.io/badge/Pandas-white)](https://pypi.org/project/pandas/)
[![NPM](https://img.shields.io/badge/Pandas__ta-gray)](https://pypi.org/project/pandas-ta/)
[![NPM](https://img.shields.io/badge/matplotlib-gren)](https://pypi.org/project/matplotlib/)
[![NPM](https://img.shields.io/badge/numpy-aqua)](https://pypi.org/project/numpy/)
[![NPM](https://img.shields.io/badge/MQL5-yellow)](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)

#AUTHOR

Jonatas leme dos reis "ninomal"




