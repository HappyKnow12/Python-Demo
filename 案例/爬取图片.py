import requests
from bs4 import BeautifulSoup
import os

def get_imgs(root_url):
    res = requests.get(root_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    list = soup.find('div', class_='list').find_all('li')
    imgs = []
    for item in list:
        img_url = item.find('img')['src']
        imgs.append(img_url)

    for img in imgs:
        img_res = requests.get(img)
        filename = os.path.basename(img)
        with open(f'图片/{filename}', 'wb') as file:
            file.write(img_res.content)

get_imgs('http://www.netbian.com/s/haokanmeinv/index_3.htm')