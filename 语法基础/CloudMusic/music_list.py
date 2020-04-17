"""
爬取网易云歌单数据
@Date 2020.04.17
"""
import requests
import csv
import json
import pymysql
import time
import datetime


def crawl():
    play_lists = []
    url = "http://localhost:3000/top/playlist/highquality?cat=%E5%8F%A6%E7%B1%BB/%E7%8B%AC%E7%AB%8B"
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    play_lists = response.json().get("playlists")
    return play_lists


def data_insert(play_lists):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    for dic in play_lists:
        item = (dic['id'], dic['name'],
                dic['coverImgUrl'], dic['tag'],
                dic['trackCount'], dic['shareCount'],
                dic['commentCount'], '0', theTime, theTime, "ext")
        val.append(item)
        # print(item)
    # print(val)
    sql = "INSERT INTO song_list (song_list_id,song_list_name,thumbnail,type,song_count,like_count,comment_count,delete_flag,update_time,create_time,ext1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  #  sql = "INSERT INTO song_list (song_list_id,song_list_name,thumbnail,type,song_count,like_count,comment_count,delete_flag,update_time,create_time,ext1) VALUES ('111456043','掰的人是这样拉小提琴的','http://p1.music.126.net/bxKjPzDgEGO-Syp0q3iO-A==/3335918279600446.jpg')"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
        # cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


if __name__ == "__main__":
    list = crawl()
    # print(list)
    data_insert(list)
