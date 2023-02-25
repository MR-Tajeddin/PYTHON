import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"/Users/alitaj/Desktop/writer.csv")
DF = df.Authors.to_list()
NewDF=[]

for S in DF:
    NewDF.extend(S.split("; "))
New = pd.Series(NewDF)
Freq = New.value_counts()
First10 = Freq [:10]

E = pd.DataFrame(First10)
Name = list(E.index)
E['Name']=Name
E1= E.reset_index(drop=True)
E1.columns = ['Fre','Name']
E1=E1[['Name','Fre']]
E1.to_csv(r"/Users/alitaj/Desktop/First10writers.csv")

U= E.values

import numpy as np

U.ndim
np.squeeze(U)
plt.bar(E.index, np.squeeze(U), width=0.5, bottom=None, align='center',color='green',edgecolor='yellow')
plt.xticks(rotation=90)
plt.xlabel('Authers Name')
plt.ylabel('Number of Article')
plt.title("The Number of Auther's Articles")

