import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('ventasEfectuadas2001.csv', sep=',')

df['Total por Vendedor'] = df['T1'] + df['T2'] + df['T3'] + df['T4']

total_por_trimestre = df[['T1', 'T2', 'T3', 'T4']].sum()

print('Total por Trimestre')
print(total_por_trimestre)

print(df)


plt.pie(df['Total por Vendedor'], labels=df['Vendedor'])
plt.title('Ventas Efectuadas en 2001')
plt.show()