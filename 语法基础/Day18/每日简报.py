from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, article, title):
        super().__init__()
        self.article = article
        self.title = title

    def run(self):
        filename = self.title
        article = self.article
        with open('./res/article/'+filename+'.txt', 'w', encoding="utf-8") as f:
            f.write(article)


def main():
    # 使用天性数据接口提供的网络API
    resp = requests.get(
        'http://api.tianapi.com/bulletin/index?key=106dafa779c4b0c66f824ff1e7a45c60')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        article = mm_dict['digest']
        title = mm_dict['title']
        # 通过多线程的方式显示图片下载
        DownloadHanlder(article, title).start()


if __name__ == "__main__":
    main()
