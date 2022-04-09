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
        prices.extend(['', '', int(result[i][1]), int(result[i][5]), int(result[i][9]), '', '', int(result[i][3]), int(result[i][7]),
                       int(result[i][11])])
        weight.extend(['', '', int(result[i][0]), int(result[i][4]), int(result[i][8]), '', '', int(result[i][2]), int(result[i][6]),
                       int(result[i][10])])
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
        prices.extend(['', '', '', '', '', '', '', '', int(result[i][0]),int(result[i][1])])
        weight.extend(['', '', '', '', '', '', '', '', int(result[i][2]),int(result[i][3])])
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
        weight.extend(['', '', int(result[i][0]), int(result[i][2]), int(result[i][6]), '', '', '', int(result[i][4]), int(result[i][8])])
        prices.extend(['', '', int(result[i][1]), int(result[i][3]), int(result[i][7]), '', '', '', int(result[i][5]), int(result[i][9])])
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


def average(worksheet):

    for i in range(3, 71):
        if i not in [6,7,11,12,16,17,21,22,26,27,31,32,36,37,41,42,46,47,51,52,56,57,61,62,66,67]:
            worksheet.write(f'K{i}', f'=ROUND(AVERAGE(B{i}, E{i}, H{i}))')
            worksheet.write(f'L{i}', f'=ROUND(AVERAGE(C{i}, F{i}, I{i}))')
            worksheet.write(f'M{i}', f'=ROUND(AVERAGE(D{i}, G{i}, J{i}), 2)')
        else:
            pass

menu = ["Маргарита", "Пепперони", "4 сыра", "С ветчиной и грибами", "Мясная", "Мексиканская", "Сальмоне"]
pizza = ['Пиццы', 'Пронто', '', '', 'Виват', '', '', 'Аллоха', '', '', 'Средняя', '', '']
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

format_names = workbook.add_format({'bg_color': '99CCFF', 'border': 4})
format_pizza = workbook.add_format({'bg_color': 'FFCC99', 'border': 4})

worksheet.write_column('A3', temp_arr, format_pizza)
worksheet.write_row('A2', tags, format_names)
worksheet.write_row('A1', pizza, format_names)

pronto_data(result_pronto, worksheet)
allo_data(result_allo, worksheet)
vivat_data(result_vivat, worksheet)
average(worksheet)
#button(worksheet)
worksheet.set_row(0, 15, bold_cell)
worksheet.set_column(0, len(tags), 35, bold_cell)

workbook.close()

print("--- %s seconds ---" % (time.time() - start_time))
