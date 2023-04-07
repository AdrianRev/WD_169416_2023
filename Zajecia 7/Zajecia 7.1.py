import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
grupa = grupa.reset_index()
print(grupa.columns)
wykres = grupa.plot(x='Rok', y=('Liczba', 'sum'), kind='line')
wykres.set_ylabel('Liczba urodzeń')
wykres.legend()
plt.title("Liczba urodzeń w danym roku")
plt.xticks(range(2000, 2017, 2))
plt.show()