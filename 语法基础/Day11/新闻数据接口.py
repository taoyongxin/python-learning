"""
requests请求api 用字典和列表保存为json
@Date 2020.4.4
"""
import json
import requests
resp = requests.get(
    'http://api.tianapi.com/allnews/index?key=106dafa779c4b0c66f824ff1e7a45c60&num=10&col=7'
)
newslist = json.loads(resp.text)['newslist']
result = []
data = './res/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)
