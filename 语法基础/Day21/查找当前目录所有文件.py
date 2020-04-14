"""
查找当前目录所有文件
@Date 2020.04.14
"""
import os
import pyecharts.options as opts
from pyecharts.charts import Pie

txt_numbers = 0
json_numbers = 0
csv_numbers = 0
jpg_numbers = 0
png_numbers = 0
html_numbers = 0


def get_all(cwd):
    result = []
    # 遍历当前目录，获取文件列表，自己调试看各个步骤的结果
    get_dir = os.listdir(cwd)
    # print(get_dir)
    for i in get_dir:
        # 把第一步获取的文件加入路径
        # print(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件夹名放入列表
            file_name = os.path.basename(sub_dir)
            # print(file_name)
            # 取出字符串点以后的字符
            print(file_name.split(".")[-1])
            if file_name.split(".")[-1] == 'txt':
                global txt_numbers
                txt_numbers += 1
            elif file_name.split(".")[-1] == 'json':
                global json_numbers
                json_numbers += 1
            elif file_name.split(".")[-1] == 'csv':
                global csv_numbers
                csv_numbers += 1
            elif file_name.split(".")[-1] == 'jpg':
                global jpg_numbers
                jpg_numbers += 1
            elif file_name.split(".")[-1] == 'png':
                global png_numbers
                png_numbers += 1
            elif file_name.split(".")[-1] == 'html':
                global html_numbers
                html_numbers += 1
            result.append(file_name)
    # 累计各个类型的文件的数量
    print("txt数目为：", txt_numbers)
    print("json数目为：", json_numbers)
    print("csv数目为：", csv_numbers)
    print("jpg数目为：", jpg_numbers)
    print("png数目为：", png_numbers)
    print("html数目为：", html_numbers)
    return result


def draw(txt, json, csv, jpg, png, html):
    x_data = ["txt", "json", "csv",
              "jpg", "png", "html"]
    y_data = [txt, json, csv,
              jpg, png, html]
    (
        Pie(init_opts=opts.InitOpts(width="1600px", height="1000px"))
        .set_colors(["#9c88ff", "#00a8ff", "#fbc531", "#ff6b81", "#ff7f50", "#a4b0be"])
        .add(
            series_name="文件类型",
            data_pair=[list(z) for z in zip(x_data, y_data)],
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            # label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
        .render("./res/测试饼状图.html")
    )


if __name__ == "__main__":
    # 获取当前目录:/home/tao000101/demo
    cur_path = os.getcwd() + '/res'
    # print(cur_path) #/home/tao000101/demo/res
    # 调用函数，统计res目录下文件
    print('当前目录的所有文件', get_all(cur_path))
    draw(txt_numbers, json_numbers, csv_numbers,
         jpg_numbers, png_numbers, html_numbers)
    # 扩展，按文件类型统计后绘制一个饼图
