import requests
from bs4 import BeautifulSoup
import time


def da_importa(a):
    b = []
    for i in range(len(a)):
        if a[i].isdigit():
            if a[i + 2].isdigit() and a[i + 3].isdigit() == False and a[i - 1].isdigit() == False:
                b.append(int(a[i]) * 100 + int(a[i + 1]) * 10 + int(a[i + 2]))
            if a[i + 3].isdigit():
                b.append(int(a[i]) * 1000 + int(a[i + 1]) * 100 + int(a[i + 2]) * 10 + int(a[i + 3]))
    return b


def change_hrefs(hrefs):
    new_hrefs = []
    add = 'msk/all/'
    for i in hrefs:
        tmp1 = i[:21]
        tmp2 = i[21:]
        res = tmp1 + add + tmp2
        new_hrefs.append(res)
    return new_hrefs

def change_info(info):
    for i in range(len(info)):
        tmp = ''
        info[i] = info[i][29:]
        tmp = info[i][:8]
        tmp += info[i][28:33]
        tmp += info[i][52:]
        info[i] = tmp
        info[i] = info[i].replace('t1', 'Традиционное')
        info[i] = info[i].replace('t2', 'Тонкое')
    return info


def get_info(hrefs, main_menu):
    result = {}
    k = 0
    for i in hrefs:
        temp_arr = []
        one_content = requests.get(i)
        soup = BeautifulSoup(one_content.text, 'lxml')
        something = str(str(soup).split("window.dataProduct")[1]).split("iiko_products")[0]
        new_something = str(something).split("measureUnit")
        for j in range(1, len(new_something)):
            temp_arr.append(new_something[j].split("modifiers_groups")[0])
        temp_arr = change_info(temp_arr)
        temp_arr = ",".join(temp_arr)+"костылище"
        result.setdefault(main_menu[k], da_importa(temp_arr))
        k += 1
    return result

start_time = time.time()
url = 'https://allopizza.su/msk/all#pizza'
example = ['Маргарита', 'Пепперони', 'Мехико', 'Четыре сыра', 'Ветчина и грибы', 'Мясная', 'Морская де Люкс']
allo_content = requests.get(url)
soup = BeautifulSoup(allo_content.text,"lxml")
match = soup.find_all("a")
main_menu = []
hrefs = []
for i in match:
    if i.text in example:
        main_menu.append(i.text)
        hrefs.append(i.get('href'))
hrefs = change_hrefs(hrefs)
result_allo = get_info(hrefs, main_menu)



#print("--- %s seconds ---" % (time.time() - start_time))