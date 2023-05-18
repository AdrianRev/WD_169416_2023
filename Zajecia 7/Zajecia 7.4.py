import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',sep=';')
df_g = df.groupby('Sprzedawca')['idZamowienia'].count().reset_index()
wykres = df_g.plot.bar(x = 'Sprzedawca',y = 'idZamowienia',label = None)
wykres.set_ylabel('Ilość złożonych zamówień')
wykres.set_xlabel('Sprzedawca')
plt.xticks(rotation=35)
plt.show()