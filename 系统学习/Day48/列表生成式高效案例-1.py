"""
列表生成式高效案例-1
"""

# 1、对每个元素的乘方操作后，利用列表生成返回一个新的列表
from random import random
a = range(0, 11)
b = [x**2 for x in a]
print(b)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2、数值型的元素，转换为字符串类型的列表
a = range(0, 10)
b = [str(i) for i in a]
print(b)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 3、生成10 个 0 到 1 的随机浮点数，保留小数点后两位
a = [round(random(), 2) for _ in range(10)]
print(a)  # [0.39, 0.49, 0.14, 0.07, 0.45, 0.53, 0.44, 0.76, 0.42, 0.88]

# 4、对一个列表里面的数据筛选，只计算[0,11) 中偶数的平方
a = range(11)
b = [x**2 for x in a if x % 2 == 0]
print(b)  # [0, 4, 16, 36, 64, 100]

# 5、zip 和列表
a = range(5)
b = ['a', 'b', 'c', 'd', 'e']
c = [str(y) + str(x) for x, y in zip(a, b)]
print(c)  # ['a0', 'b1', 'c2', 'd3', 'e4']

# 6、打印键值对
a = {'a': 1, 'b': 2, 'c': 3}
b = [k + '=' + str(v) for k, v in a.items()]
print(b)  # ['a=1', 'b=2', 'c=3']
