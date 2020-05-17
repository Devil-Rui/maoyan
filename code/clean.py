import pandas as pd
from datetime import datetime
import numpy

from_url = r'../static/datas.csv'
to_url = r'../static/datas.csv'

# 主演 上映时间 票房
def first(f,t):
    df = pd.read_csv(f)
    df['主演'] = df['主演'].str[3:]
    df['上映时间'] = df['上映时间'].str[5:]
    df.insert(loc=0, column='排名', value=[x for x in range(1, 101)])
    df['票房'].fillna('暂无', inplace=True)
    df.to_csv(t, index=False, encoding='utf_8_sig')

#1994-05-17(法国)  1999/1/2
def str2date(str_date):
    str_date = str_date.strip()  #将空格去掉
    a_date=''
    if (len(str_date) > 10):
        str_date = str_date[:10]  #取前10位日期

    if (str_date.find('-') > 0):  # 如果是中间-这种方式
        if (len(str_date) < 10):
            year = str_date[:4]
            month = str_date[str_date.rfind('-')+1:]
            a_date = '%s-%s' % (year, month)
        else:
            year = str_date[:4]
            month = str_date[5:str_date.rfind('-')]
            day = str_date[str_date.rfind('-') + 1:]
            a_date = '%s-%s-%s' % (year, month, day)

    if (str_date.find('/') > 0):
        if (len(str_date) < 8):
            year = str_date[:4]
            month = str_date[str_date.rfind('/') + 1:]
            if month < 10:
                month = '0' + str(month)
            a_date = '%s-%s' % (year, month)
        else:
            year = str_date[:4]
            month = str_date[5:str_date.rfind('/')]
            day = str_date[str_date.rfind('/') + 1:]
            if month < 10:
                month = '0' + str(month)
            if day < 10:
                day = '0' + str(day)
            a_date = '%s-%s-%s' % (year, month, day)
    elif(str_date.find('-')==-1 and str_date.find('-')==-1  ):
        a_date=str_date[:4]
    return a_date

#上映时间
def second(f,t):
    df = pd.read_csv(f)
    for i in range(df['上映时间'].__len__()):
        data = str2date(df['上映时间'][i])
        df['上映时间'][i] = data
    df['上映时间'] = pd.to_datetime(df['上映时间'], format='%Y-%m-%d')
    df.to_csv(t, index=False, encoding='utf_8_sig')

#制作国家
def third(f,t):
    df = pd.read_csv(f)
    for i in range(df['制方国家'].__len__()):
        df['制方国家'][i] = df['制方国家'][i].replace('大陆','')
        df['制方国家'][i] = df['制方国家'][i].replace('香港','')
        df['制方国家'][i] = df['制方国家'][i].replace('台湾','')
        df['制方国家'][i] = df['制方国家'][i].replace('西德','德国')
        df['制方国家'][i] = ','.join(set(df['制方国家'][i].split(',')))
    df.to_csv(t, index=False, encoding='utf_8_sig')

# 票房处理 单位：万
def fourth(f,t):
    df = pd.read_csv(f)
    for i in range(df['票房'].__len__()):
        if df['票房'][i][-3:] == '万美元':
            df['票房'][i] = int(df['票房'][i][:-3]*7.1)
        elif df['票房'][i][-1] == '亿':
            df['票房'][i] = int(df['票房'][i][:-1] * 10000)
        elif df['票房'][i][-1] == '万':
            df['票房'][i] = df['票房'][i][:-1]
    df.to_csv(t, index=False, encoding='utf_8_sig')

if __name__ == '__main__':
    # first(from_url,to_url)
    # second(from_url,to_url)
    # third(from_url,to_url)
    # fourth(from_url,to_url)
    df = pd.read_csv(from_url)
    l= []
    for i in range(df['票房'].__len__()):
        if df['票房'][i] != '暂无':
            l.append(int(df['票房'][i]))
    print(max(l))
