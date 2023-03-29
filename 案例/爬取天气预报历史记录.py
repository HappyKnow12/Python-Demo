import requests
import pandas as pd

def craw_weather_forecast(year, month):
    url = 'https://tianqi.2345.com/Pc/GetHistory'
    params = {
        'areaInfo[areaId]': 54511,
        'areaInfo[areaType]': 2,
        'date[year]': year,
        'date[month]': month
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    res = requests.get(url, params=params, headers=headers)
    data = res.json()['data']
    df = pd.read_html(data)[0]
    return df

list = []
for year in range(2011, 2023):
    for month in range(1, 13):
        list.append(craw_weather_forecast(year, month))

pd.concat(list).to_excel('北京10年天气数据.xlsx', index=False) # index是序号