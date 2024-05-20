import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('primerSemestre2002.csv', sep=',')

df['Costes Variables'] = df['Volumen De Ventas'] * 0.60

df['Costes'] = df['Costes Variables'] + df['Costes Fijos']

df['Beneficios'] = df['Ingresos Por Ventas'] - df['Costes']

bar_width = 0.35
index = np.arange(len(df))

plt.figure(figsize=(10,5))
plt.bar(index, df['Beneficios'], bar_width, label='Beneficios', color='blue')
plt.bar(index + bar_width, df['Costes'], bar_width, label='Costes', color = 'red')
plt.xlabel('Mes')
plt.title('Beneficios y costes por mes')
plt.xticks(index + bar_width / 2, df['Mes'], rotation = 45)
plt.legend()

plt.tight_layout()
plt.show()


print(df)