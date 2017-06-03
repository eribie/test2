

import pandas as pd
pd.options.display.max_rows=10000
import os
import matplotlib.pyplot as plt
from Creation_df_spread import *
from classe_strategie import *





df = concatener_dataframes("Renault_retraité","Peugeot_retraité")

df['mmobx'] = df['7_x'].rolling(window=200).mean()

df['mmoby'] = df['7_y'].rolling(window=200).mean()
print(df)

df['spread'] = df['7_x'] - (df['7_y']*df['mmobx']/df['mmoby'])

print(df)

df = df.tail(10000)
print(df)


renault = strategie()
peugeot = strategie()
quantitz = 100

for index, row in df.iterrows():

    if row['spread'] > 1 and peugeot.achete is False:
        renault.vente(quantitz, row['7_x'])
        peugeot.achat(quantitz * row['7_x'] / row['7_y'], row['7_y'])
    elif row['spread'] < -1 and renault.achete is False:
        renault.achat(quantitz, row['7_x'])
        peugeot.vente(quantitz * row['7_x'] / row['7_y'], row['7_y'])
    elif row['spread'] < -1 and peugeot.achete is True and renault.vendu is True:
        peugeot.stopAchat(quantitz * row['7_x'] / row['7_y'], row['7_y'])
        renault.stopVente(quantitz, row['7_x'])

    elif row['spread'] > 1 and renault.achete is True and peugeot.vendu is True:
        renault.stopAchat(quantitz, row['7_x'])
        peugeot.stopVente(quantitz * row['7_x'] / row['7_y'], row['7_y'])

    df.loc[index, 'pnl'] = renault.get_Pnl(quantitz, row['7_x'])
    df.loc[index, 'av'] = peugeot.achete
#renault.get_Pnl(quantitz,row['7_x'])+ peugeot.get_Pnl(quantitz * row['7_x']/row['7_y'],row['7_y'])

print(df)
print(df['pnl'])
#print (quantitz * row['7_x']/row['7_y'])
df.plot(x='timestamp',y=['spread','7_x','7_y'])
df.plot(x='timestamp',y='pnl')
plt.show()