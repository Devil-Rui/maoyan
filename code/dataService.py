import pandas as pd
from typing import List
import operator,numpy


url = r'E:\pycharm\workplace\maoyan\static\datas.csv'

# 将给定list中的dict就行数据处理
def kv_op(key,list):
    if len(list):
        flag = True
        for d in list:
            if key == d.get('name'):
                d['value'] = d.get('value')+1
                flag = False
                break
        if flag:
            list.append({'name': key, 'value': 1})
    else:
        list.append({'name':key,'value':1})

# 电影类型
def category_op():
    df = pd.read_csv(url)
    list = []
    for i in range(df['类型'].__len__()):
        datas = df['类型'][i].split('\n')
        for item in datas:
            item = item.replace(' ','')
            kv_op(item,list)
    return list

#电影制作国家（国际化）
def area_op():
    df = pd.read_csv(url)
    list = []
    for i in range(df['制方国家'].__len__()):
        datas = df['制方国家'][i].split(',')
        for item in datas:
            kv_op(item,list)
    return list

#电影年份
def year_op():
    df = pd.read_csv(url)
    list = []
    for i in range(df['上映时间'].__len__()):
        data = df['上映时间'][i][:4]
        kv_op(int(data),list)
    list = sorted(list, key=operator.itemgetter('name'))
    for i in range(len(list)):
        list[i] = [list[i].get('name'),list[i].get('value')]
    return list

#电影时长
def length_op():
    df = pd.read_csv(url)
    list = []
    for i in range(df['片长'].__len__()):
        data = df['片长'][i][:-2]
        kv_op(int(data),list)
    list = sorted(list, key=operator.itemgetter('name'))
    for i in range(len(list)):
        list[i] = [list[i].get('name'),list[i].get('value')]
    return list

#电影评分
def score_op():
    df = pd.read_csv(url)
    list = []
    for i in range(df['评分'].__len__()):
        data = df['评分'][i]
        kv_op(float(data),list)
    list = sorted(list, key=operator.itemgetter('name'))
    for i in range(len(list)):
        list[i] = [list[i].get('name'),list[i].get('value')]
    return list

# 全部类型
def get_categories():
    df = pd.read_csv(url)
    d = {}
    for i in range(df['类型'].__len__()):
        datas = df['类型'][i].split('\n')
        for item in datas:
            item = item.replace(' ', '')
            d.setdefault(item)
    return list(d)

#全部国家
def get_districts():
    df = pd.read_csv(url)
    d = {}
    for i in range(df['制方国家'].__len__()):
        datas = df['制方国家'][i].split(',')
        for item in datas:
            item = item.replace(' ', '')
            d.setdefault(item)
    return list(d)

# 获取指定类型的评分-年份数据 [1980, 9.2]
def scoreWithYearByCatetory(catetory):
    df = pd.read_csv(url)
    list = []
    if catetory=='全部':
        for i in range(df['上映时间'].__len__()):
            year = df['上映时间'][i][:4]
            score = df['评分'][i]
            list.append([float(year),float(score)])
        return list
    else:
        bool = df['类型'].str.contains(catetory)
        df = df[bool]
        df.reset_index(drop=True, inplace=True)
        for i in range(df['上映时间'].__len__()):
            year = df['上映时间'][i][:4]
            score = df['评分'][i]
            list.append([float(year),float(score)])
        return list

# 获取指定类型的评分-片长数据 [1980, 130]
def scoreWithLengthByCatetory(catetory):
    df = pd.read_csv(url)
    list = []
    if catetory == '全部':
        for i in range(df['片长'].__len__()):
            length = df['片长'][i][:-2]
            score = df['评分'][i]
            list.append([int(length), float(score)])
        return list
    else:
        bool = df['类型'].str.contains(catetory)
        df = df[bool]
        df.reset_index(drop=True, inplace=True)
        for i in range(df['片长'].__len__()):
            year = df['片长'][i][:-2]
            score = df['评分'][i]
            list.append([int(year), float(score)])
        return list

# 获取指定国家的评分-年份数据 [1980, 9.2]
def scoreWithYearByCountry(country):
    df = pd.read_csv(url)
    list = []
    bool = df['制方国家'].str.contains(country)
    df = df[bool]
    df.reset_index(drop=True, inplace=True)
    for i in range(df['上映时间'].__len__()):
        year = df['上映时间'][i][:4]
        score = df['评分'][i]
        list.append([float(year),float(score)])
    return list

# 获取指定国家的评分-片长数据 [1980, 130]
def scoreWithLengthByCountry(country):
    df = pd.read_csv(url)
    list = []
    bool = df['制方国家'].str.contains(country)
    df = df[bool]
    df.reset_index(drop=True, inplace=True)
    for i in range(df['片长'].__len__()):
        year = df['片长'][i][:-2]
        score = df['评分'][i]
        list.append([int(year), float(score)])
    return list

# 根据国家获取类型
def get_average(country):
    df = pd.read_csv(url)
    bool = df['制方国家'].str.contains(country)
    df = df[bool]
    df.reset_index(drop=True, inplace=True)
    d = {}
    for i in range(df['类型'].__len__()):
        datas = df['类型'][i].split('\n')
        for item in datas:
            item = item.replace(' ', '')
            if item in d:
                d[item] = numpy.round(numpy.mean([float(df['评分'][i]),float(d[item])]),decimals=2)
            else:
                d[item] = df['评分'][i]
    l = list(d)
    ll = []
    for item in l:
        ll.append(d[item])
    return [l,ll]

#获取指定范围的数据[{},{}]
def getFilm(page,span):
    df = pd.read_csv(url)
    l = []
    for i in range((page-1)*span,(page-1)*span+span):
        data = {}
        item = df.loc[i]
        data['排名'] = int(item['排名'])
        data['电影名称'] = item['电影名称']
        data['导演'] = item['导演']
        data['主演'] = item['主演'].replace(',',' ')
        data['类型'] = item['类型'].replace('\n','')
        data['制方国家'] = item['制方国家']
        data['上映时间'] = item['上映时间'][:4]
        data['片长'] = item['片长']
        data['评分'] = item['评分']
        data['链接'] = item['链接']
        data['图片'] = item['图片']
        data['票房'] = item['票房']
        data['介绍'] = item['介绍']
        l.append(data)
    l = sorted(l, key=operator.itemgetter('排名'))
    return l

#获取指定包含指定名称的数据[{},{}]
def getFilmByKey(key):
    df = pd.read_csv(url)
    bool = df['电影名称'].str.contains(key)
    df = df[bool]
    df.reset_index(drop=True, inplace=True)
    l = []
    for i in range(df['电影名称'].__len__()):
        data = {}
        item = df.loc[i]
        data['排名'] = int(item['排名'])
        data['电影名称'] = item['电影名称']
        data['导演'] = item['导演']
        data['主演'] = item['主演'].replace(',',' ')
        data['类型'] = item['类型'].replace('\n','')
        data['制方国家'] = item['制方国家']
        data['上映时间'] = item['上映时间'][:4]
        data['片长'] = item['片长']
        data['评分'] = item['评分']
        data['链接'] = item['链接']
        data['图片'] = item['图片']
        data['票房'] = item['票房']
        data['介绍'] = item['介绍']
        l.append(data)
    l = sorted(l, key=operator.itemgetter('排名'))
    return l

def get_money():
    df = pd.read_csv(url)
    data = [{"name":"0~100","value":0},{"name":"100~500","value":0},{"name":"500~1000","value":0},{"name":"1000~3000","value":0},
            {"name":"3000~5000","value":0},{"name":"5000~8000","value":0},{"name":"8000~10000","value":0},{"name":"10000~30000","value":0},
            {"name":"30000~50000","value":0},{"name":"50000~80000","value":0},{"name":"80000~100000","value":0},{"name":"100000~150000","value":0}]
    l = []
    no = 0
    for i in range(df['票房'].__len__()):
        if df['票房'][i] == '暂无':
            no += 1
        else:
            l.append(int(df['票房'][i]))
    l.sort()
    tmp = 0
    for item in l:
        for i in range(tmp,len(data)):
            if item < int(data[i]['name'].split('~')[1]):
                data[i]['value'] = data[i]['value'] + 1
                break
            else:
                tmp += 1
    data[0]['name'] = '0~1'
    for i in range(1,len(data)):
        data[i]['name'] = data[i]['name'].split('~')[0][0:-2] + '~' + data[i]['name'].split('~')[1][0:-2]
    data.append({"name":"暂无","value":no})
    return data







if __name__ == '__main__':
    pass