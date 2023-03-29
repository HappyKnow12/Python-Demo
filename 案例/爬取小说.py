import requests
from bs4 import BeautifulSoup

def get_xiaoshuo_list(root_url):
    res = requests.get(root_url)
    soup = BeautifulSoup(res.text, 'lxml')
    list_ = soup.find('div', id='list').find_all('a')
    list_url = []
    for index, node in enumerate(list_):
        if index >= 9:
            list_url.append(('http://www.biqugse.com' + node['href'], node.get_text()))
    return list_url

list_url = get_xiaoshuo_list('http://www.biqugse.com/98473/')

def get_xiaoshou_content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.find('div', id='content')
    return content.get_text(separator='\n', strip=True)

with open('开局账号被盗，反手充值一百万.txt', 'a', encoding='utf-8') as fin:
    for url, name in list_url:
        print(url, name)
        fin.write('\n'+name+'\n\n')
        fin.write(get_xiaoshou_content(url))


