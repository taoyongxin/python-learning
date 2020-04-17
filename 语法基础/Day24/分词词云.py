"""
分词词云
@Date 2020.04.17
"""
# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='GnBu',
    font_path='./res/font/SimHei.ttf'
)
# 调用jieba的Lcut()方法对原始文本进行中文分词，得到string
txt = '我如果爱你——绝不像攀援的凌霄花，借你的高枝炫耀自己：\
    我如果爱你——绝不学痴情的鸟儿，为绿荫重复单调的歌曲；\
    也不止像泉源，常年送来清凉的慰籍；也不止像险峰，\
    增加你的高度，衬托你的威仪。甚至日光。甚至春雨。\
    不，这些都还不够！我必须是你近旁的一百株木棉，做为树的形象和你站在一起。\
    根，紧握在地下，叶，相触在云里。每一阵风过，我们都互相致意，\
    但没有人听懂我们的言语。你度有你的铜枝铁干，像刀，像剑知，也像戟，\
    我有我的红硕花朵，像沉重的叹息，又像英勇的火炬，我们分担寒潮、\
    风雷、霹雳；我们共享雾霭、流岚、虹霓，仿佛永远分离，却又终身相依，\
    这才是道伟大的爱情，坚贞就在这里：爱，不仅爱你伟岸的身躯，\
    也爱你坚持的位置，脚下的土地。'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('./res/img/output4.png')
