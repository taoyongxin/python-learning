"""
列表切片
Date:2020.4.2
Author:tao
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['potaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
#['apple', 'strawberry', 'waxberry']
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
#['grape', 'apple', 'strawberry', 'waxberry', 'potaya', 'pear', 'mango']
print(fruits3)
fruits4 = fruits[-3:-1]
#['potaya', 'pear']
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
#['mango', 'pear', 'potaya', 'waxberry', 'strawberry', 'apple', 'grape']
print(fruits5)
