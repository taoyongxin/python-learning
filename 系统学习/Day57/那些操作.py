"""
那些操作
@Date 2020.05.20
"""

from functools import reduce
import random

# 一行代码生成[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 使用列表生成式，创建列表，观察元素出现规律，可得到如下代码
a = [2*i+1 for i in range(10)]
print(a)

# 写一个等差数列，产生一个首项为10，公差为12，未项不大于100的列表
# 使用列表生成式创建

a = list(range(10, 100, 12))
print(a)  # [10, 22, 34, 46, 58, 70, 82, 94]

# 一行代码求 1 到 1000 内整数和
# 方法1：使用python内置函数sum求和
s = sum(range(1000))
print(s)  # 499500
# 方法2：使用functools 模块中的reduce求和
s = reduce(lambda x, y: x+y, range(1000))
print(s)  # 499500

# 打乱一个列表
# 使用random模块，shuffle函数打乱原来列表
a = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(a)
print(a)  # [6, 2, 8, 5, 3, 4, 7, 1]
