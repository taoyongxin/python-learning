"""
数据样本和清晰
@Date 2020.05.04
"""
from random import randint, sample, shuffle, uniform

# 使用random的sample抽样10个样本
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])
lst_sample = sample(lst, 10)
print(lst_sample)

# 使用内置random中的buffle函数冲洗数据
lst = [randint(0, 50) for _ in range(100)]
shuffle(lst)
print(lst[:5])

# 生成满足均匀分布的坐标点
x, y = [i for i in range(100)], [round(uniform(0, 10), 2) for _ in range(100)]
print(y)
