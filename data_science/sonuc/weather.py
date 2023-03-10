import pandas as pd
df=pd.read_csv("weatherHistory.csv",index_col='Formatted Date', parse_dates=True)
df.index = pd.to_datetime(df.index)
print(df.dtypes)
#df.resample('D')
#print(df.head())