import matplotlib as plt
from product import Products
import pandas_ta as ta #calcule average and other function 

class ProductsServices(Products):
       
    def __init__(self):
        super().__init__()
        pass
        
    
    
        
            
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

