'''
Program zapisujący słowniki do pliku dictionaries.txt
creatingDict pobiera dane z komórek (IMIE/NAZWISKO) oraz Numery
a następnie zapisuje je w postaci słownika w następującym schemacie
{"Nazwa":[lista imion],"Numery":[lista numerów]}
'''
import openpyxl
import shelve

# otworzenie excela
excel_file = openpyxl.load_workbook('lista_imion.xlsx', data_only=True)

# funkcje tworzące listy imion i nazwisk


def list_creator(workbook, column):
    return [i.value for i in excel_file[workbook][column][1:-1]]


def dict_creator(lista_nazw, lista_numerow):
    lista_nazw.reverse()
    lista_numerow.reverse()
    return {'Nazwa': lista_nazw, 'Numery': lista_numerow}


# zapisanie wyników w pliku dictionaries.txt
file = open("dictionaries.txt", 'w')
file.write(str(dict_creator(
    list_creator('first names', 'B'), list_creator('first names', 'F')))+'\n\n')
file.write(str(dict_creator(
    list_creator('first names', 'F'), list_creator('first names', 'K')))+'\n\n')
file.write(str(dict_creator(
    list_creator('last names', 'B'), list_creator('last names', 'G')))+'\n\n')
file.close()

# zapisanie zmiennych slownikowych w pliku shelve
shelf_file = shelve.open('myData')
shelf_file['man_name'] = dict_creator(
    list_creator('first names', 'B'), list_creator('first names', 'F'))
shelf_file['woman_name'] = dict_creator(
    list_creator('first names', 'G'), list_creator('first names', 'K'))
shelf_file['last_name'] = dict_creator(
    list_creator('last names', 'B'), list_creator('last names', 'G'))


# Sprawdzenie długości list
if len(shelf_file['man_name']['Nazwa']) == len(shelf_file['man_name']['Numery']):
    print("OK")
else:
    print("ERROR")
