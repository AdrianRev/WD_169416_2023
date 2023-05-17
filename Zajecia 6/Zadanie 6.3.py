import pandas as pd

def zad_a(df):
    unikalne = df['Sprzedawca'].unique()
    df_unikalne = pd.DataFrame({'Nazwisko':unikalne})
    print(df_unikalne)

def zad_b(df):
    print(df.sort_values(by='Utarg', ascending=False).head(5))

def zad_c(df):
    print(df.groupby('Sprzedawca')['idZamowienia'].count())

def zad_d(df):
    print(df.groupby('Kraj')['idZamowienia'].count())

def zad_e(df):
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    df_e = df[(df['Data zamowienia'].dt.year == 2005) & (df['Kraj'] == 'Polska')]
    print(df_e['Kraj'].count())

def zad_f(df):
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    print(df['Utarg'][(df['Data zamowienia'].dt.year == 2004)].mean())

def zad_g(df):
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    df2004 = df[df['Data zamowienia'].dt.year == 2004]
    df2004.to_csv('zamowienia_2004.csv', header=None, index=False)

    df2005 = df[df['Data zamowienia'].dt.year == 2005]
    df2005.to_csv('zamowienia_2004.csv', header=None, index=False)

def main():
    df = pd.read_csv('zamowienia.csv', sep=';')




if __name__ == "__main__":
    main()