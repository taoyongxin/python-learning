"""
pyecharts绘制柱状图示例
@Date 2020.04.11
"""
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker

bar2 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(['信息数量', '关注人数', '参与人数'])
    .add_yaxis("上班摸鱼", [8490, 3546, 14276])
    .add_yaxis("一图胜千言", [4969, 6005, 8837])
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="专题数据对比"))

)
bar2.render("./res/掘金数据柱形图.html")
