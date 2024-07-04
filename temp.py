import json

import requests

from 爬虫 import UA_pool

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

arr = ['2023', '2022', '2021']
province_name = {}
for item in province_id:
    province_name[item['name']] = item['value']
    province_name[item['value']] = item['name']
province_header = {}
mp = {1: '理科', 2: '文科', 3: '综合类', 2073: '物理类', 2074: '历史类'}
province_type = {}

def get_header():
    url = 'https://static-data.gaokao.cn/www/2.0/school/140/dic/specialplan.json'
    html = get_url(url)
    unicoder = json.loads(html)
    data = unicoder['data']
    newsdata = data['newsdata']
    type = newsdata['type']
    last = -1
    header = ['名称', '省', '市', '985', '211', '学校类型', '学校属性']
    for item in type.items():
        key, value = item
        #print(f'{key} {value}')
        pro_id = key[:2]
        if last == -1:
            last = pro_id
        if pro_id != last:
            province_header[last] = header
            #print(f'{last} ', *header)
            header = header[:7]
            last = pro_id
        year = key[3:]
        #print(f'{pro_id} {year}')
        if year in arr:
            for element in value:
                s = f'{year}年{mp[element]}录取分数'
                header.append(s)
            if '文科' not in header[-1] and '理科' in header[-1]:
                s = f'{year}年文科录取分数'
                header.append(s)
            elif '历史类' not in header[-1] and '物理类' in header[-1]:
                s = f'{year}年历史类录取分数'
                header.append(s)

    province_header[last] = header
    #print(f'{last} ', *header)
