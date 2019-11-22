'''
Program zapisujący słowniki do pliku dictionaries.txt
creatingDict pobiera dane z komórek (IMIE/NAZWISKO) oraz Numery
a następnie zapisuje je w postaci słownika w następującym schemacie
{"Nazwa":[lista imion],"Numery":[lista numerów]}
'''
import openpyxl
import shelve

# otworzenie excela
workBook = openpyxl.load_workbook('lista_imion.xlsx', data_only=True)

# funkcje tworzące listy imion i nazwisk


def listCreator(workbook, column):
    return [i.value for i in workBook[workbook][column][1:-1]]


def dictCreator(listaNazw, listaNumerow):
    listaNazw.reverse()
    listaNumerow.reverse()
    return {'Nazwa': listaNazw, 'Numery': listaNumerow}


# zapisanie wyników w pliku dictionaries.txt
file = open("dictionaries.txt", 'w')
file.write(str(dictCreator(listCreator('first names', 'B'), listCreator('first names', 'F')))+'\n\n')
file.write(str(dictCreator(listCreator('first names', 'F'), listCreator('first names', 'K')))+'\n\n')
file.write(str(dictCreator(listCreator('last names', 'B'), listCreator('last names', 'G')))+'\n\n')
file.close()

# zapisanie zmiennych slownikowych w pliku shelve
shelfFile = shelve.open('myData')
shelfFile['manName'] = dictCreator(listCreator('first names', 'B'), listCreator('first names', 'F'))
shelfFile['womanName'] = dictCreator(listCreator(
    'first names', 'G'), listCreator('first names', 'K'))
shelfFile['lastName'] = dictCreator(listCreator('last names', 'B'), listCreator('last names', 'G'))

# Sprawdzenie długości list

if len(dictCreator(listCreator('first names', 'B'), listCreator('first names', 'F'))['Nazwa']) == len(dictCreator(listCreator('first names', 'B'), listCreator('first names', 'F'))['Numery']):
    print("OK")
else:
    print("ERROR")
