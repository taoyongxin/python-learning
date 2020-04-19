"""
excel操作
@Date 2020.04.18
pip3 install xlrd
"""
import xlrd
import wordcloud
import random


# 1、打开工作簿
workbook = xlrd.open_workbook('./res/excel/班级卡片数据.xlsx')

# 2.工作表
# 输出所有sheet的名字
print(workbook.sheet_names())
# 获取所有的sheet
print(workbook.sheets())
# 根据索引获取sheet
# #<xlrd.sheet.Sheet object at 0x7fa69c141a58>
print(workbook.sheet_by_index(0))
# 根据名字获取sheet
# <xlrd.sheet.Sheet object at 0x7fa69c141a58>
print(workbook.sheet_by_name('工作表1'))

# 3.行、列操作
sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)  # 42
# 获取列数
print(sheet1.ncols)  # 15
# 获取第2行内存
print(sheet1.row_values(1))
# 获取第3列内容
print(sheet1.col_values(2))

# 4.单元格操作
cell1 = sheet1.cell(1, 1).value
print(cell1)
cell2 = sheet1.row(1)[1].value
print(cell2)
cell3 = sheet1.cell(1, 2).value
print(cell3)
cell4 = sheet1.row(2)[1].value
print(cell4)

# 5.日期类型（在对应的单元格准备好日期数据）
date_value = xlrd.xldate_as_datetime(
    sheet1.cell_value(1, 5), workbook.datemode)
print(type(date_value), date_value)


def get_data(filename, sheetnum):
    dir_case = './res/excel/' + filename + '.xlsx'
    workbook = xlrd.open_workbook(dir_case)
    table = workbook.sheets()[sheetnum]
    nor = table.nrows
    nol = table.ncols
    dict = {}
    for i in range(1, nor):
        for j in range(nol):
            title = table.cell_value(0, j)
            value = table.cell_value(i, j)
            dict[title] = value
        yield dict


if __name__ == "__main__":
    student_list = get_data('班级卡片数据', 0)
    students_name = ''
    for dic in student_list:
        print(dic)
        students_name = students_name+dic['姓名']+','
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='#eeeeee',
                            colormap='tab20b',
                            font_path='./res/font/SimHei.ttf')
    w.generate(students_name)
    w.to_file('./res/img/班级资料卡词云.png')
