"""
列表元素添加和删除
Date:2020.4.1
Author:tao
"""

list1 = [1, 3, 5, 7, 100]
list1.append(200)  # append从数组最后面添加
list1.insert(1, 400)  # insert添加到数组的最前面
print(list1)  # [1, 400, 3, 5, 7, 100, 200]
# 合并两个列表
list1.extend([1000, 2000])
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
list1 += [100, 200]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000, 100, 200]
print(len(list1))  # 11
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 100 in list1:
    list1.remove(100)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [1, 400, 3, 5, 7, 200, 1000, 2000, 100, 200]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)  # [400, 3, 5, 7, 200, 1000, 2000, 100]
# 清空列表元素
list1.clear()
print(list1)  # []
