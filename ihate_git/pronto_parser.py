import requests
from bs4 import BeautifulSoup
import time


def find_size(spisok):
    catalog = []
    new_spisok_mid = spisok[1]
    new_spisok_mid = new_spisok_mid.split(",")
    new_spisok_large = spisok[2]
    new_spisok_large = new_spisok_large.split(",")
    for i in range(2):
        catalog.append(new_spisok_mid[i+1])
        catalog.append(new_spisok_large[i+1])
    cataloge.append(catalog)


def new_url(url):
    dodo_content = requests.get(url)
    soup = BeautifulSoup(dodo_content.text, "lxml")
    match = soup.find("form", class_="item js-widget item_detail")
    spisok = str(match).split("catalog_item")
    find_size(spisok)


def href_manager(spisok):
    for href in range(len(hrefs)):
        url = "https://pronto24.ru" + hrefs[href]
        new_url(url)

start_time = time.time()
menu = ["Маргарита","Пепперони","4 сыра","С ветчиной и грибами","Много мяса","Дьявола","Пронтиссимо Фирменная"]
dodo_content = requests.get("https://pronto24.ru/catalog/category/picca")
soup = BeautifulSoup(dodo_content.text, "lxml")
match = soup.find_all("a")
hrefs , cataloge= [], []
for pizza in menu:
    for i in match:
        if i.text == pizza:
            hrefs.append(i.get("href"))
href_manager(hrefs)
result_pronto = dict(zip(menu,cataloge))
