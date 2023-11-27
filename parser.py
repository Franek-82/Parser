def func(url, n):
    import requests
    from bs4 import BeautifulSoup
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/88.0.4324.96 Safari/537.36"}
    res = requests.get(url, headers=headers)
    print(n, url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'lxml')
        txt = f'\n{n}\n{url}\n\t\t{soup.h1.text}\n'
        head_text = soup.find('div', class_='tldr').get_text()
        txt += head_text  # + '\n'
        #  Первый блок insights-block
        div = soup.find('div', class_='insights-block')
        if div:
            if div.find('h3'):
                list_head = [h3.get_text() for h3 in div.find_all('h3')]
            else:
                # "Key insights" ---- Список из 1 элемента (заголовка)
                list_head = [el.text for el in div.select('.insights-block > h2')]
                # print(list_head)
            for i, ul in enumerate(div.find_all('ul', class_='insights')):  #  1
                list_of_li = ul.find_all('li', class_='insights-item')
                txt += '\n\t' + list_head[i] + '\n'
                for el in list_of_li:  #  7
                    a = el.find_all('div')[1]
                    txt += a.get_text() + '\n'
        #  Второй блок FAQ
        faq = soup.find('div', class_='faq-block')
        if faq:
            txt += faq.find('h2').get_text()
            for q in faq.find_all('li', class_='qa-list__item'):
                txt += f"\n\t{q.find('p').get_text()}\n"
                a = q.find_all('span')[1]
                txt += f"- {a.get_text()}\n"
        #  Третий блок Timestamped Summary
        div_time = soup.find('div', class_='timestamped-summary')
        if div_time:
            txt += f"\n\t\t{div_time.find('h2').get_text()}\n"
            li_time = [i for i in div_time.find_all('span', class_='key-ideas-item__timestamp')]
            li_text = [i for i in div_time.find_all('div', class_='key-ideas-item__title')]
            for i in range(len(li_time)):
                txt += li_time[i].get_text()
                txt += li_text[i].get_text() + '\n'
        return txt
    else:
        print("!!", res.status_code)
