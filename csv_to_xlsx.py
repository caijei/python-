import pandas as pd
from openpyxl import writer

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
#writer = pd.ExcelWriter('D:\\py课设\\excel格式\\高校分数线.xlsx', engine='openpyxl')

for province in province_id:
    # 读取CSV文件
    data_csv = pd.read_csv(f'D:\\py课设\\csv格式\\高校分数线{province["value"]}.csv', encoding='utf-8')
    data_csv.to_excel(f'D:\\py课设\\excel格式\\高校分数线{province["value"]}.xlsx', index=False,sheet_name=province["value"])
    # 将数据写入Excel文件的一个新工作表中
    #data_csv.to_excel(writer, index=False, sheet_name=province['value'])

# 关闭并保存Excel文件
writer.close()