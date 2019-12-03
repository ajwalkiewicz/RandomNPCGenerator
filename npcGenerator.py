'''
Program ten generuje losowych NPC Do gry Zew Cthulu
Wszystkie słowniki zostały wytworzone za pomocą creatingDict.py
Tutaj jedynie za pomocą modułu shelve zostały zimportowane zmienne
'''

# import bibliotek
import random
import shelve
import modules.dictionaries
from os import path
import tkinter
from PIL import ImageTk, Image

# Zmienne globalne
shelv_file = shelve.open(path.join("support", "myData"))
man_name = shelv_file['man_name']
woman_name = shelv_file['woman_name']
last_name = shelv_file['last_name']
all_skills = shelv_file['skills']
# zaimportuj JOB_SKILLS z shelve a następnie usuń importowanie JOB_SKILLS
# z dictionaries.py
KRZEPA_MO = modules.dictionaries.KRZEPA_MO
ZAWODY = modules.dictionaries.ZAWODY
WIEK = modules.dictionaries.WIEK
ALL_SKILLS = modules.dictionaries.ALL_SKILLS
SPEC = modules.dictionaries.SPEC
JOB_SKILLS = modules.dictionaries.JOB_SKILLS

# Słownik profilu postaci

chr_profile = {'Imie': '', 'Nazwisko': '', 'Płeć': '', 'Zawód': '', 'Wiek': 0,
               'S': 0, 'KON': 0, 'BC': 0, 'ZR': 0, 'WYG': 0,
               'INT': 0, 'MOC': 0, 'WYK': 0, 'PS': 0, 'Ruch': 0,
               'PW': 0, 'PP': 0, 'PM': 0, 'MO': 0, 'Krzepa': 0,
               # 'Punkty': 0,
               }


MAJETNOSC = {
    'Antykwariusz': (30, 70), 'Artysta estradowy': (9, 70), 'Atleta': (9, 70),
    'Bibliotekarz': (9, 35), 'Człowiek plemienny': (0, 15), 'Duchowny': (9, 60),
    'Bogaty hobbysta': (50, 90), 'Detektyw Policyjny': (20, 50), 'Artysta': (5, 50),
    'Dziennikarz': (9, 30), 'Fanatyk': (0, 30), 'Farmer': (9, 30),
    'Inżynier': (30, 60), 'Lekarz': (30, 80), 'Misjonarz': (0, 30),
    'Muzyk': (9, 30), 'Oficer policji': (9, 30), 'Oficer wojskowy': (20, 70),
    'Parapsycholog': (9, 30), 'Pilot': (20, 70), 'Pisarz': (9, 30),
    'Prawnik': (30, 80), 'Profesor': (20, 70), 'Prywatny detektyw': (9, 30),
    'Przestępca': (5, 65), 'Włóczęga': (0, 5), 'Żołnierz': (9, 30)
}

# Losowanie zawodu
LISTA_ZAWODOW = (
    ('Antykwariusz', 'Duchowny', 'Bibliotekarz',
     'Dziennikarz', 'Inżynier', 'Lekarz',
     'Misjonarz', 'Parapsycholog', 'Pisarz',
     'Prawnik', 'Profesor'),  # 1
    ('Artysta', 'Fanatyk', 'Muzyk'),  # 2
    ('Artysta', 'Detektyw Policyjny', 'Atleta',
     'Człowiek plemienny', 'Farmer', 'Muzyk',
     'Oficer policji', 'Oficer wojskowy', 'Pilot',
     'Prywatny detektyw', 'Przestępca', 'Włóczęga',
     'Żołnierz'),  # 3
    ('Bogaty hobbysta', 'Artysta estradowy', 'Fanatyk',
     'Włóczęga'),  # 4
    ('Detektyw Policyjny', 'Atleta', 'Człowiek plemienny',
     'Farmer', 'Oficer policji', 'Oficer wojskowy',
     'Prywatny detektyw', 'Przestępca', 'Włóczęga',
     'Żołnierz'))  # 5

# Do usunięcia po zastosowaniu importowania danych z excela
job_skills = ['Psychoanaliza', 'Prowadzenie Samochodu', 'Prawo', 'Pływanie',
              'Pistolet Maszynowy', 'Piła Łańcuchowa', 'Pierwsza Pomoc',
              'Perswazja', 'Okultyzm', 'Obsługa Ciężkiego Sprzętu', 'Nurkowanie',
              'Nawigacja', 'Nasłuchiwanie', 'Miotacz Ognia', 'Miecz',
              'Meteorologia', 'Medycyna']
job_skills = [i.lower() for i in job_skills]


def losuj_zawod(zaw='Optymalny'):
    global LISTA_ZAWODOW
    global skill_points
    global hobby_points

    lista_punktow = (
        chr_profile['WYK']*4,  # 1
        chr_profile['WYK']*2 + chr_profile["MOC"]*2,  # 2
        chr_profile['WYK']*2 + chr_profile["ZR"]*2,  # 3
        chr_profile['WYK']*2 + chr_profile["WYG"]*2,  # 4
        chr_profile['WYK']*2 + chr_profile["S"]*2)  # 5

    if zaw == 'Random':
        zawod = random.choice([job for job in MAJETNOSC.keys()])
        chr_profile['Zawód'] = zawod
        pozycja_zaw = [i for i, j in enumerate(LISTA_ZAWODOW) if zawod in j]
        punkty = [i for i in lista_punktow if lista_punktow.index(i) in pozycja_zaw]
        skill_points = max(punkty)
    else:
        skill_points = max(lista_punktow)
        max_punkty = [i for i, j in enumerate(lista_punktow) if j == skill_points]
        pozycja = random.choice(max_punkty)
        if len(LISTA_ZAWODOW[pozycja]) == 1:
            zawod = LISTA_ZAWODOW[pozycja]
        else:
            zawod = random.choice(LISTA_ZAWODOW[pozycja])
        chr_profile['Zawód'] = zawod

    hobby_points = chr_profile['INT']*2
    # chr_profile['Zawód'] =

# Losowanie imion i nazwisk


def losuj(dictionary, workbook):
    '''Funkcja losująca imie i nazwisko'''
    # sheet = excel_file[workbook]
    number = random.randint(0, dictionary['Numery'][-1])  # int(sheet[cell].value))
    for i in range(len(dictionary['Numery'])):
        if number < dictionary['Numery'][i]:
            return dictionary['Nazwa'][i]
    return 'wtf?'


def pochodne(S=0, BC=0, ZR=0):
    '''okreslenie pochodnych cech na podstawie cech głównych'''
    for _ in range(len(KRZEPA_MO['Zakres'])):
        if S + BC <= KRZEPA_MO['Zakres'][_]:
            results = list(
                (KRZEPA_MO['MO'][_], KRZEPA_MO['Krzepa'][_]))
            break
    if ZR:
        if ZR < BC and S < BC:
            results.append('7')
        elif S >= BC and ZR >= BC:
            results.append('9')
        else:
            results.append('8')
    return results


def umiejetnosci(zawod):
    def job_skills(zawod):
        global job_skills
        # if zawod in JOB_SKILLS.keys():
        #     return modules.dictionaries.temp(zawod)
        # else:
        return job_skills

    global skill_points
    job_skills = job_skills(zawod)
    print(job_skills)
    global hobby_points
    global character_skills
    character_skills = all_skills.copy()
    #  Rozwiązać zapamiętywanie skillsów poprzednich postaci - trzeba zresetować all-skills
    credit_rating = random.randint(*MAJETNOSC[zawod])
    character_skills['Majętność'] = credit_rating
    character_skills['Unik'] = chr_profile['ZR'] // 2
    character_skills['Język Ojczysty'] = chr_profile['WYK']
    skill_points -= credit_rating
    #  rozdawanie punktów na umiejętności zawodowe
    while skill_points:
        random.shuffle(job_skills)
        for skill in job_skills:
            #  skill = random.choice(job_skills)
            if 90-character_skills[skill] >= skill_points:
                przydzial_pkt = random.randint(0, skill_points)
            elif character_skills[skill] >= 90:
                continue
            else:
                przydzial_pkt = random.randint(0, 90-character_skills[skill])
            # Sprawdzenie przydziału punktów
            print(
                f'{skill}: {character_skills[skill]}: {przydzial_pkt}, pozostało: {skill_points - przydzial_pkt}')
            character_skills[skill] += przydzial_pkt
            skill_points -= przydzial_pkt
            if skill_points == 0:
                break
    while hobby_points:
        print(hobby_points)
        hobby_list = list(character_skills.keys())
        random.shuffle(hobby_list)
        for skill in hobby_list:
            #  skill = random.choice(character_skills)
            if 90-character_skills[skill] >= hobby_points:
                przydzial_pkt = random.randint(0, hobby_points)
            elif character_skills[skill] >= 90:
                continue
            else:
                przydzial_pkt = random.randint(0, 90-character_skills[skill])
            # Sprawdzenie przydziału punktów
            print(
                f'{skill}: {character_skills[skill]}: {przydzial_pkt}, pozostało: {hobby_points - przydzial_pkt}')
            character_skills[skill] += przydzial_pkt
            hobby_points -= przydzial_pkt
            if hobby_points == 0:
                break

    # rozdawanie punktów na umiejętności z hobbysta
    # while hobby_points:
    #     skill = random.choice(list(all_skills.keys()))
    #     #  skill = random.choice(all_skills)
    #     if 90-all_skills[skill] >= skill_points:
    #         przydzial_pkt = random.randint(0, skill_points)
    #     else:
    #         przydzial_pkt = random.randint(0, 90-all_skills[skill])
    #
    #     all_skills[skill] += przydzial_pkt
    #     hobby_points -= przydzial_pkt
    #     print(hobby_points)


# Generowanie cech postaci


def create_character(zaw, plec):
    gender = {'Mężczyzna': man_name, 'Kobieta': woman_name,
              'Random': random.choice([man_name, woman_name])}
    temp = gender[plec]
    if temp == man_name:
        chr_profile['Płeć'] = 'Mężczyzna'
    if temp == woman_name:
        chr_profile['Płeć'] = 'Kobieta'

    ustawienia_zawodu = zaw

    def main_traits():
        chr_profile['Imie'] = losuj(temp, 'first names')
        chr_profile['Nazwisko'] = losuj(last_name, 'last names')
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
        print(chr_profile['Zawód'])

    def modyfikuj_cechy(Wiek=0, WYG=0, PS=0, Ruch=0):
        if Wiek <= 19:
            pula = 5
            for i in range(pula):
                wybor = [um for um in ('S', 'KON', 'ZR') if chr_profile[um] != 1]
                if wybor:
                    chr_profile[random.choice(wybor)] -= 1
                else:
                    break
            test = random.randint(1, 100)
            if PS < test:
                PS += random.randint(1, 10)
        elif Wiek <= 39:
            test = random.randint(1, 100)
            if chr_profile['WYK'] < test:
                chr_profile['WYK'] += random.randint(1, 10)
        elif Wiek <= 49:
            WYG -= 5
            Ruch = Ruch - 1
            pula = 5
            for i in range(pula):
                wybor = [um for um in ('S', 'KON', 'ZR') if chr_profile[um] != 1]
                if wybor:
                    chr_profile[random.choice(wybor)] -= 1
                else:
                    break
            for i in range(2):
                test = random.randint(1, 100)
                if chr_profile['WYK'] < test:
                    chr_profile['WYK'] += random.randint(1, 10)
        elif Wiek <= 59:
            WYG -= 10
            Ruch = Ruch - 2
            pula = 10
            for i in range(pula):
                wybor = [um for um in ('S', 'KON', 'ZR') if chr_profile[um] != 1]
                if wybor:
                    chr_profile[random.choice(wybor)] -= 1
                else:
                    break
            for i in range(3):
                test = random.randint(1, 100)
                if chr_profile['WYK'] < test:
                    chr_profile['WYK'] += random.randint(1, 10)
        elif Wiek <= 69:
            WYG -= 15
            if WYG < 0:
                WYG = 0
            Ruch = Ruch - 3
            pula = 20
            for i in range(pula):
                chr_profile[random.choice([um for um in ('S', 'KON', 'ZR')
                                           if chr_profile[um] != 1])] -= 1
            for i in range(4):
                test = random.randint(1, 100)
                if chr_profile['WYK'] < test:
                    chr_profile['WYK'] += random.randint(1, 10)
        elif Wiek <= 79:
            WYG -= 20
            if WYG < 0:
                WYG = 0
            Ruch = Ruch - 4
            pula = 40
            for i in range(pula):
                wybor = [um for um in ('S', 'KON', 'ZR') if chr_profile[um] != 1]
                if wybor:
                    chr_profile[random.choice(wybor)] -= 1
                else:
                    break
            for i in range(4):
                test = random.randint(1, 100)
                if chr_profile['WYK'] < test:
                    chr_profile['WYK'] += random.randint(1, 10)
        elif Wiek <= 90:
            WYG -= 25
            if WYG < 0:
                WYG = 0
            Ruch = Ruch - 5
            pula = 80
            for i in range(pula):
                wybor = [um for um in ('S', 'KON', 'ZR') if chr_profile[um] != 1]
                if wybor:
                    chr_profile[random.choice(wybor)] -= 1
                else:
                    break
            for i in range(4):
                test = random.randint(1, 100)
                if chr_profile['WYK'] < test:
                    chr_profile['WYK'] += random.randint(1, 10)
        chr_profile['WYG'] = WYG
        chr_profile['PS'] = PS
        chr_profile['Ruch'] = Ruch

    main_traits()
    modyfikuj_cechy(Wiek=int(chr_profile['Wiek']),
                    WYG=int(chr_profile['WYG']),
                    PS=int(chr_profile['PS']),
                    Ruch=int(chr_profile['Ruch']))
    losuj_zawod(ustawienia_zawodu)
    umiejetnosci(chr_profile['Zawód'])

    return None


# Wyświetlenie profilu postaci


def print_character1(itemsDict, leftWidth, rightWidth):
    print('PROFIL POSTACI'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ' ') + str(v).ljust(rightWidth))


def print_character2(itemsDict, leftWidth, rightWidth):
    show_character.insert(tkinter.INSERT, 'PROFIL POSTACI'.center(
        leftWidth + rightWidth, '-') + '\n')
    for k, v in itemsDict.items():
        show_character.insert(tkinter.INSERT, k.ljust(
            leftWidth, ' ') + str(v).ljust(rightWidth) + '\n')

    show_character.insert(tkinter.INSERT, 'UMIEJĘTNOŚCI'.center(
        leftWidth + rightWidth, '-') + '\n')
    for k, v in sorted(character_skills.items()):
        show_character.insert(tkinter.INSERT, k.capitalize().ljust(
            leftWidth, ' ') + str(v).ljust(rightWidth) + '\n')


def generate():
    create_character(clicked2.get(), clicked1.get())
    print_character1(chr_profile, 30, 20)
    print_character2(chr_profile, 30, 20)
    save()


def save():
    chr_file = open('chracter_files.txt', 'a')
    chr_file.write(str(chr_profile) + str(character_skills) + '\n')
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


gender_list = tkinter.OptionMenu(
    options_frame, clicked1, 'Mężczyzna', 'Kobieta', 'Random')
gender_list.grid(row=0, column=0, sticky=tkinter.EW)

zawody_list = JOB_SKILLS.keys()
occupation_list = ('Random', 'Optymalny', *zawody_list)

job_menu = tkinter.OptionMenu(options_frame, clicked2, *occupation_list)
job_menu.grid(row=1, column=0, sticky=tkinter.EW)

button_generate = tkinter.Button(
    options_frame, text='Generuj', font=('Helvetica', 15), command=generate)
button_generate.grid(row=2, column=0, pady=5, sticky=tkinter.EW)


def clear():
    show_character.delete('1.0', tkinter.END)


button_clear = tkinter.Button(
    options_frame, text='Wyczyść', font=('Helvetica', 10), command=clear)
button_clear.grid(row=3, column=0, pady=5, sticky=tkinter.EW)

# Środkowa część okna
results_frame = tkinter.LabelFrame(root, text='Statystyki Postaci:', padx=10, pady=10)
results_frame.grid(row=0, column=1, sticky=tkinter.NS)

show_character = tkinter.Text(results_frame, width=60, height=30)
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
