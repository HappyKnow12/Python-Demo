import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def get_list(page_num):
    url = 'https://www.cnblogs.com/AggSite/AggSitePostList'
    data = {
        "CategoryType": "SiteHome",
        "ParentCategoryId": 0,
        "CategoryId": 808,
        "PageIndex": page_num,
        "TotalPostCount": 4000,
        "ItemListActionName": "AggSitePostList"
    }

    headers = {
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    res = requests.post(url, json.dumps(data), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_list_dom = soup.find_all('article', class_='post-item')
    article_list = []
    for article_dom in article_list_dom:
        title = article_dom.find('a', class_='post-item-title').get_text()
        footer = article_dom.find('footer', class_='post-item-foot')
        author = footer.find('a', class_='post-item-author').find('span').get_text()
        time = footer.find('span', class_='post-meta-item').find('span').get_text()
        btns = footer.find_all('a', class_='post-meta-item btn')
        digg = btns[0].find('span').get_text()
        comments = btns[1].find('span').get_text()
        read = btns[2].find('span').get_text()
        article_list.append([title, author, time, digg, comments, read])
    return article_list

list = []
for index in range(20):
    list.extend(get_list(index))

df = pd.DataFrame(list, columns=['标题', '作者', '创建时间', '点赞数', '评论数', '阅读数'])
df.to_excel('博客园20页文章信息.xlsx', index=False)