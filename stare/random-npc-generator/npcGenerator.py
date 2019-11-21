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
shelvFile = shelve.open('myData')
manName = shelvFile['manName']
womanName = shelvFile['womanName']
lastName = shelvFile['lastName']

#Słownik zawodów

#Słownik profilu postaci

chrProfile = {
    'imie' : '',
    'nazwisko' : '',
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
    for i,j in dictionary.items():
        if number in j:
            return i
    return 'wtf?'

nazwisko = losuj(lastName, 'last names', 'F1002')
chrProfile['imie']=losuj(manName, 'first names', 'E202')
chrProfile['nazwisko']= nazwisko[0].upper() + nazwisko[1:].lower()
chrProfile['S']  =random.randint(15,90)
chrProfile['KON']=random.randint(15,90)
chrProfile['BC'] =random.randint(40,90)
chrProfile['ZR'] =random.randint(15,90)
chrProfile['WYG']=random.randint(15,90)
chrProfile['INT']=random.randint(40,90)
chrProfile['MOC']=random.randint(15,90)
chrProfile['WYK']=random.randint(40,90)
chrProfile['PP'] =chrProfile['MOC']
chrProfile['PS'] =random.randint(15,90)
chrProfile['PM'] =chrProfile['MOC']//5
chrProfile['PW'] =(chrProfile['BC']+chrProfile['KON'])//10

#Losowanie zawodu

#Wyświetlenie profilu postaci

for i,j in chrProfile.items():
    print(i + ':  ' + str(j))

#Zapisanie profilu do pliku .txt
chrFile = open('chracterFiles.txt','a')
chrFile.write(str(chrProfile)+'\n\n')
chrFile.close()
