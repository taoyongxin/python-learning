"""
基础词云
@Date 2020.04.17
"""
import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate('Not everything can beat you,Things are going to change you,\
    But you get to choose ,which ones you let change you \
    Life is a gift,Appreciate all the rewards,And jump on every opportunity,\
        Not everyone going to love you, But who needs them anyway')
# 生成本地图片
w.to_file('./res/img/output1.png')

# 创建词云对象，设置词云图片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        colormap='tab20b',
                        font_path='./res/font/SimHei.ttf')
w.generate('确诊,众志成城,教育部,钟南山,封城,疫情,学生,中小学,管理,高校,毕业,复课,李兰娟,校园,\
    疫情防控,隔离,错峰,新冠肺炎,武汉加油,高考,物资,延期,消毒,方案,口罩,防疫,不畏困难,病例,线上教学,\
        确保,有效,核检,推迟,一级响应,科学,保障')
w.to_file('./res/img/outpu2.png')
