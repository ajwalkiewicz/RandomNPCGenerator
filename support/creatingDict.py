'''
Program zapisujący słowniki do pliku dictionaries.txt
creatingDict pobiera dane z komórek (IMIE/NAZWISKO) oraz Numery
a następnie zapisuje je w postaci słownika w następującym schemacie
{"Nazwa":[lista imion],"Numery":[lista numerów]}
'''
import openpyxl
import shelve

# otworzenie excela
excel_file = openpyxl.load_workbook('data.xlsx', data_only=True)
# funkcje tworzące listy imion i nazwisk


def list_creator(workbook, column):
    '''Tworzy listę elementów złożoną z elementów podanej kolumny
    Na wejściu trzeba podać arkusz na którym się pracuje oraz
    columne z któej mają zostac pobrane dane.
    Na wyjściu zwraca listę z wartości komórek z podanej kolumny'''
    return [i.value for i in excel_file[workbook][column][1:-1]]


def dict_creator(lista_nazw, lista_numerow):
    '''Tworzy słownik według schematu:
    {'Nazwa: argument 1', 'Numery': argument 2}'''
    lista_nazw.reverse()
    lista_numerow.reverse()
    return {'Nazwa': lista_nazw, 'Numery': lista_numerow}


def skills_dict_creator(lista_nazw, lista_numerow):
    '''Tworzy słownik dla umiejętności'''
    lista_nazw.reverse()
    lista_numerow.reverse()
    # Pamiętaj by w komórkach w excelu znajdowały się jakieś wartości
    # W przeciwnym razie program zwróci error, ze int() nie moze działać na Nontype
    return {job.casefold().strip():  int(lista_numerow[lista_nazw.index(job)]) for job in lista_nazw}


def job_skills_creator(workbook, column):
    '''Tworzy słownik umiejętności zawodowych. Wg schematu:
    {'Nazwa zawodu': [lista umiejętności zawodowych]}'''
    working_sheet = excel_file[workbook]
    job_skills_list = []
    for i in range(2, len(working_sheet[column])):
        job_skills_list.append([cell.value.casefold().strip() for cell in working_sheet[i][1:]
                                if cell.value is not None])
    occupation_list = list_creator(workbook, column)
    return {job: job_skills for job, job_skills in zip(occupation_list, job_skills_list)}


# Zapisanie wyników w pliku dictionaries.txt
file = open("dictionaries.txt", 'w')
file.write(str(dict_creator(
    list_creator('first names', 'B'), list_creator('first names', 'F')))+'\n\n')
file.write(str(dict_creator(
    list_creator('first names', 'G'), list_creator('first names', 'K')))+'\n\n')
file.write(str(dict_creator(
    list_creator('last names', 'B'), list_creator('last names', 'G')))+'\n\n')
file.close()

file = open('skills.txt', 'w')
file.write(str(skills_dict_creator(
    list_creator('skills', 'A'), list_creator('skills', 'B')))+'\n\n')
file.write(str(job_skills_creator('occupations', 'A')))
file.close()


# zapisanie zmiennych slownikowych w pliku shelve
shelf_file = shelve.open('myData')
shelf_file['man_name'] = dict_creator(
    list_creator('first names', 'B'), list_creator('first names', 'F'))
shelf_file['woman_name'] = dict_creator(
    list_creator('first names', 'G'), list_creator('first names', 'K'))
shelf_file['last_name'] = dict_creator(
    list_creator('last names', 'B'), list_creator('last names', 'G'))
shelf_file['skills'] = skills_dict_creator(
    list_creator('skills', 'A'), list_creator('skills', 'B'))
shelf_file['JOB_SKILLS'] = job_skills_creator('occupations', 'A')

print(shelf_file['skills'])
# Sprawdzenie długości list
if len(shelf_file['man_name']['Nazwa']) == len(shelf_file['man_name']['Numery']):
    print("OK")
else:
    print("ERROR")
