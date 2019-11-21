#Program zapisujący słowniki do pliku dictionaries.txt
import openpyxl, os, shelve
#ustawieni sciezki dla plików
sciezka = os.path.join('C:\\', 'Users', 'ajwal', 'OneDrive','IT', 'Projekty', 'Zew Cthulhu')
os.chdir(sciezka)
#otworzenie excela
workBook = openpyxl.load_workbook('lista_imion.xlsx', data_only=True)
#otworzeni pliku dictionaries.txt
plik = os.path.join(sciezka,'dictionaries.txt')
file = open(plik,'w')

#funkcje tworzące listy imion i nazwisk
def listCreator(workbook,column):
    return [i.value for i in workBook[workbook][column][1:-1]]

def dictCreator(listaNazw, listaNumerow):
    listaNazw.reverse()
    listaNumerow.reverse()
    return {'Nazwa':listaNazw,'Numery':listaNumerow}

#zapisanie wyników w pliku dictionaries.txt
file.write(str(dictCreator(listCreator('first names','B'), listCreator('first names','F')))+'\n\n')
file.write(str(dictCreator(listCreator('first names','F'), listCreator('first names','K')))+'\n\n')
file.write(str(dictCreator(listCreator('last names','B'), listCreator('last names','G')))+'\n\n')
file.close()

#zapisanie zmiennych slownikowych w pliku shelve
shelfFile = shelve.open('myData')
shelfFile['manName'] = dictCreator(listCreator('first names','B'),listCreator('first names','F'))
shelfFile['womanName'] = dictCreator(listCreator('first names','G'),listCreator('first names','K'))
shelfFile['lastName'] = dictCreator(listCreator('last names','B'),listCreator('last names','G'))

#Sprawdzenie długości list

if len(dictCreator(listCreator('first names','B'),listCreator('first names','F'))['Nazwa'])==len(dictCreator(listCreator('first names','B'),listCreator('first names','F'))['Numery']):
    print("OK")
else:
    print("ERROR")

                 

