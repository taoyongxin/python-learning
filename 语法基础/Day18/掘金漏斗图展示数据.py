import pyecharts.options as opts
from pyecharts.charts import Funnel

x_data = ["上班摸鱼", "一图胜千言", "今天学到了", "树洞一下", "今日最佳"]
y_data = [100, 80, 60, 40, 20]

data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

(
    Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data_pair=data,
        gap=2,
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="掘金专题热度", subtitle="按照热度排行"))
    .render("./res/掘金漏斗图.html")
)
