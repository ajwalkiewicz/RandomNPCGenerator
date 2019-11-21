# Program ten generuje losowych NPC Do gry Zew Cthulu

# Dla wybranej płci:
# 1. losuje imie i nazwisko z listy
#   a) uwględniając popularnośc imion wtamtym okresie
# 2. losuje cechy postaci postaci
# 3. losuje zawód pod warunkiem:
#   a) nie wybrano zawodu wcześniej
#   b) zawód jest dobrany optymalnie pod statystyki
# 4. losuje umiejętności postaci (z listy umiejętności zawodowych)
# 5. losuje umiejętności z hobby
# 6. losuje dodatkowe cechy postaci
# 7. zapisuje statystyki so pliku
# -----Dodatkowe funkcje w przyszłości
# 1. Graficzny interfejs
# 2. więcej opcji do wyboru np. zawód postaci, zaintteresowania, wygląd
# 3. zapisuje kartę do
# 4. dodatnie opcji użycia investigator experience package

#import bibliotek
import openpyxl, os, random, shelve


#ustawianie aktualnej sciezki:
sciezka = os.path.join('C:\\', 'Users', 'ajwal', 'OneDrive','IT', 'Projekty', 'Zew Cthulhu')
os.chdir(sciezka)

workBook = openpyxl.load_workbook('lista_imion.xlsx', data_only=True)

#Tworzenie słownika imion: męskich, żeńskich i nazwisk
#Wszystkie słowniki zostały wytworzone za pomocą creatingDict.py
#Tutaj jedynie za pomocą modułu shelve zostały zimportowane zmienne
#Zmienne globalne
shelvFile = shelve.open('myData')
manName = shelvFile['manName']
womanName = shelvFile['womanName']
lastName = shelvFile['lastName']
krzepaMO = shelvFile['Krzepa_MO']

#Słownik zawodów

#Słownik profilu postaci

chrProfile = {
    'Imie' : '',
    'Nazwisko' : '',
    'Wiek': 0,
    'S' : 0,
    'KON' : 0,
    'BC' : 0,
    'ZR' : 0,
    'WYG' : 0,
    'INT' : 0,
    'MOC' : 0,
    'WYK' : 0,
    'PS' : 0,
    'Ruch' : 0,
    'PW' : 0,
    'PP' : 0,
    'PM' : 0,
    'MO' : 0,
    'Krzepa' : 0,
    }

#Losowanie imion i nazwisk
def losuj(dictionary, workbook, cell):
    sheet = workBook[workbook]
    number = random.randint(0, int(sheet[cell].value))
    for i in range(len(dictionary['Numery'])):
        if number <= dictionary['Numery'][i]:
            return dictionary['Nazwa'][i]
    return 'wtf?'

#Losowanie zawodu
def losujZawod():
    return none

#Generowanie cech postaci
def createCharacter():
    chrProfile['Imie']=losuj(manName, 'first names', 'E202')
    chrProfile['Nazwisko']= losuj(lastName, 'last names', 'F1002')
    chrProfile['Wiek']  = random.randint(15,90)
    chrProfile['S']  = random.randint(15,90)
    chrProfile['KON']= random.randint(15,90)
    chrProfile['BC'] = random.randint(40,90)
    chrProfile['ZR'] = random.randint(15,90)
    chrProfile['WYG']= random.randint(15,90)
    chrProfile['INT']= random.randint(40,90)
    chrProfile['MOC']= random.randint(15,90)
    chrProfile['WYK']= random.randint(40,90)
    chrProfile['PP'] = chrProfile['MOC']
    chrProfile['PS'] = random.randint(15,90)
    chrProfile['PM'] = chrProfile['MOC']//5
    chrProfile['PW'] = (chrProfile['BC']+chrProfile['KON'])//10
    chrProfile['MO'] = pochodne(chrProfile['S'],chrProfile['BC'])[0]
    chrProfile['Krzepa'] = pochodne(chrProfile['S'],chrProfile['BC'])[1]
    chrProfile['Ruch'] = pochodne(chrProfile['S'],chrProfile['BC'],chrProfile['ZR'])[2]

def pochodne(S, BC, *ZR):
    for _ in range(len(krzepaMO['Zakres'])):
        if S + BC <= krzepaMO['Zakres'][_]:
            results = list((krzepaMO['MO'][_],krzepaMO['Krzepa'][_]))
            break
    if ZR:
        if ZR[0] < BC and S < BC:
            results.append('7')
        elif S >= BC and ZR[0] >= BC:
            results.append('9')
        else:
            results.append('8')
    return results

#Wyświetlenie profilu postaci
def printCharacter(itemsDict, leftWidth, rightWidth):
    print('PROFIL POSTACI'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ' ') + str(v).ljust(rightWidth))

#Główna pętla programu
wartosc = "TAK"
print("Witaj w programie generującym NPC\n Oto twoja postać:")
while wartosc:
    createCharacter()
    printCharacter(chrProfile, 10, 6)

#Zapisanie profilu do pliku .txt
    chrFile = open('chracterFiles.txt','a')
    chrFile.write(str(chrProfile)+'\n\n')
    chrFile.close()

    print("Czy chcesz kontynuować? (enter to quit)")
    wartosc = input()

#Sprawdzenie poprawności
#print(lastName)
##print(lastName['Nazwa'][5])
##print(range(len(lastName['Numery'])))
##print(type(lastName['Numery'][5]))
##print(losuj(manName, 'first names', 'E202'))
##print(losuj(lastName, 'last names', 'F1002'))
