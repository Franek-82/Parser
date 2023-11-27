from Parser import func
from time import sleep
import requests
from bs4 import BeautifulSoup
n = 0
for numb in range(1, 999):
    root = f'https://eightify.app/summary/miscellaneous/page-{numb}'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/88.0.4324.96 Safari/537.36"}
    res = requests.get(root, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    tag_main = soup.find('main')
    if numb == 1:
        my_text = 'Eightify'.center(30)
        title = tag_main.find('h1', class_='h1').text
        my_text += '\n\t' + title + '\n'
        my_text += tag_main.find('div', class_='article').text
        with open('C:/Users/rick1/Desktop/Parsing/my_file.txt', 'w', encoding='utf-8') as f:
            f.write(my_text)
    soup_tag = tag_main.find('div', class_='grid-container')
    li = soup_tag.find_all('div', class_='card')
    if li:
        #  Если у <div class='grid-container'> есть дочерний тэг, то идет выполнение нижнего кода
        for card in li:  # 18
            sleep(3)
            url = card.find('a').get('href')
            res = requests.get(url, headers=headers)
            with open('C:/Users/rick1/Desktop/Parsing/my_file.txt', 'a', encoding='utf-8') as f:
                n += 1
                f.write(func(url, n))
    else:
        break
