import pandas as pd
import openpyxl


imiona = pd.read_excel('imiona.xlsx',)

#zad2a
#print(imiona[imiona['Liczba']>1000])

#zad2b
#print(imiona[imiona['Imie']=='ADRIAN'])

#zad2c
#Liczba_urodzen = imiona['Liczba'].sum()
#print(Liczba_urodzen)

#zad2d
#print(imiona.groupby(['Rok']).agg({'Liczba':['sum']}))

#zad2e
#d1 = imiona[(imiona['Rok'] > 1999) & (imiona['Rok'] < 2006)]['Liczba'].sum()
#print(d1)

#Zad2f
#print(imiona.groupby(['Plec']).agg({'Liczba':['sum']}))

#zad2g
#suma = imiona.groupby(['Imie', 'Plec']).agg({'Liczba': ['sum']})
#popularne = suma.groupby('Plec').idxmax()
#print(popularne)

#zad2h
#suma = imiona.groupby(['Rok','Imie', 'Plec']).agg({'Liczba': ['sum']})
#popularne = suma.groupby(['Rok','Plec']).idxmax()
#print(popularne)