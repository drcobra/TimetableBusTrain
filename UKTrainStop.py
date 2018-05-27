import numpy as np
import pandas as pd

#Format time
def trueTime(x):
    if len(x) == 10:	#delay
        x = x[5:10]
    elif len(x) == 12:	#on time
        x = x[0:5]

    return x

def UKTrainStop(stopID, direction):
	df = pd.read_html('https://traintimes.org.uk/live/' + stopID + '?dep',header=0,skiprows=0)[0]

	#Split routes
	if direction == 1:
		df2 = df[df['P.']==1.0].drop(['P.','Unnamed: 3'], axis=1)
	elif direction == 2:
		df2 = df[df['P.']==2.0].drop(['P.','Unnamed: 3'], axis=1)

	#Modify time display. Look like the bus
	df2['Time'] = (pd.to_datetime(df2['Time'].astype(str).apply(trueTime)) - pd.datetime.now()).astype('timedelta64[m]')
	df2['Time'] = df2['Time'].astype(int).astype(str) + ' mins'
	
	df2.rename(columns={'Time': 'time', 'To': 'route'}, inplace=True)

	return df2[['route','time']].to_html(index=False, justify='left', border=0)
