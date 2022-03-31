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


def new_url(url):
    upgraded_spisok = []
    dodo_content = requests.get(url)
    soup = BeautifulSoup(dodo_content.text, "lxml")
    spisok = str(soup.text).split("Размер и тесто")
    new_spisok = str(spisok[1]).split("Бортик")
    new_spisok[0] = new_spisok[0].replace('\t','')
    new_spisok[0] = new_spisok[0].replace('\r','')
    new_spisok[0] = new_spisok[0].replace('\n','')
    return da_importa(new_spisok[0])






def href_manager(spisok, menu):
    result = {}
    for href in range(len(hrefs)):
        url = "https://www.vivatpizza.ru" + hrefs[href]
        result.setdefault(menu[href], new_url(url))
    return result

start_time = time.time()
result = {}
menu = ["Маргарита", "Пепперони", "4 сыра", "Классика", "Мясная делюкс", "Сальмоне", "Мексиканская"]

current_menu = []
dodo_content = requests.get("https://www.vivatpizza.ru/menu/traditional-pizza")
soup = BeautifulSoup(dodo_content.text, "lxml")
match = soup.find_all("a")
hrefs = []

for i in match:
    if i.text in menu:
        current_menu.append(i.text)
        hrefs.append(i.get("data-popup-href"))
result_vivat = href_manager(hrefs, current_menu)
#print(result_vivat)
"Тонкое м г ц, Пышное м г ц"

#https://www.vivatpizza.ru/popup/constructor?constructorId=4f5ffd98-98e7-460d-ab31-272d22e23bd5
#print("--- %s seconds ---" % (time.time() - start_time))