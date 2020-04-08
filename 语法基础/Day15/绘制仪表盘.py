"""
使用pycharts绘制仪表盘
@Date 2020.04.09
"""
from pyecharts import charts

# 仪表盘
guage = charts.Gauge()
guage.add('Python小例子', [('Python机器学习', 30),
                        ('Python基础', 70), ('Python正则', 90)])
guage.render(path="./res/仪表盘.html")
print('ok')
