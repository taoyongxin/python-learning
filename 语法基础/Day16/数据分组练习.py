"""
python数据分组练习
@Date 2020.04.09
"""
from itertools import groupby
weather = [{'date': '2020-01-01', 'weather': 'cloud'},
           {'date': '2020-01-02', 'weather': 'sunny'},
           {'date': '2020-01-03', 'weather': 'cloud'}]
# 分组前没有按照分组字段排序，分组失败
for k, items in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in items:
        print(i)

print('******************************************************')

# 分组前按照分组字段排序，分组成功
weather.sort(key=lambda x: x['weather'])
for k, items in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in items:
        print(i)
