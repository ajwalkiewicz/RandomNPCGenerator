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
def lName(workbook,column):
    listaImionMenskich = []
    sheet = workBook[workbook]
    for i in sheet[column][1:-1]:
        listaImionMenskich.append(i.value)
    return listaImionMenskich

def lNumber(workbook, column):
    numeryMenskich = []
    sheet = workBook[workbook]
    for i in sheet[column][1:-1]:
        numeryMenskich.append(i.value)
    return numeryMenskich

def dictCreator(listaNazw, listaNumerow):
    result = {}
    listaNazw.reverse()
    listaNumerow.reverse()
    result.setdefault(listaNazw[0],list(range(0,int(listaNumerow[0]))))
    for i in listaNazw:
        result.setdefault(i, list(range(int(listaNumerow[listaNazw.index(i)-1]), int(listaNumerow[listaNazw.index(i)]))))
    result.setdefault(listaNazw[-1],list(range(int(listaNumerow[-2]), int(listaNumerow[-1]))))
    return result

#zapisanie wyników w pliku dictionaries.txt
file.write(str(dictCreator(lName('first names','B'),lNumber('first names','F')))+'\n\n')
file.write(str(dictCreator(lName('first names','F'),lNumber('first names','K')))+'\n\n')
file.write(str(dictCreator(lName('last names','B'),lNumber('last names','G')))+'\n\n')
file.close()

#zapisanie zmiennych slownikowych w pliku shelve
shelfFile = shelve.open('myData')
shelfFile['manName'] = dictCreator(lName('first names','B'),lNumber('first names','F'))
shelfFile['womanName'] = dictCreator(lName('first names','G'),lNumber('first names','K'))
shelfFile['lastName'] = dictCreator(lName('last names','B'),lNumber('last names','G'))

#Sprawdzenie długości slownikow
#print(len(dictCreator(lName('first names','B'),lNumber('first names','F'))))
#print(len(dictCreator(lName('first names','F'),lNumber('first names','K'))))
#print(len(dictCreator(lName('last names','B'),lNumber('last names','G'))))

#Sprawdzenie poprawności
##huj = []
##for i in dictCreator(lName('first names','B'),lNumber('first names','F')).values():
##    huj = huj + i
##if huj == list(range(0,10004)):
##    print('jest OK')
##else:
##    print('czegos brakuje')

                 

