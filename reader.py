import os
import sys
import csv

src = sys.argv[1]
dst = sys.argv[2]
zmiany = sys.argv[3:]

# src = sciezka odczytu = katalog_1/katalog_11/katalog_111/mlb_players.csv
# dst = sciezka zapisu = katalog_1/ katalog_11/katalog_112/katalog_docelowy
# i zmiany: change1 change2 change3
#
# if os.path.exists(src) and os.path.isfile(src):
#     print('OK')
# else:
#     print('Nie OK')


def zmien_csv():
    wyzszy_katag, nazwa_pliku = os.path.split(src)
    if not os.path.isfile(src):
        print(f'Podany plik {nazwa_pliku} nie istnieje.')
        print(f'Pliki w katalogu {wyzszy_katag}:')
        print(os.listdir(wyzszy_katag))
        return
    else:
        with open(src) as plik:
            zawartosc_pliku = []
            reader = csv.reader(plik, skipinitialspace=True)
            for wiersz in reader:
                zawartosc_pliku.append(wiersz)
        # print(zawartosc_pliku[:5])
        for zmiana in zmiany[:2]:
            z = zmiana.split(',')
            # print(z)

            liczba_wierszy = len(zawartosc_pliku)
            liczba_kolumn = len(zawartosc_pliku[0])

            if liczba_wierszy > int(z[0]) and liczba_kolumn > int(z[1]):
                zawartosc_pliku[int(z[0])][int(z[1])] = z[2]
            # print(int(z[0]))
            # print(int(z[1]))

        sciezka_nowego_pliku = os.path.join(dst, nazwa_pliku)
        if not os.path.isdir(dst):
            os.makedirs(dst)
        # print(katalog)
        with open(sciezka_nowego_pliku, 'w') as plik_zapisu:
            writer = csv.writer(plik_zapisu)
            for wiersz in zawartosc_pliku:
                writer.writerow(wiersz)

zmien_csv()