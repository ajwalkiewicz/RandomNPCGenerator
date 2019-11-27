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
from os import path
import tkinter
from PIL import ImageTk, Image

# Otwieranie excela
excel_file = openpyxl.load_workbook(path.join("support", "lista_imion.xlsx"), data_only=True)

# Zmienne globalne
shelv_file = shelve.open(path.join("support", "myData"))
man_name = shelv_file['man_name']
woman_name = shelv_file['woman_name']
last_name = shelv_file['last_name']
KRZEPA_MO = modules.dictionaries.KRZEPA_MO

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


class Character:
    def __init__(self):
        return


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


def print_character2(itemsDict, leftWidth, rightWidth):
    show_character.insert(tkinter.INSERT, 'PROFIL POSTACI'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        show_character.insert(tkinter.INSERT, k.ljust(
            leftWidth, ' ') + str(v).ljust(rightWidth) + '\n')


def generate():
    create_character()
    print_character2(chr_profile, 20, 40)
    save()


def save():
    chr_file = open('chracter_files.txt', 'a')
    chr_file.write(str(chr_profile)+'\n\n')
    chr_file.close()


# GUI in tkinter

root = tkinter.Tk()
root.title('NPC Generator')

# Lewa część okna
options_frame = tkinter.LabelFrame(root, text='Opcje postaci', padx=10, pady=10)
options_frame.grid(row=0, column=0, sticky=tkinter.NS)

clicked1 = tkinter.StringVar()
clicked1.set('Random')
clicked2 = tkinter.StringVar()
clicked2.set('Random')

gender_list = tkinter.OptionMenu(options_frame, clicked1, 'Mężczyzna', 'Kobieta', 'Random')
gender_list.grid(row=0, column=0)

job_list = tkinter.OptionMenu(
    options_frame,
    clicked2,
    'Antykwariusz',
    'Policjant',
    'Lekarz',
    'Farmer',
    'Bibliotekarz')
job_list.grid(row=1, column=0)

button_generate = tkinter.Button(
    options_frame, text='Generuj', font=('Helvetica', 10), command=generate)
button_generate.grid(row=2, column=0)


def clear():
    pass
    # show_character.delete(0, tkinter.END)


button_clear = tkinter.Button(
    options_frame, text='Wyczyść', font=('Helvetica', 10), command=clear)
button_clear.grid(row=3, column=0)

# Środkowa część okna
results_frame = tkinter.LabelFrame(root, text='Statystyki Postaci:', padx=10, pady=10)
results_frame.grid(row=0, column=1, sticky=tkinter.NS)

show_character = tkinter.Text(results_frame, width=60, height=20)
show_character.pack()

# Prawa strona okna
extra_options_frame = tkinter.LabelFrame(root, text='Zdjęcie Postaci', padx=10, pady=10)
extra_options_frame.grid(row=0, column=2, sticky=tkinter.NS)

char_image = ImageTk.PhotoImage(Image.open('support/images/test.jpg').resize(
    (200, 300), resample=Image.ANTIALIAS))
show_image = tkinter.Label(extra_options_frame, image=char_image)
button_save = tkinter.Button(extra_options_frame, text='Save', anchor=tkinter.S)
button_exit = tkinter.Button(extra_options_frame, text='Exit', command=root.quit, anchor=tkinter.S)

show_image.grid(row=0, column=0, columnspan=2)
button_save.grid(row=1, column=0)
button_exit.grid(row=1, column=1)


root.mainloop()
# Sprawdzenie poprawności
# print(lastName)
# print(lastName['Nazwa'][5])
# print(range(len(lastName['Numery'])))
# print(type(lastName['Numery'][5]))
# print(losuj(manName, 'first names', 'E202'))
# print(losuj(lastName, 'last names', 'F1002'))
