import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
grupa = grupa.reset_index()
wykres = grupa.plot(x='Plec', y=('Liczba', 'sum'), kind='bar')
print(grupa)
wykres.set_ylabel('Liczba urodzeń(mln)')
wykres.legend()
plt.title("Liczba urodzeń konkretnej płci w danym roku")
plt.show()
