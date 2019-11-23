'''
Program ten generuje losowych NPC Do gry Zew Cthulu
Wszystkie słowniki zostały wytworzone za pomocą creatingDict.py
Tutaj jedynie za pomocą modułu shelve zostały zimportowane zmienne
'''

# import bibliotek
import openpyxl
import random
import shelve
import modules.dictionaries
import os

# Otwieranie excela
excel_file = openpyxl.load_workbook(os.path.join("support", "lista_imion.xlsx"), data_only=True)

# Zmienne globalne
shelv_file = shelve.open(os.path.join("support", "myData"))
man_name = shelv_file['man_name']
woman_name = shelv_file['woman_name']
last_name = shelv_file['last_name']
KRZEPA_MO = modules.dictionaries.KRZEPA_MO
# Słownik zawodów

# Słownik profilu postaci

chr_profile = {
    'Imie': '',
    'Nazwisko': '',
    'Wiek': 0,
    'S': 0,
    'KON': 0,
    'BC': 0,
    'ZR': 0,
    'WYG': 0,
    'INT': 0,
    'MOC': 0,
    'WYK': 0,
    'PS': 0,
    'Ruch': 0,
    'PW': 0,
    'PP': 0,
    'PM': 0,
    'MO': 0,
    'Krzepa': 0,
}

# Losowanie imion i nazwisk


def losuj(dictionary, workbook, cell):
    sheet = excel_file[workbook]
    number = random.randint(0, int(sheet[cell].value))
    for i in range(len(dictionary['Numery'])):
        if number <= dictionary['Numery'][i]:
            return dictionary['Nazwa'][i]
    return 'wtf?'

# Losowanie zawodu


def losuj_zawod():
    return

# Generowanie cech postaci


def create_character():
    chr_profile['Imie'] = losuj(man_name, 'first names', 'E202')
    chr_profile['Nazwisko'] = losuj(last_name, 'last names', 'F1002')
    chr_profile['Wiek'] = random.randint(15, 90)
    chr_profile['S'] = random.randint(15, 90)
    chr_profile['KON'] = random.randint(15, 90)
    chr_profile['BC'] = random.randint(40, 90)
    chr_profile['ZR'] = random.randint(15, 90)
    chr_profile['WYG'] = random.randint(15, 90)
    chr_profile['INT'] = random.randint(40, 90)
    chr_profile['MOC'] = random.randint(15, 90)
    chr_profile['WYK'] = random.randint(40, 90)
    chr_profile['PP'] = chr_profile['MOC']
    chr_profile['PS'] = random.randint(15, 90)
    chr_profile['PM'] = chr_profile['MOC'] // 5
    chr_profile['PW'] = (chr_profile['BC'] + chr_profile['KON']) // 10
    chr_profile['MO'] = pochodne(chr_profile['S'], chr_profile['BC'])[0]
    chr_profile['Krzepa'] = pochodne(chr_profile['S'], chr_profile['BC'])[1]
    chr_profile['Ruch'] = pochodne(chr_profile['S'], chr_profile['BC'], chr_profile['ZR'])[2]
    return


def pochodne(S, BC, *ZR):
    for _ in range(len(KRZEPA_MO['Zakres'])):
        if S + BC <= KRZEPA_MO['Zakres'][_]:
            results = list(
                (KRZEPA_MO['MO'][_], KRZEPA_MO['Krzepa'][_]))
            break
    if ZR:
        if ZR[0] < BC and S < BC:
            results.append('7')
        elif S >= BC and ZR[0] >= BC:
            results.append('9')
        else:
            results.append('8')
    return results

# Wyświetlenie profilu postaci


def print_character(itemsDict, leftWidth, rightWidth):
    print('PROFIL POSTACI'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ' ') + str(v).ljust(rightWidth))


# Główna pętla programu
wartosc = "TAK"
print("Witaj w programie generującym NPC\n Oto twoja postać:")
while wartosc:
    create_character()
    print_character(chr_profile, 10, 6)

# Zapisanie profilu do pliku .txt
    chr_file = open('chracter_files.txt', 'a')
    chr_file.write(str(chr_profile)+'\n\n')
    chr_file.close()

    print("Czy chcesz kontynuować? (enter to quit)")
    wartosc = input()

# Sprawdzenie poprawności
# print(lastName)
# print(lastName['Nazwa'][5])
# print(range(len(lastName['Numery'])))
# print(type(lastName['Numery'][5]))
# print(losuj(manName, 'first names', 'E202'))
# print(losuj(lastName, 'last names', 'F1002'))
