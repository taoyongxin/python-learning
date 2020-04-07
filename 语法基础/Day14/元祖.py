"""
Python中的元祖与列表类型也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
不同之处在于元祖的元素不能修改，在前面的代码中我们已经不止一次使用过元祖了，顾名思义
我们把多个元素组合到一起就形成了一个元祖，所以它和列表一样可以保存多条数据。
@Date 2020.4.6
"""

# 定义元祖
t = ('Tao', 18, True, '江苏扬州')
print(t)  # ('Tao', 18, True, '江苏扬州')
# 获取元祖中的元素
print(t[0])  # Tao
print(t[3])  # 江苏扬州
# 遍历元祖中的值
for member in t:
    print(member)
    # Tao
    # 18
    # True
    # 江苏扬州
# 重新给元祖赋值
# t[0] = 'Wang'  # 发生异常: TypeError
# 变量t重新引用了新的元祖原来的元祖被垃圾回收
t = ('Wang', 22, True, '江苏南京')
print(t)  # ('Wang', 22, True, '江苏南京')
# 将元祖转换成列表
person = list(t)
print(person)  # ['Wang', 22, True, '江苏南京']
# 列表是可以修改它的元素的
person[0] = 'Li'
person[1] = 25
print(person)  # ['Li', 25, True, '江苏南京']
# 将列表转换成元祖
print(tuple(person))  # ('Li', 25, True, '江苏南京')
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)  # ('apple', 'banana', 'orange')
