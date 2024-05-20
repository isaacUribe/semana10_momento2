import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hotel_miramar.csv', sep=',')

df['Precio'] = df['Dias de estancia'] * 53.49
df['IVA'] = df['Precio'] * 0.16
df['Total'] = df['Precio'] + df['IVA']

plt.pie(df['Total'], labels=df['Cliente'])

plt.show()