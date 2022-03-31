from pronto_parser import result_pronto, menu
from allo_parser import result_allo
'''from vivat_parser import result_vivat'''

import xlsxwriter as xlsx
import pandas as pd

'''def button(worksheet):
    worksheet.insert_button('A50', {'macro': 'rodrigo',
                                   'caption': 'Press Me'})'''

def correcr_pronto(weight):
    for i in range(len(weight)):
        weight[i] = weight[i][1:-1]
    return weight

def pronto_data(result, worksheet):
    prices = []
    weight = []
    for i in result.keys():
        for j in range(len(result[i]) - 1):
            if result[i][j].split(':')[1][0] != '"' and result[i][j + 1].split(':')[1][0] != '"':
                prices.extend([''] * 8 + [result[i][j].split(':')[1], result[i][j + 1].split(':')[1]])
                j += 1
            elif result[i][j].split(':')[1][0] == '"' and result[i][j + 1].split(':')[1][0] == '"':
                weight.extend([''] * 8 + [result[i][j].split(':')[1], result[i][j + 1].split(':')[1]])
                j += 1
    weight = correcr_pronto(weight)
    for i in range(2):
        prices.remove('')
        weight.remove('')
    worksheet.write_column('B3', prices)
    worksheet.write_column('C3', weight)

def allo_data(result, worksheet):
    menu = ['Маргарита', 'Пепперони', 'Четыре сыра', 'Ветчина и грибы', 'Мясная', 'Мехико', 'Морская де Люкс']

    prices = []
    weight = []

    for i in menu:
        weight.extend(['', '', result[i][0], result[i][2], result[i][6], '', '', '', result[i][4], result[i][8]])
        prices.extend(['', '', result[i][1], result[i][3], result[i][7], '', '', '', result[i][5], result[i][9]])
    for i in range(2):
        prices.remove('')
        weight.remove('')
    worksheet.write_column('F3', prices)
    worksheet.write_column('G3', weight)

menu = ["Маргарита","Пепперони","4 сыра","С ветчиной и грибами","Мясная","Мексиканская","Сальмоне"]
pizza = ['Пиццы', 'Пронто', '', 'Виват', '',  'Аллоха']
tag = ['Цена, руб', 'Вес, г']
tags = ['']
for i in range(3):
    tags.extend(tag)
temp_arr = []
workbook = xlsx.Workbook('pizza_table.xlsx')
worksheet = workbook.add_worksheet()
bold_cell = workbook.add_format({'bold': True})


for i in range(len(menu)):
    temp_arr.extend([menu[i] + ' маленькая', menu[i] + ' средняя', menu[i] + ' большая', '', '',
                     menu[i] + ' мальнькая тонк', menu[i] + ' средняя тонк', menu[i] + ' большая тонк', '', ''])


worksheet.write_column('A3', temp_arr)
worksheet.write_row('A2', tags)
worksheet.write_row('A1', pizza)

pronto_data(result_pronto, worksheet)
allo_data(result_allo, worksheet)

#button(worksheet)
worksheet.set_row(0, 15, bold_cell)
worksheet.set_column(0, len(tags), 35, bold_cell)

workbook.close()
