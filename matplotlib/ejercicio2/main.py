import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv('movimientos2001.csv', sep=',')

df['Beneficios'] = df['Ingresos'] - df['Gastos']
df['Porcentaje'] = df['Beneficios'] * 0.14

bar_width = 0.35
index = np.arange(len(df))

plt.figure(figsize=(10,5))
plt.bar(index, df['Beneficios'], bar_width, label='Beneficios', color='blue')
plt.bar(index + bar_width, df['Gastos'], bar_width, label='Gastos', color = 'red')

plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.title('Beneficios y gastos por mes')
plt.xticks(index + bar_width / 2, df['Mes'], rotation = 45)
plt.legend()

plt.tight_layout()
plt.show()
