import requests
import json
import csv
from 爬虫 import UA_pool


def save_data(s, data):
    with open(f'D:\\py课设\\高校分数线{s}.csv', encoding='UTF-8', mode='a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(data)


headers = {
    'User-Agent': UA_pool.get_ua()
}


def get_url(url):
    try:
        response = requests.get(url, headers=headers, timeout=1)  # 超时设置为10秒
    except:
        for i in range(4):  # 循环去请求网站
            response = requests.get(url, headers=headers, timeout=20)
            if response.status_code == 200:
                break
    html_str = response.text
    return html_str


def func(m):
    x=''
    y=''
    for j in m['type'].keys():
        if j == '1':
            x = m['type'][j]
        if j == '2':
            y = m['type'][j]
    return x,y


def check(x):
    if x == '1':
        return '是'
    else:
        return '否'


url = 'https://static-data.gaokao.cn/www/2.0/school/name.json'
html = requests.get(url).text
unicodestr = json.loads(html)  # 将string转化为dict
dat = unicodestr["data"]

province_id = [{"name": 11, "value": "北京"}, {"name": 12, "value": "天津"}, {"name": 13, "value": "河北"},
               {"name": 14, "value": "山西"}, {"name": 15, "value": "内蒙古"}, {"name": 21, "value": "辽宁"},
               {"name": 22, "value": "吉林"}, {"name": 23, "value": "黑龙江"}, {"name": 31, "value": "上海"},
               {"name": 32, "value": "江苏"}, {"name": 33, "value": "浙江"}, {"name": 34, "value": "安徽"},
               {"name": 35, "value": "福建"}, {"name": 36, "value": "江西"}, {"name": 37, "value": "山东"},
               {"name": 41, "value": "河南"}, {"name": 42, "value": "湖北"}, {"name": 43, "value": "湖南"},
               {"name": 44, "value": "广东"}, {"name": 45, "value": "广西"}, {"name": 46, "value": "海南"},
               {"name": 50, "value": "重庆"}, {"name": 51, "value": "四川"}, {"name": 52, "value": "贵州"},
               {"name": 53, "value": "云南"}, {"name": 54, "value": "西藏"}, {"name": 61, "value": "陕西"},
               {"name": 62, "value": "甘肃"}, {"name": 63, "value": "青海"}, {"name": 64, "value": "宁夏"},
               {"name": 65, "value": "新疆"}]
header = ['名称', '省', '市', '985', '211', '软科排名', '学校类型', '学校属性',
              "2023理科分数线","2023文科分数线","2022理科分数线","2022文科分数线","2021理科分数线","2021文科分数线"]
for l in province_id:
    with open('D:\\py课设\\高校分数线' + l["value"] + '.csv', encoding='utf-8-sig', mode='w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
for i in dat:
    schoolid = i['school_id']
    schoolname = i['name']
    #如果是专科学校
    if i['type'] == '6001':
        continue
    url1 = f'https://static-data.gaokao.cn/www/2.0/school/{schoolid}/info.json'

    html1 = get_url(url1)
    unicodestr1 = json.loads(html1)  # 将string转化为dict
    if len(unicodestr1) != 0:
        dat1 = unicodestr1["data"]
        if dat1['school_type_name'] != '本科':
            continue
        name = dat1["name"]
        f985 = check(dat1["f985"])

        f211 = check(dat1['f211'])

        ruanke_rank = dat1["ruanke_rank"]
        if ruanke_rank == '0':
            continue
        type_name = dat1["type_name"]
        school_nature_name = dat1["school_nature_name"]  #学校是公办还是民办
        province_name = dat1["province_name"]  #在那个省学校
        city_name = dat1["city_name"]  #学校在那个市

        pro_type_min = dat1["pro_type_min"]

        print(f"正在下载{schoolname},学校id = {dat1['school_id']}")
        for l in province_id[13:14]:
            if f'{l['name']}' in pro_type_min:
                Lfen2023 = ''
                Wfen2023 = ''
                Lfen2022 = ''
                Wfen2022 = ''
                Lfen2021 = ''
                Wfen2021 = ''
                for m in pro_type_min[f'{l['name']}']:
                    if m['year'] == 2023:
                        Lfen2023,Wfen2023 = func(m)
                    elif m['year'] == 2022:
                        Lfen2022,Wfen2022 = func(m)
                    else:
                        Lfen2021,Wfen2021 = func(m)
                if Lfen2023 == '' or Lfen2022 == '' or Lfen2021 == '' or Wfen2023 == '' or Wfen2022 == '' or Wfen2021 == '':
                    continue
                tap = (name, province_name, city_name, f985, f211, ruanke_rank, type_name,
                       school_nature_name, Lfen2023, Wfen2023,Lfen2022, Wfen2022, Lfen2021, Wfen2021)
                save_data(l["value"], tap)
