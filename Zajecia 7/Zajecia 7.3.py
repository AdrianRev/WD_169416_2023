import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('imiona.xlsx')
df_lata = df[(df['Rok']>=2013) &(df['Rok']<=2017)].reset_index()
df_plec = df_lata.groupby('Plec').sum()

wykres=df_plec.plot.pie(x='Plec',y='Liczba',autopct='%.2f %%',fontsize=20)
plt.title('% urodzonych dzieci ze względu na płeć w latach 2013-2017')
wykres.set_ylabel('Urodzenia')
plt.show()