"""
元组是不可变的，所以没用插入和删除方法
@Date 2020.05.03
"""


from numpy import random
a = ()   # 空元组对象
b = (1, 'xiaoming', 29.5, '17312662388')
c = ('001', '2020-05-03', ['三文鱼', '电烤箱'])
# 从[1,5)区间内随机选择 10 个数
a = random.randint(1, 5, 10)
print(a)
# [1 1 2 1 2 4 4 3 4 1]
at = tuple(a)
# 统计 3 出现次数
at.count(3)
print(at.count(3))  # 1
