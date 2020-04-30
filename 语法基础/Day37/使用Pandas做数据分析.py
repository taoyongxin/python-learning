"""
使用Pandas做数据分析（1）
@Date 2020.04.30
四月，再见，Hi May~~
"""
import pandas as pd

# 导入数据集
path1 = "./res/csv/juejin.csv"
# 数据集存入一个名未chipo的数据框
chipo = pd.read_csv(path1, sep="\t")
# 查看前10行
print(chipo.head(10))
# 数据集中有多少列
print(chipo.shape[1])
# 打印出全部的列名
print(chipo.columns)
# 数据集的索引
print(chipo.index)
# print(chipo['follower_count'].nunique)
