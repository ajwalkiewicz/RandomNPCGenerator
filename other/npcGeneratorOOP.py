# Generator NPC napisany obiektowo
import random
import shelve
from os import path


class Character():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class MainTraits(Character):
    pass


class Skills(Character):
    pass


shelv_file = shelve.open(path.join("support", "myData"))
man_name = shelv_file['man_name']
woman_name = shelv_file['woman_name']
last_name = shelv_file['last_name']


def losuj(dictionary, workbook):
    '''Funkcja losująca imie i nazwisko'''
    # sheet = excel_file[workbook]
    number = random.randint(0, dictionary['Numery'][-1])  # int(sheet[cell].value))
    for i in range(len(dictionary['Numery'])):
        if number < dictionary['Numery'][i]:
            return dictionary['Nazwa'][i]
    return 'wtf?'


character = Character(losuj(man_name, 'first names'), losuj(last_name, 'last names'))
print(character.name, character.last_name)
