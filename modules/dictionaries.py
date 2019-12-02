# Słowniki wykorzystywane w npcGeneratorze
import random

ZAWODY = {
    'Antykwariusz': (30, 70),
    'Bogaty hobbysta': (50, 90),
    'Detektyw Policyjny': (20, 50),
    'Arytsta': (5, 50)
}

KRZEPA_MO = {
    'Zakres': [64, 84, 124, 164, 204, 283, 364, 444, 524],
    'MO': ['-2', '-1', '0', '+1K4', '+1K6', '+2K6', '+3K6', '+4K6', '+5K6'],
    'Krzepa': [-2, -1, 0, 1, 2, 3, 4, 5, 6]
}

WIEK = {
    'Zakres': [19, 39, 49, 59, 69, 79, 90],
    'Ruch': [0, 0, -1, -2, -3, -4, -5]
}

WIEK = {
    'Zakres': [19, 39, 49, 59, 69, 79, 90],
    'Ruch': [0, 0, -1, -2, -3, -4, -5],
    'Mod_cech': [5, 0, 5, 10, 20, 40, 80],
    'Mod_wyg': [0, 0, 5, 10, 15, 20, 25],
    'Mod_wyk': [0, 1, 2, 3, 4, 4, 4]
}


ALL_SKILLS = ['Aktorstwo', 'Antropologia', 'Archeologia', 'Astronomia', 'Walka Wręcz (Bicz)',
              'Walka Wręcz (Bijatyka)', 'Biologia', 'Botanika', 'Broń Artyleryjska', 'Broń Ciężka',
              'Broń Krótka', 'Broń Obuchowa', 'Charakteryzacja', 'Chemia', 'Czytanie z Ruchu Warg',
              'Elektryka', 'Fałszerstwo', 'Farmacja', 'Fizyka', 'Fotografia',
              'Gadanina', 'Garota', 'Geologia', 'Hipnoza', 'Historia', 'Inżynieria', 'Jeździectwo',
              'Język Obcy: Niemiecki', 'Język Obcy: Francuski', 'Język Obcy: Hiszpański',
              'Język Obcy: Łacina', 'Język Obcy: Greka', 'Język Obcy: Inny', 'Język Ojczysty',
              'Karabin/Strzelba', 'Karabin Maszynowy', 'Korzystanie z bibliotek', 'Kryminalistyka',
              'Kryptografia', 'Księgowość', 'Łuk', 'Majętność', 'Matematyka',
              'Materiały Wybuchowe', 'Mechanika', 'Medycyna', 'Meteorologia', 'Miecz',
              'Miotacz Ognia', 'Nasłuchiwanie', 'Nawigacja', 'Nurkowanie',
              'Obsługa Ciężkiego Sprzętu', 'Okultyzm', 'Perswazja',
              'Pierwsza Pomoc', 'Pilotowanie: samolot', 'Pilotowanie: łódż', 'Piła Łańcuchowa',
              'Pistolet Maszynowy', 'Pływanie', 'Prawo', 'Prowadzenie Samochodu', 'Psychoanaliza',
              'Psychologia', 'Rzucanie', 'Skakanie', 'Spostrzegawczość', 'Sztuka Przetrwania',
              'Sztuki Piękne', 'Ślusarstwo', 'Topór/Siekiera', 'Tresura Zwierząt', 'Tropienie',
              'Ukrywanie', 'Unik', 'Urok Osobisty', 'Wiedza o Naturze', 'Wiedza Tajemna',
              'Włócznia', 'Wspinaczka', 'Wycena', 'Zastraszanie', 'Zoologia', 'Zręczne Palce',
              'Fryzjerstwo', 'Grancarstwo', 'Hutnictwo', 'Kaligrafia', 'Pisarstwo', 'Rzeźba',
              'Stolarstwo', 'Gotowanie', 'Malarstwo', 'Śpiew']

SPEC = {'I': ('Gadanina', 'Perswazja', 'Urok Osobisty', 'Zastraszanie'),
        'J': ('Język Obcy: Niemiecki', 'Język Obcy: Francuski', 'Język Obcy: Hiszpański',
              'Język Obcy: Łacina', 'Język Obcy: Greka', 'Język Obcy: Inny'),
        'WW': ('Walka Wręcz (Bicz)', 'Walka Wręcz (Bijatyka)', 'Broń Obuchowa',
               'Garota', 'Miecz', 'Piła Łańcuchowa',
               'Topór/Siekiera', 'Włócznia'),
        'P': ('Pilotowanie: samolot', 'Pilotowanie: łódź'),
        'BP': ('Broń Ciężka', 'Broń Krótka', 'Karabin/Strzelba',
               'Karabin Maszynowy', 'Łuk', 'Miotacz Ognia',
               'Pistolet Maszynowy'),
        'N': ('Astronomia', 'Biologia', 'Botanika',
              'Chemia', 'Farmacja', 'Fizyka',
              'Geologia', 'Inżynieria', 'Kryminalistyka',
              'Kryptografia', 'Matematyka', 'Meteorologia',
              'Zoologia'),
        'SR': ('Aktorstwo', 'Fałszerstwo', 'Fotografia',
               'Sztuki Piękne', 'Fryzjerstwo', 'Grancarstwo',
               'Hutnictwo', 'Kaligrafia', 'Pisarstwo',
               'Rzeźba', 'Stolarstwo', 'Gotowanie',
               'Malarstwo', 'Śpiew', 'Taniec'),
        'D': ALL_SKILLS
        }

JOB_SKILLS = {'Antykwariusz': (('Korzystanie z bibliotek', 'Historia', 'Spostrzegawczość',
                                'Wycena'), (((1, 'SR'), (1, 'I'), (1, 'D'), (1, 'J')))),
              'Artysta': (('Psychologia', 'Spostrzegawczość'),
                          ((1, 'SR'), (1, 'I'), (1, 'J'), (2, 'D')),
                          ('Historia', 'Wiedza o Naturze')),
              'Artysta estradowy': (('Charakteryzacja', 'Nasłuchiwanie', 'Psychologia',
                                     'Aktorstwo'), ((2, 'I'), (2, 'D'))),
              'Atleta':	(('Jeździectwo', 'Pływanie', 'Rzucanie', 'Skakanie',
                          'Walka Wręcz (Bijatyka)',	'Wspinaczka'),	((1, 'I'), (1, 'D'))),
              'Bibliotekarz': (('Język Ojczysty', 'Korzystanie z bibliotek',
                                'Księgowość'), ((1, 'J'), (4, 'D'))),
              'Bogaty hobbysta': ([('Jeździectwo')], ((1, 'SR'), (1, 'I'), (1, 'BP'),
                                                      (3, 'D'), (1, 'J'))),
              'Człowiek plemienny': (('Nasłuchiwanie', 'Okultyzm', 'Pływanie', 'Spostrzegawczość',
                                      'Sztuka Przetrwania', 'Wiedza o Naturze', 'Wspinaczka'),
                                     (), ('Rzucanie', (1, 'WW')))
              }


def temp(zawod):
    result = []
    for i in JOB_SKILLS[zawod][0]:
        result.append(i)
    for i in JOB_SKILLS[zawod][1]:
        result = result + random.sample(SPEC[i[1]], i[0])
    if len(JOB_SKILLS[zawod]) > 2:
        for i in JOB_SKILLS[zawod][2:]:
            result.append(random.choice(i))
    return result


# for i in range(10):
#     zawod = random.choice(['Antykwariusz', 'Artysta'])
#     print(f'{zawod}: {temp(zawod)}')
