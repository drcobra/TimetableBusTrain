import numpy as np
import pandas as pd

#from IPython.display import display, HTML
#http://m.buses.co.uk/stop.aspx?stopid=155089

def BrightonBusStop(stopID):
    df = pd.read_html('http://m.buses.co.uk/stop.aspx?stopid=' + stopID, header=0,skiprows=2)[0]
    df['route'] = df['service'].astype(str)+" "+df['destination']

    return df[['route','time']].to_html(index=False, justify='left', border=0)
