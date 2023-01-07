#CryptoCurrencies.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stt 

URL = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ETH&market=USD&apikey=RV1XK080XUBTH2EG&datatype=csv'
Columns = ['timestamp', 'open (USD)', 'high (USD)', 'low (USD)', 'close (USD)', 'volume']
DF = pd.read_csv(URL, sep = ',', usecols = Columns, header = 0)

#print(DF.head(10))
#print(DF.tail(10))

C = DF['close (USD)'].to_numpy()
C = C[::-1].copy()

plt.plot(C,label='ETH Closes (Last 1000 Days)')
plt.xlabel('Time (Days)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
