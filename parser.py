from bs4 import BeautifulSoup
with open('C:/Users/User/Desktop/Новая папка/Elon Musk Discusses War, AI, Aliens, and Humanity _ Lex Fridman Podcast #400 — Eightify.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    list_txt = f'\t\t\t\t{soup.h1.text}\n'
    head_text = soup.find('div', class_='tldr').get_text()
    list_txt += head_text + '\n'
    div = soup.find('div', class_='insights-block')
    list_h3 = [h3.get_text() for h3 in div.find_all('h3')]
    for i, ul in enumerate(div.find_all('ul', class_='insights')):  #  2
        li = ul.find_all('li', class_='insights-item')
        list_txt += f'\t\t{list_h3[i]}\n'
        for el in li:  #  7
            a = el.find_all('div')[1]
            list_txt += a.get_text()+'\n'  #  len(list_txt) : 10
    faq = soup.find('div', class_='faq-block')
    txt2 = faq.find('h2').get_text()
    for q in faq.find_all('li', class_='qa-list__item'):
        txt2 += f"\n\t{q.find('p').get_text()}\n"
        a = q.find_all('span')[1]
        txt2 += f"- {a.get_text()}\n"
    div = soup.find('div', class_='timestamped-summary')
    txt2 += f"\n\t\t{div.find('h2').get_text()}\n"
    li_time = [i for i in div.find_all('span', class_='key-ideas-item__timestamp')]
    li_text = [i for i in div.find_all('div', class_='key-ideas-item__title')]
    for i in range(len(li_time)):
        txt2 += li_time[i].get_text()
        txt2 += li_text[i].get_text() + '\n'
    print(txt2)
