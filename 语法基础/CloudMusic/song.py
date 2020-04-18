import uuid
import requests
import csv
import json
import pymysql
import time
import datetime
import random
import hashlib
from faker import Faker
fake = Faker(locale='zh_CN')


# 爬取歌单数据
def crawl_music_list(music_list_type):
    play_lists = []
    url = "http://localhost:3000/top/playlist/highquality?cat=" + \
        str(music_list_type)
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
        "origin': 'https://music.163.com"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    play_lists = response.json().get("playlists")
    return play_lists


# 获取歌曲url
def crawl_song_url(song_id):
    data = []
    url = "http://localhost:3000/song/url?id=" + \
        str(song_id)
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
        "origin': 'https://music.163.com"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    try:
        data = response.json().get("data")[0]['url']
    except:
        data = " "
    return data


# 获取歌词
def crawl_song_lyric(song_id):
    lyric = []
    url = "http://localhost:3000/lyric?id=" + \
        str(song_id)
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
        "origin': 'https://music.163.com"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    try:
        lyric = response.json()['lrc']['lyric']
    except:
        lyric = " "
    return lyric


# 爬取歌单中的音乐详情
def crawl_song(music_list_id):
    play_lists = []
    url = "http://localhost:3000/playlist/detail?id="+str(music_list_id)
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
        "origin': 'https://music.163.com"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    songs = response.json().get("playlist").get("tracks")
    return songs


# 新增歌单
def data_insert_music_list(play_lists):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    for dic in play_lists:
        # 获取歌单下的音乐id
        songs = crawl_song(dic['id'])
        data_insert_song(songs)
        item = (dic['id'], dic['name'],
                dic['coverImgUrl'], dic['tag'],
                dic['trackCount'], dic['shareCount'],
                dic['commentCount'], '0', theTime, theTime, "ext")
        val.append(item)
    sql = "INSERT INTO song_list (song_list_id,song_list_name,thumbnail,type,song_count,like_count,comment_count,delete_flag,update_time,create_time,ext1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


# 新增歌单
def data_insert_song(songs):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

    for dic in songs:
        # 获取歌手姓名
        singer = dic['ar'][0]['name']
        # 获取歌曲封面图
        picUrl = dic['al']['picUrl']
        # 获取歌曲时长
        time = songTimeStamp(dic['dt'])
        # 获取歌曲url
        data = crawl_song_url(dic['id'])
        # url = data[0]['url']
        # 获取歌词
        lyric = crawl_song_lyric(dic['id'])
        item = (dic['id'], dic['name'],
                dic['id'], singer,
                time, picUrl,
                data, lyric, 1000, fake.pyint(),
                fake.pyint(), '0', theTime, theTime)
        val.append(item)
    sql = "INSERT INTO song (song_id,song_name,sort_id,singer,duration,thumbnail,url,lyric,comment_count,like_count,play_count,delete_flag,update_time,create_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


# 歌曲时长转换
def songTimeStamp(time):
    seconds = int(time/1000 % 60)
    minutes = int(time/1000/60)
    if(seconds < 10):
        seconds = '0' + ":" + str(seconds)
    if(minutes <= 9):
        minutes = '0' + str(minutes)
    return str(minutes) + ":" + str(seconds)


if __name__ == "__main__":
    musics_list_type = ['摇滚', '古典', '流行', '华语', '民谣', '电子', '另类/独立', '轻音乐', '影视原声',
                        'ACG', '欧美', '日语', '韩语', '粤语', '说唱', '爵士', '蓝调', '小语种', '古风', '后摇', '运动', '浪漫']
    # musics_list_type = ['流行']
    for music_list_type in musics_list_type:
        music_list = crawl_music_list(music_list_type)
        data_insert_music_list(music_list)
    # 爬取歌单的数据
    # music_list = crawl_music_list()
    # # 新增歌单的数据
    # data_insert_music_list(music_list)
