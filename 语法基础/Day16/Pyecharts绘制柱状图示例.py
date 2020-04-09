"""
pyecharts绘制柱状图示例
@Date 2020.04.09
"""
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
# 内置主题类型可查看pyecharts.globals.ThemeType
# 有LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC
# MACARONS PURPLE_PASSION ROMA ROMANTIC SHINE
# VINTAGE WALDEN WESTEROS WONDERLAND等十余种

# 第一幅，数据固定
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
    .add_yaxis('JD', [5, 54, 455, 545, 455, 45])
    .add_yaxis('TB', [51, 4, 55, 55, 45, 45])
    .set_global_opts(title_opts=opts.TitleOpts(title="电商销售对比"))
)
bar.render(path="./res/电商销售对比.html")
# 第二幅，数据分离
items = ['Java', 'C', 'Python', 'C++', 'JavaScript', 'C#', 'PHP']
data_list1 = [188, 151, 145, 150, 52, 145, 12]
data_list2 = [190, 142, 158, 140, 42, 151, 21]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis(items)
    .add_yaxis('2020年', data_list1)
    .add_yaxis('2019年', data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行', subtitle="2019-2020"))
)
bar1.render(path="./res/编程语言排行.html")
# 第三幅
bar2 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(['VIVO', 'OPPO', 'HUAWEI', 'HONOR', 'MI', 'Apple', 'Meizu'])
    .add_yaxis("北京", [85, 75, 90, 50, 120, 60, 70])
    .add_yaxis("上海", [90, 78, 70, 55, 140, 40, 88])
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="手机销售情况"))

)
bar2.render("./res/手机销售情况.html")
