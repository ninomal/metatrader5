# implments volume in matplot basead in mt5 
import pandas as pd
import time
from datetime import datetime
import pytz
import matplotlib as plt
import pandas_ta as ta #calcule average and other function 

ATIVO = "WINV23" #name of market
POS = 0 # position bar
COUNT = 0 #position count 

class Products:
    def __init__(self, mt5):
        self.mt5 = mt5     
        self.COUNT = COUNT
        self.SYMBOL = ATIVO
        self.POS = POS
        self.daTime = self.dateTime()        
        self.dados = self.colectDate()
        self.TIMEFRAME = self.mt5.TIMEFRAME_M1
    
    def convertDateHour(self, df):
        df['time'] = pd.to_datetime(df['time'], unit ='s')
        return df
    
    def colectDate(self):
        date =self.mt5.copy_rates_from_pos(self.SYMBOL,self.mt5.TIMEFRAME_M1, self.POS, self.COUNT)
        dateDf = pd.DataFrame(date)
        dateConvDf = self.convertDateHour(dateDf)
        return dateConvDf
                
    def dateTime(self):
        named_tuple = time.localtime() 
        timeframe = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        print(timeframe)
        return timeframe
        
        
'''
    def prev_Calc(self):
        prev_calculated,_value = 
        "iMA(NULL, 0, period, 0, MODE_SMA, PRICE_CLOSE, 0)"
        
    def rates_total(self):
        bar = (start, )

    
    def onCalculate(dados,
                    const int prev_calculated,
                    const datetime &time[], 
                    const double &open[],
                    const double &high[],
                    const double &low[],
                    const double &close[],
                    const long &tick_volume[],
                    const long &volume[],
                    const int &spread[])
    {
    if(rates_total<2)
        return(0);
    //--- starting work
    int pos=prev_calculated-1;
    //--- correct position
    if(pos<1)
        {
        ExtVolumesBuffer[0]=0;
        pos=1;
        }
    //--- main cycle
    if(InpVolumeType==VOLUME_TICK)
        CalculateVolume(pos,rates_total,tick_volume);
    else
        CalculateVolume(pos,rates_total,volume);
    //--- OnCalculate done. Return new prev_calculated.
    return(rates_total);
    }
    //+------------------------------------------------------------------+
    //|                                                                  |
    //+------------------------------------------------------------------+
    void CalculateVolume(const int pos,const int rates_total,const long& volume[])
    {
    ExtVolumesBuffer[0]=(double)volume[0];
    ExtColorsBuffer[0]=0.0;
    //---
    for(int i=pos; i<rates_total && !IsStopped(); i++)
        {
        double curr_volume=(double)volume[i];
        double prev_volume=(double)volume[i-1];
        //--- calculate indicator
        ExtVolumesBuffer[i]=curr_volume;
        if(curr_volume>prev_volume)
            ExtColorsBuffer[i]=0.0;
        else
            ExtColorsBuffer[i]=1.0;
        }
    //---
    
    
    
    #test
    void OnStart()
  {
//---
   MqlRates rates[];
   ArraySetAsSeries(rates,true);
   int copied=CopyRates(Symbol(),0,0,100,rates);
   if(copied>0)
     {
      Print("Bars copied: "+copied);
      string format="open = %G, high = %G, low = %G, close = %G, volume = %d";
      string out;
      int size=fmin(copied,10);
      for(int i=0;i<size;i++)
        {
         out=i+":"+TimeToString(rates[i].time);
         out=out+" "+StringFormat(format,
                                  rates[i].open,
                                  rates[i].high,
                                  rates[i].low,
                                  rates[i].close,
                                  rates[i].tick_volume);
         Print(out);
        }
     }
   else Print("Failed to get history data for the symbol ",Symbol());
  }
    
  
    '''