"""
爬取网易云用户数据
@Date 2020.04.17
"""
import requests
import csv
import json
import pymysql
import time
import datetime
import random
import hashlib
import uuid
from faker import Faker
fake = Faker(locale='zh_CN')


def crawl():
    subscribers = []
    url = "http://localhost:3000/playlist/subscribers?id=109322062&limit=1000"
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
        # 测试生成uuid
        # key_id = uuid.uuid4()
        # print(key_id)
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


# 随机生成邮箱
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
    list = crawl()
    # print(list)
    data_insert_user(list)
