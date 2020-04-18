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
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    play_lists = response.json().get("playlists")
    return play_lists


# 爬取用户数据
def crawl_users(music_list_id):
    subscribers = []
    url = "http://localhost:3000/playlist/subscribers?id=" + \
        str(music_list_id)+"&limit=1000"
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # print("请求URL：", response.url)
    # print("返回数据：", response.text)
    subscribers = response.json().get("subscribers")
    return subscribers


# 新增用户
def data_insert_user(subscribers):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    # 获取系统当前时间并且格式化
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    # 遍历数组数据
    for dic in subscribers:
        # 随机生成账号和密码
        userName = ''.join(random.sample(
            "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_/", 10))
        userPassword = ''.join(random.sample(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890", 6))
        # 随机生成手机号码
        phone = fake.phone_number()
        # 随机生成邮箱
        email = RandomEmail()
        # email = fake.email() #使用fake随机生成邮箱
        # 随机性别
        sex = ["男", "女"]
        gender = random.choice(sex)
        # 随机生成地址
        address = fake.address()
        # 随机生成生日
        birthday = fake.date()
        # 生成时间
        ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        # 根据密码进行MD5加密 生成盐
        h1 = hashlib.md5()
        h1.update(userPassword.encode('UTF-8'))
        salt = h1.hexdigest()
        item = (dic['userId'], userName,
                dic['nickname'], userPassword,
                phone, email,
                dic['avatarUrl'], gender, address,
                birthday, 0, 0, theTime, theTime, salt, 'ex')
        val.append(item)
    sql = "INSERT INTO user (user_id,user_name,nick_name,password,phone,email,avatar,gender,address,birthday,cloud_coin,delete_flag,update_time,create_time,salt,ext1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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


# 新增歌单
def data_insert_music_list(play_lists):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    for dic in play_lists:
        # 访问用户的接口，取出此歌单下用户的数据
        users = crawl_users(dic['id'])
        # 将用户数据存入到用户表
        data_insert_user(users)
        # 新增用户歌单关联表
        data_insert_user_music_list(users, dic['id'])
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


def data_insert_user_music_list(users, music_list_id):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "db_python")
    # 使用cursor() 方法创建一个游标对象cursor
    cursor = db.cursor()
    val = []
    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    for dic in users:
        # 通过uuid库随机生成主键id
        key_id = uuid.uuid4()
        item = (str(key_id), str(music_list_id), str(dic['userId']),
                theTime, theTime)
        # print(item)
        val.append(item)
    sql = "INSERT INTO user_song_list (id,song_list_id,user_id,create_time,update_time) VALUES (%s,%s,%s,%s,%s)"
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


def RandomEmail(emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email


if __name__ == "__main__":
    # musics_list_type = ['摇滚', '古典', '流行','华语','民谣','电子','另类/独立','轻音乐','影视原声','ACG','欧美','日语','韩语','粤语','说唱','爵士','蓝调','小语种','古风','后摇','运动','浪漫']
    musics_list_type = ['轻音乐']
    for music_list_type in musics_list_type:
        music_list = crawl_music_list(music_list_type)
        data_insert_music_list(music_list)
    # 爬取歌单的数据
    # music_list = crawl_music_list()
    # # 新增歌单的数据
    # data_insert_music_list(music_list)
