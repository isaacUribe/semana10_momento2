import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('factura.csv', sep=',')

df['Mano de Obra($)'] = df['Mano de Obra(Horas)'] * 18
df['Total'] = df['Mano de Obra($)'] + df['Materiales']

subtotal = df['Total'].sum()
iva = subtotal * 0.16
total = subtotal + iva

print("Subtotal", subtotal)
print("IVA", iva)
print("TOTAL", total)

print(df)

plt.plot(df['Descripcion'],df['Materiales'], label='Materiales')
plt.plot(df['Descripcion'], df['Mano de Obra(Horas)'], label='Mano de obra', linestyle='--')
plt.show()