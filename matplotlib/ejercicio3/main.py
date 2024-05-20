import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('papeleriaJuanGandia.csv', sep=',')


df['Precio'] = df['Precio Unitario'] * df['Cantidad']

total = df['Precio'].sum()
iva = total * 0.16
pre_final = total + iva

print(df)
print("TOTAL: ", total)
print("IVA: ", iva)
print("PRE. FINAL: ", pre_final)

plt.pie(df['Precio'], labels=df['Nombre'])

plt.show()