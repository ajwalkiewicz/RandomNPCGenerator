'''
korekcjaExcel.py - zmienia nazwiska zapisane w pliku lista_imion.xlsx
z imion pisanych capslockiem na na imiona pisane z dużej litery
Wyniki zapisywanie są w pliku lista_imion_copy.xlsx
'''
import openpyxl

# otworzenie excela
excel_file = openpyxl.load_workbook('lista_imion.xlsx')


def zmiana(workbook, column):
    sheet = excel_file[workbook]
    for i in range(1, len(sheet[column])):
        sheet.cell(row=i, column=2).value = sheet.cell(
            row=i, column=2).value[0].upper() + sheet.cell(row=i, column=2).value[1:].lower()


zmiana('last names', 'B')
excel_file.save('lista_imion_copy.xlsx')
