"""
爬取掘金专题数据
@Date 2020.04.11
"""
import requests
import csv
import json
import pymysql
import time


def crawl():
    url = "https://short-msg-ms.juejin.im/v1/topicList?uid=5dc985d9f265da4d2b350fa9&device_id=1585185008570&token=eyJhY2Nlc3NfdG9rZW4iOiJpNlBwdHI1SE91dldtZmcyIiwicmVmcmVzaF90b2tlbiI6IjNTRjk2NEJLbE5VZ3o1azgiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D&src=web&sortType=hot&page=0&pageSize=100"
    # 查询参数
    params = {
        "uid": "5dc985d9f265da4d2b350fa9",
        "device_id": "1585185008570",
        "token": "eyJhY2Nlc3NfdG9rZW4iOiJpNlBwdHI1SE91dldtZmcyIiwicmVmcmVzaF90b2tlbiI6IjNTRjk2NEJLbE5VZ3o1azgiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D",
        "src": "web",
        "sortType": "hot",
        "page": 0,
        "pageSize": 100
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers, params=params)
    # print("请求的url：", response.url)
    # print("返回数据：", response.text)

    # csvfile = open('./res/juejin.csv', 'w', newline='')
    # writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    # keys = ['objectId', 'title', 'description',
    #         'icon', 'msgsCount', 'followersCount']
    # writer.writerow(keys)
    # i = 1
    # for dd in response.json().get("d").get("list"):
    #     writer.writerow([dd['objectId'], dd['title'], dd['description'],
    #                      dd['icon'], dd['msgsCount'], dd['followersCount']])
    #     i += 1
    # csvfile.close()

    list_data = []
    list_data = response.json().get("d").get("list")
    return list_data


def data_insert(list_data):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    for dic in list_data:
        item = (dic['objectId'], dic['title'], dic['description'],
                dic['icon'], dic['msgsCount'], dic['followersCount'],
                dic['attendersCount'], dic['hotIndex'], dic['createdAt'],
                dic['updatedAt'], dic['latestMsgCreatedAt'], dic['followed'],)
        val.append(item)
    sql = "INSERT INTO t_juejin (objectId,title,description,icon,msgsCount,followersCount,attendersCount,hotIndex,createdAt,updatedAt,latestMsgCreatedAt,followed) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    list = crawl()
    print(list)
    data_insert(list)
    # crawl()
