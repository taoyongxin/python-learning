"""
外部文本词云
@Date 2020.04.17
"""
import wordcloud
import random

# 读入外部文本文件
f = open('./res/txt/外部文本.txt', encoding='utf-8')
txt = f.read()
w = wordcloud.WordCloud(
    scale=2,  # 缩放2倍
    max_font_size=100,
    background_color='#383838',
    colormap='Set3',
    font_path='./res/font/SimHei.ttf')
# https://matplotlib.org/examples/color/colormaps_reference.html
# 将txt变量传入
w.generate(txt)
w.to_file('./res/img/output3.png')
