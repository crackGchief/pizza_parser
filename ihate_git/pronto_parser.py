import time

start_time = time.time()

from pronto_parser import result_pronto, menu
from allo_parser import result_allo
from vivat_parser import result_vivat

import xlsxwriter as xlsx

'''def button(worksheet):
    worksheet.insert_button('A50', {'macro': 'rodrigo',
                                   'caption': 'Press Me'})'''


def correcr_pronto(weight):
    for i in range(len(weight)):
        weight[i] = weight[i][1:-1]
    return weight


def vivat_data(result, worksheet):
    menu = ['Маргарита', 'Пепперони', '4 сыра', 'Классика', 'Мясная делюкс', 'Мексиканская', 'Сальмоне']
    prices = []
    weight = []
    average_prices = []
    for i in menu:
        prices.extend(['', '', result[i][1], result[i][5], result[i][9], '', '', result[i][3], result[i][7],
                       result[i][11]])
        weight.extend(['', '', result[i][0], result[i][4], result[i][8], '', '', result[i][2], result[i][6],
                       result[i][10]])
        average_prices.extend(['', '', round(int(result[i][1])/int(result[i][0]), 2), round((result[i][5])/int(result[i][4]), 2),
                              round(int(result[i][9])/int(result[i][8]), 2), '', '', round(int(result[i][3])/int(result[i][2]), 2),
                              round(int(result[i][7])/int(result[i][6]), 2), round(int(result[i][11])/int(result[i][10]), 2)])
    for i in range(2):
        prices.remove('')
        weight.remove('')
        average_prices.remove('')
    worksheet.write_column('E3', prices)
    worksheet.write_column('F3', weight)
    worksheet.write_column('G3', average_prices)


def pronto_data(result, worksheet):
    menu = ['Маргарита', 'Пепперони', '4 сыра', 'С ветчиной и грибами', 'Много мяса', 'Дьявола', 'Пронтиссимо Фирменная']
    prices = []
    weight = []
    average_prices = []
    for i in menu:
        prices.extend(['', '', '', '', '', '', '', '', result[i][0],result[i][1]])
        weight.extend(['', '', '', '', '', '', '', '', result[i][2],result[i][3]])
        average_prices.extend(['', '', '', '', '', '', '', '', round(int(result[i][0])/int(result[i][2]), 2),
                               round(int(result[i][1])/int(result[i][3]), 2)])
    for i in range(2):
        prices.remove('')
        weight.remove('')
        average_prices.remove('')
    worksheet.write_column('B3', prices)
    worksheet.write_column('C3', weight)
    worksheet.write_column('D3', average_prices)


def allo_data(result, worksheet):
    menu = ['Маргарита', 'Пепперони', 'Четыре сыра', 'Ветчина и грибы', 'Мясная', 'Мехико', 'Морская де Люкс']
    prices = []
    weight = []
    average_prices = []

    for i in menu:
        weight.extend(['', '', result[i][0], result[i][2], result[i][6], '', '', '', result[i][4], result[i][8]])
        prices.extend(['', '', result[i][1], result[i][3], result[i][7], '', '', '', result[i][5], result[i][9]])
        average_prices.extend(['', '', round(int(result[i][1])/int(result[i][0]), 2), round(int(result[i][3])/int(result[i][2]), 2),
                               round(int(result[i][7])/int(result[i][6]), 2), '', '', '', round(int(result[i][5])/int(result[i][4]), 2),
                               round(int(result[i][9])/int(result[i][8]), 2)])
    for i in range(2):
        prices.remove('')
        weight.remove('')
        average_prices.remove('')
    worksheet.write_column('H3', prices)
    worksheet.write_column('I3', weight)
    worksheet.write_column('J3', average_prices)


menu = ["Маргарита", "Пепперони", "4 сыра", "С ветчиной и грибами", "Мясная", "Мексиканская", "Сальмоне"]
pizza = ['Пиццы', 'Пронто', '', '', 'Виват', '', '', 'Аллоха', '', '', 'Средняя']
tag = ['Цена, руб', 'Вес, г', 'руб за грамм']
tags = ['']
for i in range(4):
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
vivat_data(result_vivat, worksheet)

#button(worksheet)
worksheet.set_row(0, 15, bold_cell)
worksheet.set_column(0, len(tags), 35, bold_cell)

workbook.close()

print("--- %s seconds ---" % (time.time() - start_time))
