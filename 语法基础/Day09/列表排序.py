"""
列表排序
Date:2020.4.2
Author：tao
"""
list1 = ["orange", "apple", "zoo", "internationalization", "blueberry"]
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
list3 = sorted(list1, reverse=True)
# 通过Key关键字参数指定根据字符串长度进行排序而不是默认的字母表排序
list4 = sorted(list1, key=len)
print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list2)  # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
print(list3)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list4)  # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
