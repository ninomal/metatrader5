## metatrader5 Api

[![NPM](https://img.shields.io/badge/Lincence-MIT-red)](https://github.com/ninomal/metatrader5/blob/main/LICENSE1)
[![NPM](https://img.shields.io/badge/Lincence-MQL-green)](https://www.mql5.com/en/docs)

# This project

This project is based on dynamic graphics for mql5;Tools for buy and sell and average media in pandas_ta

# Functions

First of all

Login in mt5 terminal

change name of ASSETS in app.py
![asset](https://github.com/ninomal/metatrader5/assets/137447782/c2de19df-ca85-48ca-9a51-c8d7f8284b53)

change seconds that the graphics will be shown
![secoindsGraficos](https://github.com/ninomal/metatrader5/assets/137447782/9e4ae5bc-dadf-4fac-bdfe-6720abe74d8f)


change time 
![selec](https://github.com/ninomal/metatrader5/assets/137447782/9311f3e9-27a2-45fc-9874-eb9678cc2809)
            Minuts: "1" "2" "3" "4" "5" "6" "10" "12" "15" "20" "30" 
            Hours : "1h" "2h"          
            Day: "1d" "2d"  
            week : "1w"                
            monthly : "1mon"


change start of market in
![hoursstart](https://github.com/ninomal/metatrader5/assets/137447782/f7c33e67-ed74-4d19-8130-dcb100a1111c)


enter in watssap web number phone for send imagens and txt
![phonenumber](https://github.com/ninomal/metatrader5/assets/137447782/608a5cdc-252f-4cd1-8363-a71a425b7d52)

# Tools


take screenshot dynamic
![printscrenpng](https://github.com/ninomal/metatrader5/assets/137447782/30f943f8-cf73-4173-ad97-fcb9656ef11c)


connect watssap number need local number 
![watssap](https://github.com/ninomal/metatrader5/assets/137447782/198b883a-f97f-473d-90c1-f74f6e2912bc)


read text in watssap web
![readtxt](https://github.com/ninomal/metatrader5/assets/137447782/4a54562a-b0e5-4b6c-a067-e267f0ef12cb)


read txt in watssap web and enter grafics, you need send names grafics in watssap
![apiselec](https://github.com/ninomal/metatrader5/assets/137447782/ea3efec7-2489-45e4-921d-298a5aa6cff1)


send imagen in watssap web automatic
![apisendimagen](https://github.com/ninomal/metatrader5/assets/137447782/9267f337-f22c-49b0-83e7-f81cc0223bd9)

calculate pattern v
![calcv](https://github.com/ninomal/metatrader5/assets/137447782/451699f7-3274-47e6-a78e-e59ac7cbc82f)


# Graphics

Volume in indice 50 in graph
red candle for highest volume 

ui.mt5Graf()
![mt5grafics](https://github.com/ninomal/metatrader5/assets/137447782/7cf5574b-903c-45e0-bcc3-351cac7367ad)
mt5 normal grafics

ui.allGraph()
![allgraph](https://github.com/ninomal/metatrader5/assets/137447782/0c3ff3f8-b172-4997-9cdc-25d5ae97ae8b)
all day PVOL ,while no stop graph change in 5 seconds 
    Product of price and volume.
    Calculation:
        if signed:
            pvol = signed_series(close, 1) * close * volume
        else:
            pvol = close * volume

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
    Money Flow Index is an oscillator indicator that is used to measure buying and
    selling pressure by utilizing both price and volume.
    Sources:
        https://www.tradingview.com/wiki/Money_Flow_(MFI)

ui.adGraph()
![adgraph](https://github.com/ninomal/metatrader5/assets/137447782/57b61455-cfb9-4aa5-87b5-1f00a1f7733f)
    Accumulation/Distribution indicator utilizes the relative position
    of the close to it's High-Low range with volume.  Then it is cumulated.
    Sources:
        https://www.tradingtechnologies.com/help/x-study/technical-indicator-definitions/accumulationdistribution-ad/


ui.eomGraph()
![eom](https://github.com/ninomal/metatrader5/assets/137447782/151184f6-df44-4b04-a8a0-5056f553f991)
Ease of Movement (EOM)
    Ease of Movement is a volume based oscillator that is designed to measure the
    relationship between price and volume flucuating across a zero line.
    Sources:
    https://www.tradingview.com/wiki/Ease_of_Movement_(EOM)
    https://www.motivewave.com/studies/ease_of_movement.htm
    https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ease_of_movement_emv



# TECHNOLOGIES

[![NPM](https://img.shields.io/badge/PHYTON-blue)](https://www.python.org/)
[![NPM](https://img.shields.io/badge/Pandas-white)](https://pypi.org/project/pandas/)
[![NPM](https://img.shields.io/badge/Pandas__ta-gray)](https://pypi.org/project/pandas-ta/)
[![NPM](https://img.shields.io/badge/matplotlib-gren)](https://pypi.org/project/matplotlib/)
[![NPM](https://img.shields.io/badge/numpy-aqua)](https://pypi.org/project/numpy/)
[![NPM](https://img.shields.io/badge/MQL5-yellow)](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)
[![NPM](https://img.shields.io/badge/PyAutogui-purple)](https://pyautogui.readthedocs.io/en/latest/)


# AUTHOR

Jonatas leme dos reis "ninomal"




