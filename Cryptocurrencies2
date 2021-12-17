#CryptoCurrencies.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stt
def fetch(Symbol:str,Market:str='USD'):
    URL = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={}&market={}&apikey=RV1XK080XUBTH2EG&datatype=csv'.format(Symbol,Market)
    Columns = ['timestamp', 'open (USD)', 'high (USD)', 'low (USD)', 'close (USD)', 'volume']
    DF = pd.read_csv(URL, sep = ',', usecols = Columns, header = 0)

    #print(DF.head(10))
    #print(DF.tail(10))
    C = (DF['close (USD)'].to_numpy())[::-1].copy()

    L = np.log(C)

    return C, L
Ceth, Leth = fetch('ETH')
Cbtc, Lbtc = fetch('BTC')

plt.subplot(2,1,1)
plt.plot(Leth, label = 'ETH Closes')
plt.xlabel('Time (Day')
plt.ylabel('Price ($)')
plt.legend()

plt.subplot(2,1,2)
plt.plot(Lbtc, label = 'BTC Closes')
plt.xlabel('Time (Day')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
#plt.subplot(1,2,1)
#plt.plot(C,label='ETH Closes (Last 1000 Days)')
#plt.xlabel('Time (Days)')
#plt.ylabel('Price ($)')
#plt.legend()

#plt.subplot(1,2,2)
#plt.semilogy(C,label='ETH Closes (Last 1000 Days)')
#plt.xlabel('Time (Days)')
#plt.ylabel('Price ($)')
#plt.legend()
#plt.show()
L =np.log(C)
#plt.plot(L)
#plt.show()
